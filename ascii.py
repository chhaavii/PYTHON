import cv2
import numpy as np
from PIL import Image

# ASCII characters used for conversion (from darkest to brightest)
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """Resize image maintaining aspect ratio"""
    width, height = image.shape[1], image.shape[0]
    aspect_ratio = height/width
    new_height = int(aspect_ratio * new_width)
    return cv2.resize(image, (new_width, new_height))

def pixels_to_ascii(image):
    """Convert pixels to ASCII characters"""
    pixels = image.flatten()
    # Map pixel values (0-255) to ASCII characters
    ascii_str = ''
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//32]
    return ascii_str

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Convert to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Resize image
    resized_frame = resize_image(gray_frame)
    
    # Convert to ASCII
    ascii_frame = pixels_to_ascii(resized_frame)
    
    # Split the string based on image width
    ascii_frame = '\n'.join(ascii_frame[i:i+resized_frame.shape[1]] 
                           for i in range(0, len(ascii_frame), resized_frame.shape[1]))
    
    # Clear console and print ASCII art
    print('\033[H\033[J')  # Clear console
    print(ascii_frame)
    
    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
