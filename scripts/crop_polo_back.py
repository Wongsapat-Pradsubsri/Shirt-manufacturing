import os
from PIL import Image

project_root = "c:/Users/VICTUS/Desktop/ผลิตเสื้อ/astro-t_shirt"
img_path = os.path.join(project_root, "src/assets/home/polo_back.png")

# Open original back view image
img = Image.open(img_path)
w, h = img.size

# Crop to show only the upper half of the body
# Crop area: keep left and right intact, keep top at 0, crop bottom at 60% of the height
crop_bottom = int(h * 0.60)
cropped_img = img.crop((0, 0, w, crop_bottom))

# Save the cropped image back, replacing the full-body version
cropped_img.save(img_path)
print("Successfully cropped the polo back image to show only the upper torso!")
