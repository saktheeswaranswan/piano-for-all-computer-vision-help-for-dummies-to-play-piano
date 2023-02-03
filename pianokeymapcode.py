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

