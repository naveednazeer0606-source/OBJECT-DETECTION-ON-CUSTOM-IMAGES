# Week 3 - Computer Vision (Object Detection)

## 👁️ Project Overview
This project implements a real-time **Object Detection System** using the **YOLO (You Only Look Once)** architecture. It accesses the user's webcam, identifies objects in the video feed, and draws bounding boxes with confidence scores.

## 🎯 Challenges Completed
* **Integrated Trained Model:** utilized the pre-trained `yolov8n` model for efficient detection.
* **Real-time Inference:** Implemented a live video loop using OpenCV.
* **Label-Based Reporting:** The system identifies and labels multiple objects (Person, Cell Phone, Chair, etc.) simultaneously.

## 🛠 Tech Stack
* **Python 3.x**
* **OpenCV (`cv2`):** For video capture and image display.
* **Ultralytics YOLO:** State-of-the-art object detection model.

## 🚀 How to Run
1.  **Install Requirements:**
    ```bash
    pip install ultralytics opencv-python
    ```

2.  **Run the Script:**
    ```bash
    python object_detect.py
    ```
    *(The first run will automatically download the model weights).*

3.  **Controls:**
    * Press **'q'** to exit the camera window.

## 📷 Preview
*(Attach a screenshot of the window showing the AI detecting a person or object)*
