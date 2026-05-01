import cv2
import time
from ultralytics import YOLO

print("Loading YOLOv8 Nano...")
model = YOLO('yolov8n.pt')

# 1. Force Windows DirectShow backend
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 2. Force the MJPG codec so the USB bandwidth doesn't choke
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# 3. Set resolution to standard 1080p
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

print("Booting Sandevistan Optics... Press 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Camera feed dropped.")
        break

    start_time = time.perf_counter()
    results = model(frame, verbose=False)
    latency = (time.perf_counter() - start_time) * 1000

    annotated_frame = results[0].plot()

    cv2.putText(annotated_frame, f"AI Latency: {latency:.1f}ms", (10, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Sandy Vision Test", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
