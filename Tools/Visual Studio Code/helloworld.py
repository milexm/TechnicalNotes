""" 
Module helloworld.py
This is partciular helloworld program; a litte mpre than the simplistic one.
It performs the following tasks:

1) It downloads an MP3 from the internet.
2) It loads the MP3 into `pygame.mixer` and plays it.
3) It fetches and displays an image of Earth from space using PIL and matplotlib.

The program keeps running until the music stops.

Prerequisites

To execute the program you need to install the following packages:

pip install pygame
pip install pillow
pip install requests

"""
import pygame
import requests
import io
from PIL import Image
import matplotlib.pyplot as plt

# URL of a happy tune
mp3_url = "https://download.samplelib.com/mp3/sample-15s.mp3"

# Download the MP3 file
print("Downloading the happy tune...")
response = requests.get(mp3_url)
if response.status_code == 200:
    mp3_data = io.BytesIO(response.content)
    print("Download complete!")
else:
    print("Failed to download the audio file.")
    exit()

# Initialize pygame mixer and play the downloaded MP3 file
pygame.mixer.init()
pygame.mixer.music.load(mp3_data)
pygame.mixer.music.play()

# Load and display the Earth image from the ISS
earth_image_url = "https://eoimages.gsfc.nasa.gov/images/imagerecords/87000/87167/globe_epc_2015238_lrg.jpg"

print("Downloading the Earth image...")
earth_response = requests.get(earth_image_url, stream=True)
if earth_response.status_code == 200:
    earth_image = Image.open(io.BytesIO(earth_response.content))
    print("Earth image loaded!")
    print("Close the image to exit!")
else:
    print("Failed to load Earth image.")
    exit()

# Display the image
plt.imshow(earth_image)
plt.axis("off")  # Hide axes
plt.title("Hello, World! 🌍")
plt.show()



def main():
    # Keep the program running while music is playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(1000)
    
    print("Program finished!")

if __name__ == "__main__":
    main()