import cv2
import pandas as pd

# Load the key mapping from notes to positions on the mini keyboard
key_mapping = {
    'c': (85,360),
    'c#': (120, 355),
    'd': (155, 350),
    'd#': (190, 345),
    'e': (225, 340),
    'f': (260, 335),
    'f#': (295, 330),
    'g': (330, 325),
    'g#': (365, 320),
    'a': (400, 315),
    'a#': (435, 310),
    'b': (470, 305),
    'c1': (505, 300),
    'c#1': (540, 295),
    'd1': (575, 290),
    'd#1': (610, 285),
    'e1': (645, 280),
    'f1': (680, 275),
    'f#1': (715, 270),
    'g1': (750, 265),
    'g#1': (785, 260),
    'a1': (820, 255),
    'a#1': (855, 250),
    'b1': (890, 245),
    'c2': (925, 240),
    'c#2': (960, 235),
    'd2': (995, 230),
    'd#2': (1030, 225),
    'e2': (1065, 220),
    'f2': (1100, 215),
    'f#2': (1135, 210),
    'g2': (1170, 205),
    'g#2': (1205, 200)
}

# Load the entries from the csv file
entries = pd.read_csv('/home/saktheeswaran/Desktop/pianoimpo/pianotesf.csv')

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('keyboard_with_mark.mp4', fourcc, 20.0, (1280, 720))

# Open a window to display the video feed
cv2.namedWindow("keyboard_with_mark", cv2.WINDOW_NORMAL)

# Start the webcam stream
cap = cv2.VideoCapture(0)

# Loop through each entry in the csv file
for index, row in entries.iterrows():
    note = row['Note'].lower()
    center_x, center_y = key_mapping[note]
    duration = row['Duration']
    
    # Read a frame from the webcam stream
    ret, frame = cap.read()
    
    # Draw a red circle at the center of the key on the mini keyboard image
    cv2.circle(frame, (center_x, center_y), 30, (0, 0, 255), -1)
    
    # Write the frame to the video file
    out.write(frame)
    
    # Display the video feed
    cv2.imshow("keyboard_with_mark", frame)
    
    # Wait for the specified duration before displaying the next entry
    cv2.waitKey(duration)

# Release the video writer and close the window
out.release()
cv2.destroyAllWindows()

