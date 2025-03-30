import os
import urllib.request
from ultralytics import YOLO

def download_model(model_filename, model_url):
    model_path = os.path.join(os.getcwd(), model_filename)
    if not os.path.exists(model_path):
        print(f"Downloading {model_filename}...")
        try:
            urllib.request.urlretrieve(model_url, model_path)
            print(f"Model downloaded successfully and saved as {model_path}")
        except Exception as e:
            print(f"Error downloading the model: {e}")
    else:
        print(f"Model already exists at {model_path}")
    return model_path

def train_model(model_path, data_path):
    model = YOLO(model_path)
    model.train(
    data=data_path,
    epochs=1000,  # Increase if using early stopping
    imgsz=640,
    batch=2,  # Reduce from 16 to 8 (or even 4)
    device=0,  # Use 'cpu' if no GPU available
    patience=10,  # Stops training if no improvement in 10 epochs
    amp=False,  # Use mixed precision training if available
    workers=2,  # Number of workers for data loading
    optimizer='AdamW',
    cache=True,
    dropout=0.1,  # Helps prevent overfitting
    )   
    print("Training complete! Model is now trained for detecting only bikes and cars.")

if __name__ == '__main__':
    model_filename = r"runs\detect\train5\weights\best.pt"
    model_url = "https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov8m.pt"
    model_path = download_model(model_filename, model_url)
    data_path = os.path.join(os.getcwd(), "dataset", "data.yaml")
    train_model(model_path, data_path)
