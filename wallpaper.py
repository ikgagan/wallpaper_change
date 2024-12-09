import os
import ctypes
import time
import requests
from io import BytesIO
from PIL import Image

# Function to download an image from the internet
def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        raise Exception("Failed to download image.")

# Function to set the wallpaper (Windows)
def set_wallpaper(image_path):
    # Set wallpaper using ctypes
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

# Function to save image to a temporary file
def save_image(image_data, path="wallpaper.jpg"):
    image = Image.open(image_data)
    image.save(path)
    return path

# URL list of images
image_urls = [
    "https://images.pexels.com/photos/1485894/pexels-photo-1485894.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    "https://images.pexels.com/photos/2246476/pexels-photo-2246476.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
]

# Main function to cycle wallpapers
def main():
    try:
        while True:
            for url in image_urls:
                print(f"Downloading image from: {url}")
                image_data = download_image(url)
                image_path = save_image(image_data)
                
                print("Setting wallpaper...")
                set_wallpaper(os.path.abspath(image_path))
                
                print("Wallpaper changed! Waiting for 10 seconds...")
                time.sleep(10)  # Wait 10 seconds before changing
    except KeyboardInterrupt:
        print("Program stopped.")

if __name__ == "__main__":
    main()
