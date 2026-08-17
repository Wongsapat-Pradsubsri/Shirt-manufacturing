import os
from PIL import Image
import numpy as np

project_root = "c:/Users/VICTUS/Desktop/ผลิตเสื้อ/astro-t_shirt"
img_path = os.path.join(project_root, "src/assets/home/jacket_premium.png")

img = Image.open(img_path).convert("RGB")
arr = np.array(img, dtype=np.float32)

h, w, _ = arr.shape

points = {
    "wall_left": (int(h * 0.5), int(w * 0.1)),
    "wall_top_right": (int(h * 0.1), int(w * 0.8)),
    "hanger": (int(h * 0.22), int(w * 0.5)),
    "collar": (int(h * 0.28), int(w * 0.5)),
    "jacket_body": (int(h * 0.5), int(w * 0.5)),
    "jacket_sleeve_left": (int(h * 0.5), int(w * 0.25)),
}

print(f"Image dimensions: {w}x{h}")
for name, (y, x) in points.items():
    rgb = arr[y, x]
    r, g, b = rgb
    total = r + g + b
    r_n = r / total
    g_n = g / total
    b_n = b / total
    print(f"{name} at (y={y}, x={x}): RGB={rgb}, Chromaticity=({r_n:.3f}, {g_n:.3f}, {b_n:.3f}), Brightness={total/3:.1f}")
