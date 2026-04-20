import os
from PIL import Image

def resize_and_compress(path, max_size, quality=65):
    try:
        with Image.open(path) as img:
            # We want to aggressively downsize and compress to satisfy Lighthouse
            if img.width > max_size or img.height > max_size:
                img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                
            img.save(path, 'webp', quality=quality, method=6) # method=6 is the slowest but best compression
            print(f"Crushed {path} to dimensions {img.width}x{img.height} at quality {quality}")
    except Exception as e:
        print(f"Error processing {path}: {e}")

images_650 = [
    'Grua1.webp', 'Grua2.webp', 'Grua3.webp', 
    'Grua4.webp', 'Grua5.webp', 'Grua6.webp', 
    'Varadoo.webp', 'Flyer VehiGruas.webp'
]

# Banner needs to stay a bit wider for desktop hero, maybe 800px but lower quality
images_800 = ['Banner VehiGruas.webp']

images_150 = ['LogoVehi.webp', 'Fav.webp']

print("Starting deep image compression...")
for img in images_650:
    if os.path.exists(img):
        resize_and_compress(img, 650, quality=65)

for img in images_800:
    if os.path.exists(img):
        resize_and_compress(img, 800, quality=65)

for img in images_150:
    if os.path.exists(img):
        resize_and_compress(img, 150, quality=70)

print("Finished deep compression.")
