import os
import random
import shutil

# Define dataset paths
dataset_path = "dataset"
train_images = os.path.join(dataset_path, "train/images")
train_labels = os.path.join(dataset_path, "train/labels")

val_images = os.path.join(dataset_path, "val/images")
val_labels = os.path.join(dataset_path, "val/labels")

# Create val folders if they don't exist
os.makedirs(val_images, exist_ok=True)
os.makedirs(val_labels, exist_ok=True)

# Get list of image files
image_files = [f for f in os.listdir(train_images) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Set percentage of images to move (e.g., 20%)
val_split = 0.1
num_val = int(len(image_files) * val_split)

# Randomly select images for validation
val_images_selected = random.sample(image_files, num_val)

# Move selected images & corresponding labels to val folder
for img_file in val_images_selected:
    # Move image
    shutil.move(os.path.join(train_images, img_file), os.path.join(val_images, img_file))
    
    # Move corresponding label file
    label_file = img_file.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt')
    if os.path.exists(os.path.join(train_labels, label_file)):
        shutil.move(os.path.join(train_labels, label_file), os.path.join(val_labels, label_file))

print(f"✅ Moved {num_val} images and labels to val folder!")
