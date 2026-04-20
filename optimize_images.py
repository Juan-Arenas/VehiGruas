import os
from PIL import Image

def compress_insanely(path, quality=20):
    try:
        with Image.open(path) as img:
            img.save(path, 'webp', quality=quality, method=6)
            print(f"Insanely compressed {path} at quality {quality}")
    except Exception as e:
        print(f"Error processing {path}: {e}")

images_to_crush = [
    'Grua1.webp', 'Grua4.webp', 'Grua5.webp', 
    'Grua2.webp', 'Grua3.webp', 'Grua6.webp', 
    'Varadoo.webp', 'Flyer VehiGruas.webp'
]

print("Starting INSANE image compression...")
for img in images_to_crush:
    if os.path.exists(img):
        compress_insanely(img, quality=20)

print("Finished insane compression.")
