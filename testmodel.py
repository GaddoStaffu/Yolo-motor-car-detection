import cv2
import argparse
import os
from ultralytics import YOLO

# Load the trained YOLO model
model = YOLO(r"runs\detect\yolov8s-costume-model\weights\best.pt")  # Replace with the path to your trained model

def process_frame(frame):
    results = model(frame)
    for result in results:
        for box in result.boxes.data:
            x1, y1, x2, y2, conf, cls = box.tolist()
            label = model.names[int(cls)]
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f'{label} {conf:.2f}', (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame

def process_webcam():
    capture = cv2.VideoCapture(0)
    capture.set(3, 1366)
    capture.set(4, 768)
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        frame = process_frame(frame)
        cv2.imshow("YOLO Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

def process_video(video_path):
    capture = cv2.VideoCapture(video_path)
    while capture.isOpened():
        ret, frame = capture.read()
        if not ret:
            break
        frame = process_frame(frame)
        cv2.imshow("YOLO Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

def process_image(image_path):
    frame = cv2.imread(image_path)
    frame = process_frame(frame)
    cv2.imshow("YOLO Image", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_images(folder_path):
    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        if img_path.lower().endswith((".jpg", ".jpeg", ".png")):
            process_image(img_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--webcam", action="store_true", help="Use webcam for live detection")
    parser.add_argument("--videofile", type=str, help="Path to video file")
    parser.add_argument("--image", type=str, help="Path to an image file")
    parser.add_argument("--images", type=str, help="Path to a folder containing images")
    args = parser.parse_args()

    if args.webcam:
        process_webcam()
    elif args.videofile:
        process_video(args.videofile)
    elif args.image:
        process_image(args.image)
    elif args.images:
        process_images(args.images)
    else:
        print("Please specify an input method: --webcam, --videofile, --image, or --images")
