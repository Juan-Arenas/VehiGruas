import os
from PIL import Image

def resize_image(path, max_size, quality=80):
    try:
        with Image.open(path) as img:
            # Resize
            if img.width > max_size or img.height > max_size:
                img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                img.save(path, 'webp', quality=quality)
                print(f"Resized {path} to {img.width}x{img.height}")
            else:
                # Even if dimensions are smaller, save with a slightly lower quality to compress further
                img.save(path, 'webp', quality=quality)
                print(f"Optimized {path} (no resize needed) to {img.width}x{img.height}")
    except Exception as e:
        print(f"Error processing {path}: {e}")

# Images that are used as block/gallery images and can be max 800px
images_800 = [
    'Grua1.webp', 'Grua2.webp', 'Grua3.webp', 
    'Grua4.webp', 'Grua5.webp', 'Grua6.webp', 
    'Varadoo.webp', 'Flyer VehiGruas.webp', 'Banner VehiGruas.webp'
]

# Logos and smaller icons
images_200 = ['LogoVehi.webp']

print("Starting image optimization...")
for img in images_800:
    if os.path.exists(img):
        resize_image(img, 800)

for img in images_200:
    if os.path.exists(img):
        resize_image(img, 250)

print("Finished optimizing images.")
