import os



# This script filters out irrelevant classes from YOLOv8 labels
# Paths to label folders
train_label_dir = r"C:\Users\GaddoStaffu\Desktop\VehicleDetection\dataset\train\labels"
val_label_dir = r"C:\Users\GaddoStaffu\Desktop\VehicleDetection\dataset\val\labels"

# Keep only these class IDs
valid_classes = {0, 2}  # 0 = bike, 2 = car

def filter_labels(label_dir):
    for filename in os.listdir(label_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(label_dir, filename)
            
            with open(file_path, "r") as f:
                lines = f.readlines()
            
            # Keep only lines where class_id is 0 or 2
            filtered_lines = [line for line in lines if int(line.split()[0]) in valid_classes]

            # Overwrite the file only if there are valid labels left
            if filtered_lines:
                with open(file_path, "w") as f:
                    f.writelines(filtered_lines)
            else:
                os.remove(file_path)  # Delete empty label files

# Apply filtering to both train and validation labels
filter_labels(train_label_dir)
filter_labels(val_label_dir)

print("Filtering complete. Only 'bike' and 'car' labels remain.")
