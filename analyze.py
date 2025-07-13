import os
import csv
from PIL import Image
import numpy as np

# Configuration
folder = "output"
output_csv = "brightness_data.csv"
search_radius = 250  # How far from center to look (in pixels)

# Get sorted list of PNG files
image_files = sorted([f for f in os.listdir(folder) if f.endswith(".png")])

# Prepare CSV output
with open(output_csv, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["frame", "brightness"])

    for filename in image_files:
        frame_number = int(os.path.splitext(filename)[0])
        img_path = os.path.join(folder, filename)

        # Open and convert image to grayscale
        with Image.open(img_path) as im:
            gray = im.convert('L')  # L mode = grayscale
            arr = np.array(gray)

            # Find brightest pixel near center
            h, w = arr.shape
            cx, cy = w // 2, h // 2
            xmin, xmax = max(cx - search_radius, 0), min(cx + search_radius, w)
            ymin, ymax = max(cy - search_radius, 0), min(cy + search_radius, h)

            sub_region = arr[ymin:ymax, xmin:xmax]
            max_val = int(np.max(sub_region))  # Brightest pixel value

            # Write frame number and brightness to CSV
            writer.writerow([frame_number, max_val])

print(f"Brightness data saved to {output_csv}")