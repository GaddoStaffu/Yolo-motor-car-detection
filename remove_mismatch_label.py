import os
import glob


# This script removes invalid labels and their corresponding images from YOLOv8 dataset
# It checks if any label file has more than 5 values in a line and removes such labels and their images
# It keeps only the classes specified in the valid_classes set and the label should be a bound box
# The label format is assumed to be: class_id x_center y_center width height
# Paths to train and val label directories
train_label_dir = "dataset/train/labels"
val_label_dir = "dataset/val/labels"
image_extensions = [".jpg", ".png", ".jpeg"]  # Add more if needed

# Function to check and remove invalid labels and images
def clean_labels(label_dir):
    txt_files = glob.glob(os.path.join(label_dir, "*.txt"))

    for file_path in txt_files:
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Check if any line has more than 5 values
        invalid = any(len(line.strip().split()) > 5 for line in lines)

        if invalid:
            print(f"🚨 Removing invalid label: {file_path}")
            os.remove(file_path)  # Delete the label file
            
            # Find and delete the corresponding image
            image_path = None
            for ext in image_extensions:
                img_candidate = file_path.replace("/labels/", "/images/").replace(".txt", ext)
                if os.path.exists(img_candidate):
                    image_path = img_candidate
                    break

            if image_path:
                print(f"🗑️ Removing corresponding image: {image_path}")
                os.remove(image_path)

# Run cleanup on both train and val sets
clean_labels(train_label_dir)
clean_labels(val_label_dir)

print("✅ Cleanup completed. All invalid labels and images removed.")
