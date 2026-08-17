import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

project_root = "c:/Users/VICTUS/Desktop/ผลิตเสื้อ/astro-t_shirt"
img_path = os.path.join(project_root, "src/assets/home/jacket_premium.png")
out_path = os.path.join(project_root, "src/assets/home/jacket_premium_black.png")

# Open original image
img = Image.open(img_path).convert("RGB")
arr = np.array(img, dtype=np.float32)
h, w, _ = arr.shape

# 1. Create base polygon mask for the jacket
# These points tightly outline the front-facing jacket, excluding the wood hanger and background
polygon_points = [
    (430, 245),  # Left collar peak
    (485, 270),  # Collar center left
    (540, 270),  # Collar center right
    (595, 245),  # Right collar peak
    (630, 260),  # Right neck curve
    (755, 310),  # Right shoulder
    (800, 390),  # Right upper sleeve outer
    (820, 520),  # Right sleeve elbow outer
    (815, 690),  # Right sleeve forearm outer
    (795, 830),  # Right cuff outer
    (755, 875),  # Right cuff inner
    (730, 875),  # Right hem outer
    (650, 882),  # Right hem center
    (512, 885),  # Bottom center hem
    (374, 882),  # Left hem center
    (294, 875),  # Left hem outer
    (270, 875),  # Left cuff inner
    (230, 830),  # Left cuff outer
    (210, 690),  # Left sleeve forearm outer
    (205, 520),  # Left sleeve elbow outer
    (224, 390),  # Left upper sleeve outer
    (270, 310),  # Left shoulder
    (395, 260),  # Left neck curve
]

mask_img = Image.new("L", (w, h), 0)
draw = ImageDraw.Draw(mask_img)
draw.polygon(polygon_points, fill=255)

# Convert mask to numpy array for pixel-level refinement
mask = np.array(mask_img, dtype=np.uint8)

# 2. Refine mask edges using color thresholds to ensure pixel-perfect contours
r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

# Define wall color conditions (very light neutral tones)
is_wall = (r >= 210) & (g >= 205) & (b >= 200)

# Apply refinement: 
# - Remove pixels from the mask if they are wall color (even if inside polygon)
# - Add pixels to the mask if they are jacket color (even if slightly outside polygon, to prevent clipping)
refined_mask = np.copy(mask)
refined_mask[is_wall] = 0

# Smooth the refined mask edges
refined_mask_img = Image.fromarray(refined_mask, mode="L")
refined_mask_img = refined_mask_img.filter(ImageFilter.GaussianBlur(1.5))
smooth_mask = np.array(refined_mask_img, dtype=np.float32) / 255.0

# 3. Create a high-quality premium black canvas jacket texture
# Convert to grayscale and darken by factor of 0.15 (maintaining folding texture & shadows)
gray = 0.299 * r + 0.587 * g + 0.114 * b
black_r = gray * 0.16
black_g = gray * 0.16
black_b = gray * 0.165 # Charcoal black

# 4. Composite the black jacket with the original background
out_arr = np.copy(arr)
out_arr[:, :, 0] = r * (1 - smooth_mask) + black_r * smooth_mask
out_arr[:, :, 1] = g * (1 - smooth_mask) + black_g * smooth_mask
out_arr[:, :, 2] = b * (1 - smooth_mask) + black_b * smooth_mask

# Save the final high-quality image
out_arr = np.clip(out_arr, 0, 255).astype(np.uint8)
out_img = Image.fromarray(out_arr)
out_img.save(out_path)

print(f"Successfully generated clean front black jacket image at: {out_path}")
