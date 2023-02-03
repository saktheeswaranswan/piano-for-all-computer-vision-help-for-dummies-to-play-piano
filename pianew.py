import cv2
import numpy as np
import pandas as pd
import time

# Get the screen resolution from the user
screen_height = int(input("Enter screen height: "))
screen_width = int(input("Enter screen width: "))

# Load the keyboard image
keyboard = cv2.imread("key.jpg")

# Check if the image was loaded successfully
if keyboard is None:
    print("Error: Image not found. Please check the file path and try again.")
else:
    # Define the notes in the mini keyboard
    notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']

    # Define the mapping of each note to its position on the keyboard
    key_mapping = {}
    key_width = screen_width // 32
    key_height = screen_height // 4
    for i, note in enumerate(notes):
        key_mapping[note] = (key_width * (2 * i + 1), key_height * 2)

    # Read the input notes from an Excel file
    df = pd.read_excel("pianotesfg.xlsx")
    notes = df['Note'].tolist()

    # Iterate through the input notes
    for note in notes:
        # Get the position of the note on the keyboard
        x, y = key_mapping[note.lower()]

        # Draw a red circle at the position of the note
        cv2.circle(keyboard, (x, y), 10, (0, 0, 255), -1)

        # Display the keyboard with the marked key
        cv2.imshow("Keyboard with marked key", keyboard)

        # Wait for 1 second before marking the next key
        time.sleep(1)

    # Save the final keyboard image
    cv2.imwrite("keyboard_with_mark.jpg", keyboard)
    print("Keyboard with marked key saved as 'keyboard_with_mark.jpg'.")

