import cv2
import pickle
import numpy as np
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Load the video feed
video_path = "carPark.mp4"
if not os.path.exists(video_path):
    print(f"🚨 Error: Video file '{video_path}' not found!")
cap = cv2.VideoCapture(video_path)

# Load parking positions
posList_file = "CarParkPos"
try:
    with open(posList_file, "rb") as f:
        posList = pickle.load(f)
except FileNotFoundError:
    print(f"🚨 Error: Parking positions file '{posList_file}' not found! Run ParkingSpacePicker.py first.")
    posList = []

width, height = 107, 48  # Parking space dimensions

def check_parking_space():
    """Detects occupied/free parking spaces and saves an image."""
    success, img = cap.read()
    if not success:
        print("🚨 Error: Could not read video file. Check if 'carPark.mp4' exists.")
        return {"error": "Video file not found"}

    # Preprocess the image
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(
        imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16
    )
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    space_counter = 0
    spaces_status = []

    for idx, pos in enumerate(posList, start=1):  # Add spot numbers
        x, y = pos
        imgCrop = imgDilate[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 255, 0)
            status = "Free"
            space_counter += 1
        else:
            color = (0, 0, 255)
            status = "Occupied"

        spaces_status.append({"spot": f"Parking Spot {idx}", "status": status})
        cv2.rectangle(img, (x, y), (x + width, y + height), color, 3)

    if not os.path.exists("static"):
        os.makedirs("static")

    cv2.imwrite("static/parking_status.jpg", img)

    return {
        "total_spaces": len(posList),
        "free_spaces": space_counter,
        "spaces": spaces_status,
        "image_url": "/static/parking_status.jpg",
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    parking_data = check_parking_space()  # ✅ Call function to get latest data
    return jsonify(parking_data)

if __name__ == "__main__":
    print("🚀 Starting Flask Server...")
    app.run(debug=True)
