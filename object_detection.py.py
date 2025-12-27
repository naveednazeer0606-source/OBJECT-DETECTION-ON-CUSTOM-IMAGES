from ultralytics import YOLO
import cv2

def detect_objects():
    # 1. Load the pre-trained YOLOv8 model
    # 'yolov8n.pt' is the nano version (fastest). 
    # You can also use 'yolov8m.pt' (medium) or 'yolov8x.pt' (extra large/accurate)
    print("Loading model...")
    model = YOLO('yolov8n.pt') 

    # --- OPTION A: Run on an Image ---
    # Replace 'test_image.jpg' with the path to your image file
    # source='path/to/your/image.jpg'
    
    # --- OPTION B: Run on a Video ---
    # Replace 'test_video.mp4' with your video path
    # source='path/to/your/video.mp4'
    
    # --- OPTION C: Live Webcam (Great for demos!) ---
    source = 0  
    
    # 2. Run Inference
    # show=True opens a window with the results
    # save=True saves the resulting video/image to 'runs/detect/exp'
    print(f"Starting detection on source: {source}")
    results = model.predict(source=source, show=True, conf=0.5, save=True)

    # Note: If using a webcam, the script runs until you press 'q' in the display window
    # or stop the terminal (Ctrl+C).

    print("Detection complete. Check the 'runs' folder for saved output.")

if __name__ == '__main__':
    detect_objects()