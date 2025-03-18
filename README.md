Car Parking Space Detection System

# Project Overview

This is a Computer Vision-based Car Parking Space Detection System that helps monitor parking spots. It uses OpenCV and cvzone to detect free and occupied parking spaces from a video feed and visually marks them. A Flask-based web application is used to display real-time parking availability.

# Features

✅ Detects free and occupied parking spaces.

✅ Shows real-time parking status on a website.

✅ Uses OpenCV for image processing.

✅ Saves parking coordinates for monitoring.

✅ Optimized for better performance and accuracy.

# Technology Stack

Programming Language: Python

Libraries: OpenCV, cvzone, NumPy, Flask, Pickle

Web Framework: Flask

Frontend: HTML, JavaScript, CSS

Data Storage: Pickle (for storing parking space coordinates)

# Installation and Setup

Prerequisites

Install Python 3.8+ on your system.

Install Dependencies

Run the following command in your terminal:

pip install opencv-python-headless numpy cvzone flask

# Project Structure

/project_folder
  ├── main.py                # Main script for parking detection
  ├── ParkingSpacePicker.py   # Tool to select parking spots
  ├── templates/
  │    ├── index.html         # Web UI for displaying parking data
  ├── static/
  │    ├── parking_status.jpg # Updated parking lot image
  ├── CarParkPos              # File storing parking spots
  ├── carPark.mp4             # Video input (or replace with webcam)
  ├── README.md               # Project documentation

How It Works

Step 1: Select Parking Spaces

python ParkingSpacePicker.py

Click on parking spaces to mark them.

Close the window to save the positions.

Step 2: Start the Detection System

python main.py

Open your browser and go to: http://127.0.0.1:5000

You will see real-time parking space detection!

Implementation Details

Parking Space Selection (ParkingSpacePicker.py)

Allows users to mark parking spaces manually.

Saves coordinates to a file for later detection.

Parking Detection (main.py)

Reads a video file or webcam feed.

Converts the frame to grayscale and applies image processing techniques.

Uses morphological operations to detect vehicles.

Saves the updated image with marked spots.

Web Interface (index.html)

Displays free and occupied parking spaces.

Refreshes every 2 seconds to update parking status.

Uses JavaScript to fetch data from main.py.

# Future Improvements

🚀 Possible Upgrades:

🔹 Integrate YOLO for AI-based car detection.

🔹 Use a database (MySQL, Firebase) to store parking logs.

🔹 Enable live camera feed instead of a pre-recorded video.

🔹 Develop a mobile app for real-time parking updates.

# Conclusion

This project successfully detects and displays real-time parking space availability using computer vision and Flask. It can be further improved by integrating AI models and storing data in a database for better monitoring.

📌 Developed by: Sumanth Kedarisetty