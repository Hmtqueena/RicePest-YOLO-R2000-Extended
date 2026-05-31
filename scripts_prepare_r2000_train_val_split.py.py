import os
import shutil
import random
import glob
from tqdm import tqdm

# Configuration
SOURCE_IMAGES_DIR = r'd:\Users\huang\Desktop\R2000\images'
SOURCE_LABELS_DIR = r'd:\Users\huang\Desktop\R2000\labels'
DEST_ROOT = r'd:\Users\huang\Desktop\R2000\original-dataset'
RANDOM_SEED = 42

def main():
    # 1. Setup
    random.seed(RANDOM_SEED)
    print(f"Seed set to {RANDOM_SEED}")
    
    # 2. Collect Pairs
    print("Scanning for image-label pairs...")
    pairs = [] # List of (image_path, label_path)
    
    # Walk through images directory
    # Structure: images/classID_xx/filename.jpg
    image_files = glob.glob(os.path.join(SOURCE_IMAGES_DIR, '*', '*.jpg'))
    
    for img_path in tqdm(image_files, desc="Matching pairs"):
        # Construct expected label path
        # image_path: .../images/classID_00/00_00000_.jpg
        # label_path: .../labels/classID_00/00_00000_.txt
        
        rel_path = os.path.relpath(img_path, SOURCE_IMAGES_DIR)
        label_rel_path = os.path.splitext(rel_path)[0] + '.txt'
        label_path = os.path.join(SOURCE_LABELS_DIR, label_rel_path)
        
        if os.path.exists(label_path):
            pairs.append((img_path, label_path))
        else:
            print(f"Warning: Label not found for {img_path}")
            
    total_pairs = len(pairs)
    print(f"Total valid pairs found: {total_pairs}")
    
    if total_pairs != 2024:
        print(f"Warning: Expected 2024 pairs, found {total_pairs}.")
        
    # 3. Shuffle
    random.shuffle(pairs)
    
    # 4. Split
    train_count = 1518
    valid_count = total_pairs - train_count
    
    train_pairs = pairs[:train_count]
    valid_pairs = pairs[train_count:]
    
    print(f"Train set: {len(train_pairs)} (Target: 1518)")
    print(f"Valid set: {len(valid_pairs)} (Target: 506)")
    
    # 5. Create Directories & Copy
    for split_name, split_pairs in [('train', train_pairs), ('valid', valid_pairs)]:
        dest_img_dir = os.path.join(DEST_ROOT, split_name, 'images')
        dest_lbl_dir = os.path.join(DEST_ROOT, split_name, 'labels')
        
        # Clean/Create directories
        if os.path.exists(dest_img_dir):
            shutil.rmtree(dest_img_dir)
        os.makedirs(dest_img_dir, exist_ok=True)
        
        if os.path.exists(dest_lbl_dir):
            shutil.rmtree(dest_lbl_dir)
        os.makedirs(dest_lbl_dir, exist_ok=True)
        
        print(f"Copying {len(split_pairs)} pairs to {split_name}...")
        
        for img_src, lbl_src in tqdm(split_pairs, desc=f"Populating {split_name}"):
            # Flat structure: just copy filename
            filename_img = os.path.basename(img_src)
            filename_lbl = os.path.basename(lbl_src)
            
            shutil.copy2(img_src, os.path.join(dest_img_dir, filename_img))
            shutil.copy2(lbl_src, os.path.join(dest_lbl_dir, filename_lbl))
            
    print("Done. Dataset reproduced in 'original-dataset'.")

if __name__ == '__main__':
    main()
