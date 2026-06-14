# 🏏 Cricket DRS System using OpenCV

## Overview

This project is a simplified Cricket Decision Review System (DRS) developed using Python and OpenCV. The system processes a cricket delivery video, detects and tracks the ball, predicts its trajectory, and generates a basic OUT/NOT OUT decision.

The project is designed as a foundation for future AI-based DRS systems and can be extended using YOLOv8 and Machine Learning techniques.

---

## Features

* Video Processing using OpenCV
* Frame Extraction from Cricket Videos
* Ball Detection using Contour Analysis
* Ball Tracking across Multiple Frames
* Ball Trajectory Visualization
* Polynomial Curve Fitting for Trajectory Prediction
* Basic DRS Decision Engine (OUT / NOT OUT)
* CSV Export of Ball Coordinates

---

## Technologies Used

* Python
* OpenCV
* NumPy
* Matplotlib
* CSV
* Git & GitHub

---

## Project Workflow

Input Cricket Video

↓

Frame Extraction

↓

Ball Detection

↓

Ball Tracking

↓

Trajectory Prediction

↓

Decision Engine

↓

OUT / NOT OUT

---

## Project Structure

DRS/

├── dataset/

├── models/

├── result/

├── videos/

└── src/

├── detection/

├── tracking/

├── trajectory/

├── lbw/

└── utils/

---

## Results

The system can:

* Extract frames from cricket videos
* Detect the cricket ball
* Track ball movement
* Generate trajectory predictions
* Produce a basic DRS decision

---

## Future Improvements

* YOLOv8-based Ball Detection
* Automatic Bounce Detection
* Stump Detection
* Advanced LBW Prediction
* Real-time Video Processing
* Research Paper Development

---

## Author

Gaurav Gupta

B.Tech Student

Allenhouse Institute of Technology
