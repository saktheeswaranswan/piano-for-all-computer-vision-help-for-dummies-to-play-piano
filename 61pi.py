import cv2
import pandas as pd

# Load the key mapping from notes to positions on the mini keyboard
key_mapping = {
    'c': (0, 300),
    'c#': (35, 295),
    'd': (70, 290),
    'd#': (105, 285),
    'e': (140, 280),
    'f': (175, 275),
    'f#': (210, 270),
    'g': (245, 265),
    'g#': (280, 260),
    'a': (315, 255),
    'a#': (350, 250),
    'b': (385, 245),
    'c1': (420, 240),
    'c#1': (455, 235),
    'd1': (490, 230),
    'd#1': (525, 225),
    'e1': (560, 220),
    'f1': (595, 215),
    'f#1': (630, 210),
    'g1': (665, 205),
    'g#1': (700, 200),
    'a1': (735, 195),
    'a#1': (770, 190),
    'b1': (805, 185),
    'c2': (840, 180),
    'c#2': (875, 175),
    'd2': (910, 170),
    'd#2': (945, 165),
    'e2': (980, 160),
    'f2': (1015, 155),
    'f#2': (1050, 150),
    'g2': (1085, 145),
    'g#2': (1120, 140),
    'a2': (1155, 135),
    'a#2': (1190, 130),
    'b2': (1225, 125),
    'c3': (1260, 120)
}

# Load the entries from the csv file
entries = pd.read_csv('/home/saktheeswaran/VIDEOPIA/NEWD.csv')

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
    cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
    
    # Write the frame to the video file
    out.write(frame)
    
    # Display the video feed
    cv2.imshow("keyboard_with_mark", frame)
    
    # Wait for the specified duration before displaying the next entry
    cv2.waitKey(duration)

# Release the video writer and close the window
out.release()
cv2.destroyAllWindows()

