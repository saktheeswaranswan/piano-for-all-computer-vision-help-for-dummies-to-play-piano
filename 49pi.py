import cv2
import pandas as pd

# Load the key mapping from notes to positions on the mini keyboard
key_mapping =  {
    'c': (200, 300),
    'c#': (235, 295),
    'd': (270, 290),
    'd#': (305, 285),
    'e': (340, 280),
    'f': (375, 275),
    'f#': (410, 270),
    'g': (445, 265),
    'g#': (480, 260),
    'a': (515, 255),
    'a#': (550, 250),
    'b': (585, 245),
    'c1': (620, 240),
    'c#1': (655, 235),
    'd1': (690, 230),
    'd#1': (725, 225),
    'e1': (760, 220),
    'f1': (795, 215),
    'f#1': (830, 210),
    'g1': (865, 205),
    'g#1': (900, 200),
    'a1': (935, 195),
    'a#1': (970, 190),
    'b1': (1005, 185),
    'c2': (1040, 180),
    'c#2': (1075, 175),
    'd2': (1110, 170),
    'd#2': (1145, 165),
    'e2': (1180, 160),
    'f2': (1215, 155),
    'f#2': (1250, 150),
    'g2': (1285, 145),
    'g#2': (1320, 140),
    'a2': (1355, 135),
    'a#2': (1390, 130),
    'b2': (1425, 125),
    'c3': (1460, 120),
    'c#3': (1495, 115),
    'd3': (1530, 110),
    'd#3': (1565, 105),
    'e3': (1600, 100),
    'f3': (1635, 95),
    'f#3': (1670, 90),
    'g3': (1705, 85),
    'g#3': (1740, 80),
    'a3': (1775, 75),
    'a#3': (1810, 70),
    'b3': (1845, 65),
    'c4': (1880, 60),
    'c#4': (1915, 55),
    'd4': (1950, 50),
    'd#4': (1985, 45),
    'e4': (2020, 40),
    'f4': (2055, 35),
    'f#4': (2090, 30),
    'g4': (2125, 25),
    'g#4': (2160, 20),
    'a4': (2195, 15),
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

