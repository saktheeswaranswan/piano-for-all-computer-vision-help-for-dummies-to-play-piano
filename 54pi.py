import cv2
import pandas as pd

# Load the key mapping from notes to positions on the mini keyboard
key_mapping = {
    'c': (430, 360),
    'c#': (465, 355),
    'd': (500, 350),
    'd#': (535, 345),
    'e': (570, 340),
    'f': (605, 335),
    'f#': (640, 330),
    'g': (675, 325),
    'g#': (710, 320),
    'a': (745, 315),
    'a#': (780, 310),
    'b': (815, 305),
    'c1': (850, 300),
    'c#1': (885, 295),
    'd1': (920, 290),
    'd#1': (955, 285),
    'e1': (990, 280),
    'f1': (1025, 275),
    'f#1': (1060, 270),
    'g1': (1095, 265),
    'g#1': (1130, 260),
    'a1': (1165, 255),
    'a#1': (1200, 250),
    'b1': (1235, 245),
    'c2': (1270, 240),
    'c#2': (1305, 235),
    'd2': (1340, 230),
    'd#2': (1375, 225),
    'e2': (1410, 220),
    'f2': (1445, 215),
    'f#2': (1480, 210),
    'g2': (1515, 205),
    'g#2': (1550, 200),
    'a2': (1585, 195),
    'a#2': (1620, 190),
    'b2': (1655, 185),
    'c3': (1690, 180),
    'c#3': (1725, 175),
    'd3': (1760, 170),
    'd#3': (1795, 165),
    'e3': (1830, 160),
    'f3': (1865, 155),
    'f#3': (1900, 150),
    'g3': (1935, 145),
    'g#3': (1970, 140),
    'a3': (2005, 135),
    'a#3': (2040, 130),
    'b3': (2075, 125),
    'c4': (2110, 120),
    'c#4': (2145, 115),
    'd4': (2180, 110),
    'd#4': (2215, 105),
    'e4': (2250, 100),
    'f4': (2285, 95),
    'f#4': (2320, 90),
    'g4': (2355, 85),
    'g#4': (2390, 80),
    'a4': (2425, 75),
    'a#4': (2460, 70)
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

