# 🤖 Automated Quality Inspection using OpenCV

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> A Computer Vision project that automatically detects defective industrial parts using OpenCV image processing techniques.

---

## 📌 Project Overview

This project simulates an automated quality inspection system used in manufacturing industries.

Using OpenCV, the system processes images of industrial parts, detects defects using image processing techniques, and classifies each part as **PASS** or **FAIL**.

---

## ✨ Features

- Image Loading
- Grayscale Conversion
- Gaussian Blur
- Binary Thresholding
- Contour Detection
- Bounding Box Detection
- Pass / Fail Classification

---

## 🛠 Technologies Used

- Python
- OpenCV
- NumPy

---

## 📂 Project Structure

```
project2-automated-quality-inspection/
│
├── README.md
├── LICENSE
├── requirements.txt
├── main.py
├── detector.py
│
├── images/
│   ├── good_part.jpg
│   ├── defective_part.jpg
│   └── README.md
│
├── output/
│   └── README.md
│
└── screenshots/
    └── README.md
```

---

## ▶️ Installation

```bash
pip install -r requirements.txt
```

Run the program

```bash
python main.py
```

---

## 🔍 Image Processing Pipeline

1. Read Image
2. Convert to Grayscale
3. Apply Gaussian Blur
4. Apply Binary Threshold
5. Detect Contours
6. Draw Bounding Boxes
7. Display PASS / FAIL Result

---

## 🚀 Future Improvements

- Live Webcam Inspection
- Conveyor Belt Simulation
- Deep Learning Object Detection
- YOLO Integration
- Real-time Dashboard

---

## 👨‍💻 Author

**Muhammad Uzair**

Electrical Engineering Student | AI & Robotics Enthusiast

---

## 📜 License

MIT License
