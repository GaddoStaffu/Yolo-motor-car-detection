import os
import glob

# Define paths to train and validation label directories
train_label_dir = r"dataset\train\labels"
val_label_dir = r"dataset\val\labels"


def update_labels(label_dir: str, old_label: int, new_label: int):
    txt_files = glob.glob(os.path.join(label_dir, "*.txt"))

    for file_path in txt_files:
        with open(file_path, "r") as file:
            lines = file.readlines()
        

        updated_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts and parts[0] == str(old_label): 
                parts[0] = str(new_label)  
            updated_lines.append(" ".join(parts))

        # Overwrite the file with updated labels
        with open(file_path, "w") as file:
            file.write("\n".join(updated_lines) + "\n")
    
    print(f"Updated labels in {label_dir}")

# Update labels in train and validation sets
# replace label 2 with 1 in all .txt files
# integer a is the old label and b is the new label
# for example: replace 2 with 1
update_labels(train_label_dir, 2, 1)
update_labels(val_label_dir, 2, 1)
