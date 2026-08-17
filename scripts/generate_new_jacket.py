import os
import urllib.request
import urllib.parse

project_root = "c:/Users/VICTUS/Desktop/ผลิตเสื้อ/astro-t_shirt"
out_path = os.path.join(project_root, "src/assets/home/jacket_premium_black.png")

# Define the prompt for Pollinations AI
prompt = (
    "A front view of a premium black canvas bomber jacket hanging on a wooden hanger, "
    "against a clean minimalist light cream studio wall background, professional e-commerce product photography, "
    "high-quality, matching the style of adjacent product shots, no person, soft diffused lighting"
)

# Encode prompt for URL
encoded_prompt = urllib.parse.quote(prompt)
# Use the high-quality flux model hosted on pollinations
url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&private=true&model=flux"

print(f"Downloading newly generated image from: {url}")
try:
    # Add a standard user agent to avoid bot blocking
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    with urllib.request.urlopen(req) as response:
        with open(out_path, 'wb') as f:
            f.write(response.read())
    print("Successfully downloaded and saved the new generated black jacket image!")
except Exception as e:
    print(f"Error during image generation/download: {e}")
