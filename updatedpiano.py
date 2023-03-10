# -*- coding: utf-8 -*-
"""updatedpiano.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LOQF2yQHpyDbCVl56HK7qtLfemHnmzhV
"""

import cv2
import numpy as np

# Read the keyboard image
img = cv2.imread("/content/key.jpg")

# Define a function to detect the shape of a piano key
def detect_key(img, key_color):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply threshold to the grayscale image
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

    # Find contours in the threshold image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # Approximate the contour to a polygon
        epsilon = 0.01 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        # Check if the polygon has 4 vertices (indicating a rectangle)
        if len(approx) == 4:
            # Get the bounding rect of the contour
            x, y, w, h = cv2.boundingRect(approx)

            # Check if the key color matches the input key color
            color = img[y+h//2, x+w//2]
            if np.allclose(color, key_color, atol=50):
                return (x, y, w, h)

    return None

# Define the color of the piano key to be detected (in BGR format)
key_color = (255, 0, 0)

# Input the note for the key to be indicated
note = input("Enter a single piano key (e.g. C): ")

# Map the input note to the position of the key on the mini keyboard image
key_map = {
    "C": 1,
    "C#": 2,
    "D": 3,
    "D#": 4,
    "E": 5,
    "F": 6,
    "F#": 7,
    "G": 8,
    "G#": 9,
    "A": 10,
    "A#": 11,
    "B": 12
}
key_pos = key_map.get(note)

if key_pos is not None:
    # Get the position of the key on the keyboard image
    key_rect = detect_key(img, key_color)

    # Check if the key was found
    if key_rect is not None:
        # Draw a red circle on the key
        x, y, w, h = key_rect
        cv2.circle(img, (x+w//2, y+h//2), w//2, (0, 0, 255), -1)

        # Display the image with the indicated key
        cv2.imshow("Mini Keyboard", img)
        cv2.waitKey(0)
else:
    print("Invalid piano key entered.")

import cv2
import numpy as np

# Read the keyboard image
img = cv2.imread("/content/dfghdfggb.jpg")

# Define a function to detect the shape of a piano key
def detect_key(img, template):
    # Apply template matching to find the key in the image
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    # Get the coordinates of the highest match
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Check if the match is good enough
    if max_val > 0.8:
        return max_loc

    return None

# Input the note for the key to be indicated
note = input("Enter a single piano key (e.g. C): ")

# Load the template for the corresponding key
template = cv2.imread(f"{note}.jpg")

if template is not None:
    # Get the position of the key on the keyboard image
    key_loc = detect_key(img, template)

    # Check if the key was found
    if key_loc is not None:
        # Draw a red circle on the key
        x, y = key_loc
        cv2.circle(img, (x+template.shape[1]//2, y+template.shape[0]//2), template.shape[1]//2, (0, 0, 255), -1)

        # Display the image with the indicated key
        cv2.imshow("Mini Keyboard", img)
        cv2.waitKey(0)
else:
    print("Template for the given piano key not found.")

import cv2
import numpy as np
import os

# Read the keyboard image
img = cv2.imread("/content/key.jpg")

# Define a function to detect the shape of a piano key
def detect_key(img, template):
    # Apply template matching to find the key in the image
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    # Get the coordinates of the highest match
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Check if the match is good enough
    if max_val > 0.8:
        return max_loc

    return None

# Input the note for the key to be indicated
note = input("Enter a single piano key (e.g. C): ")
template_path = f"{note}.jpg"

if os.path.exists(template_path):
    template = cv2.imread(template_path)

    if template is not None:
        # Get the position of the key on the keyboard image
        key_loc = detect_key(img, template)

        # Check if the key was found
        if key_loc is not None:
            # Draw a red circle on the key
            x, y = key_loc
            cv2.circle(img, (x+template.shape[1]//2, y+template.shape[0]//2), template.shape[1]//2, (0, 0, 255), -1)

            # Display the image with the indicated key
            cv2.imshow("Mini Keyboard", img)
            cv2.waitKey(0)
else:
    print("Template for the given piano key not found.")

import cv2
import numpy as np
import os

# Read the keyboard image
img = cv2.imread("/content/key.jpg")

# Define a function to detect the shape of a piano key
def detect_key(img, template):
    # Apply template matching to find the key in the image
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    # Get the coordinates of the highest match
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Check if the match is good enough
    if max_val > 0.8:
        return max_loc

    return None

# Input the note for the key to be indicated
note = input("Enter a single piano key (e.g. C): ")
template_path = f"{note}.jpg"

if os.path.exists(template_path):
    template = cv2.imread(template_path)

    if template is not None:
        # Get the position of the key on the keyboard image
        key_loc = detect_key(img, template)

        # Check if the key was found
        if key_loc is not None:
            # Draw a red circle on the key
            x, y = key_loc
            cv2.circle(img, (x+template.shape[1]//2, y+template.shape[0]//2), template.shape[1]//2, (0, 0, 255), -1)

            # Display the image with the indicated key
            cv2.imshow("Mini Keyboard", img)
            cv2.waitKey(0)
else:
    print(f"Template image for the key '{note}' not found in the current working directory.")

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/pia

ls

!pwd

!python paidetec.py

!pip install opencv-python
!pip install opencv-python-headless



!pip install opencv-python
!pip install opencv-python-headless

import cv2
import numpy as np
import os

# Read the keyboard image from a URL
!wget -O mini_keyboard.jpg https://your_url/mini_keyboard.jpg
img = cv2.imread("/content/dfghdfggb.jpg")

# Define a function to detect the shape of a piano key
def detect_key(img, template):
    # Apply template matching to find the key in the image
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    # Get the coordinates of the highest match
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Check if the match is good enough
    if max_val > 0.8:
        return max_loc

    return None

# Input the note for the key to be indicated
note = input("Enter a single piano key (e.g. C): ")
template_path = f"{note}.jpg"

if os.path.exists(template_path):
    template = cv2.imread(template_path)

    if template is not None:
        # Get the position of the key on the keyboard image
        key_loc = detect_key(img, template)

        # Check if the key was found
        if key_loc is not None:
            # Map the input note to the position of the key on the mini keyboard image
            notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
            key_positions = [(i * template.shape[1], 0) for i in range(32)]
            key_index = notes.index(note)

            x, y = key_positions[key_index]

            # Draw a red circle on the key
            cv2.circle(img, (x+template.shape[1]//2, y+template.shape[0]//2), template.shape[1]//2, (0, 0, 255), -1)

            # Display the image with the indicated key
            cv2.imshow("Mini Keyboard", img)
            cv2.waitKey(0)
else:
    print(f"Template image for the key '{note}' not found in the current working directory.")

import cv2
import numpy as np

# Load the mini keyboard image
keyboard = cv2.imread("key.jpg")

# Map the input note to the position of the key on the mini keyboard image
note = input("Enter a piano key (e.g. 'C'): ").lower()

# Define the mapping from notes to positions on the mini keyboard
key_mapping = {
    'c': (100, 200),
    'd': (150, 200),
    'e': (200, 200),
    'f': (250, 200),
    'g': (300, 200),
    'a': (350, 200),
    'b': (400, 200)
}

if note not in key_mapping:
    print("Invalid input. Please enter a valid piano key (e.g. 'C', 'D', 'E', 'F', 'G', 'A', or 'B').")
    exit()

center_x, center_y = key_mapping[note]

# Draw a red circle at the center of the key on the mini keyboard image
cv2.circle(keyboard, (center_x, center_y), 5, (0, 0, 255), -1)

# Show the image with the red circle
cv2.imshow("Keyboard with marked key", keyboard)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Load the mini keyboard image
keyboard = cv2.imread("key.jpg")

# Map the input note to the position of the key on the mini keyboard image
note = input("Enter a piano key (e.g. 'C'): ").lower()

# Define the mapping from notes to positions on the mini keyboard
key_mapping = {
    'c': (100, 200),
    'd': (150, 200),
    'e': (200, 200),
    'f': (250, 200),
    'g': (300, 200),
    'a': (350, 200),
    'b': (400, 200)
}

if note not in key_mapping:
    print("Invalid input. Please enter a valid piano key (e.g. 'C', 'D', 'E', 'F', 'G', 'A', or 'B').")
    exit()

center_x, center_y = key_mapping[note]

# Draw a red circle at the center of the key on the mini keyboard image
cv2.circle(keyboard, (center_x, center_y), 5, (0, 0, 255), -1)

# Show the image with the red circle
cv2_imshow(keyboard)

import cv2
import numpy as np

# Load the keyboard image
keyboard = cv2.imread("key.jpg")

# Dictionary to map input notes to positions on the keyboard image
key_mapping = {
    'c': (512, 256),
    'd': (576, 256),
    'e': (640, 256),
    'f': (704, 256),
    'g': (768, 256),
    'a': (832, 256),
    'b': (896, 256)
}

def mark_key(note):
    # Get the position of the key on the keyboard image
    pos = key_mapping.get(note.lower(), None)
    if pos is None:
        print("Key not found in mapping")
        return

    # Draw a red circle on the keyboard image to indicate the position of the key
    cv2.circle(keyboard, pos, 20, (0,0,255), -1)

# Example usage
note = input("Enter a note (c, d, e, f, g, a, b): ")
mark_key(note)

# Display the marked keyboard image
cv2.imshow("Keyboard with marked key", keyboard)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# Get the screen resolution from the user
screen_height = int(input("Enter screen height: "))
screen_width = int(input("Enter screen width: "))

# Load the keyboard image
keyboard = cv2.imread("key.jpg")

# Define the notes in the mini keyboard
notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']

# Define the mapping of each note to its position on the keyboard
key_mapping = {}
key_width = screen_width // 32
key_height = screen_height // 4
for i, note in enumerate(notes):
    key_mapping[note] = (key_width * (2 * i + 1), key_height * 2)

# Get the input note from the user
note = input("Enter a note (c, d, e, f, g, a, b): ").lower()

# Check if the input note is valid
if note not in notes:
    print("Invalid input. Please enter a valid note (c, d, e, f, g, a, b).")
else:
    # Get the position of the note on the keyboard
    x, y = key_mapping[note]

    # Draw a red circle at the position of the note
    cv2.circle(keyboard, (x, y), 10, (0, 0, 255), -1)

    # Display the keyboard with the marked key
    cv2.imwrite("keyboard_with_mark.jpg", keyboard)
    print("Keyboard with marked key saved as 'keyboard_with_mark.jpg'.")

import cv2
import numpy as np
import time
import pandas as pd

# Get the screen resolution from the user
screen_height = int(input("Enter screen height: "))
screen_width = int(input("Enter screen width: "))

# Load the keyboard image
keyboard = cv2.imread("key.jpg")

# Define the notes in the mini keyboard
notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']

# Define the mapping of each note to its position on the keyboard
key_mapping = {}
key_width = screen_width // 32
key_height = screen_height // 4
for i, note in enumerate(notes):
    key_mapping[note] = (key_width * (2 * i + 1), key_height * 2)

# Get the input notes from a CSV file
notes_df = pd.read_csv("pianotesf.csv")
notes_list = notes_df['Notes'].tolist()

# Get the time interval for displaying the red dot for each note
time_interval = 1 # in seconds

# Get the live video stream or test on a video or image
video_source = int(input("Enter 1 for live video stream, 2 for video file, 3 for image file: "))
if video_source == 1:
    cap = cv2.VideoCapture(0)
elif video_source == 2:
    video_file = input("Enter the video file name with extension: ")
    cap = cv2.VideoCapture(video_file)
else:
    image_file = input("Enter the image file name with extension: ")
    frame = cv2.imread(image_file)

for note in notes_list:
    # Check if the input note is valid
    if note.lower() not in notes:
        print("Invalid input. Please enter a valid note (c, d, e, f, g, a, b).")
    else:
        # Get the position of the note on the keyboard
        x, y = key_mapping[note.lower()]

        # Draw a red circle at the position of the note
        cv2.circle(keyboard, (x, y), 10, (0, 0, 255), -1)

        # Display the keyboard with the marked key
        if video_source == 1:
            ret, frame = cap.read()
            if ret == False:
                break
        elif video_source == 2:
            ret, frame = cap.read()
            if ret == False:
                break
        cv2.imwrite("keyboard_with_mark.jpg", keyboard)
        print("Keyboard with marked key saved as 'keyboard_with_mark.jpg'.")

        time.sleep(time_interval)

if video_source == 1 or video_source == 2:
    cap.release()

cv2.destroyAllWindows()

import cv2
import numpy as np
import time
import pandas as pd

# Get the screen resolution from the user
screen_height = int(input("Enter screen height: "))
screen_width = int(input("Enter screen width: "))

# Load the keyboard image
keyboard = cv2.imread("key.jpg")

# Check if the image was loaded successfully
if keyboard is None:
    print("Error: Could not load the keyboard image. Please make sure the image file exists and the path is correct.")
    exit()

# Define the notes in the mini keyboard
notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']

# Define the mapping of each note to its position on the keyboard
key_mapping = {}
key_width = screen_width // 32
key_height = screen_height // 4
for i, note in enumerate(notes):
    key_mapping[note] = (key_width * (2 * i + 1), key_height * 2)

# Get the input notes from a CSV file
notes_df = pd.read_csv("pianotesf.csv")
notes_list = notes_df['Notes'].tolist()

# Get the time interval for displaying the red dot for each note
time_interval = 1 # in seconds

# Get the live video stream or test on a video or image
video_source = int(input("Enter 1 for live video stream, 2 for video file, 3 for image file: "))
if video_source == 1:
    cap = cv2.VideoCapture(0)
elif video_source == 2:
    video_file = input("Enter the video file name with extension: ")
    cap = cv2.VideoCapture(video_file)
else:
    image_file = input("Enter the image file name with extension: ")
    frame = cv2.imread(image_file)

for note in notes_list:
    # Check if the input note is valid
    if note.lower() not in notes:
        print("Invalid input. Please enter a valid note (c, d, e, f, g, a, b).")
    else:
        # Get the position of the note on the keyboard
        x, y = key_mapping[note.lower()]

        # Draw a red circle at the position of the note
        cv2.circle(keyboard, (x, y), 10, (0, 0, 255), -1)

        # Display the keyboard with the marked key
        if video_source == 1:
            ret, frame = cap.read()
            if ret == False:
                break
        elif video_source == 2:
            ret, frame = cap.read()
            if ret == False:
                break
        cv2.imwrite("keyboard_with_mark.jpg", keyboard)
        print("Keyboard with marked key saved as 'keyboard_with_mark.jpg'.")

        time.sleep(time_interval)

if video_source == 1 or video_source == 2:
    cap.release()

cv2.destroyAllWindows()