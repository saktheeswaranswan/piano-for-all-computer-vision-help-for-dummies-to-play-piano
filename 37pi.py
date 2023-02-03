import cv2
import pandas as pd

# Load the key mapping from notes to positions on the mini keyboard
key_mapping = {
    'c': (350, 360),
    'c#': (385, 355),
    'd': (420, 350),
    'd#': (455, 345),
    'e': (490, 340),
    'f': (525, 335),
    'f#': (560, 330),
    'g': (595, 325),
    'g#': (630, 320),
    'a': (665, 315),
    'a#': (700, 310),
    'b': (735, 305),
    'c1': (770, 300),
    'c#1': (805, 295),
    'd1': (840, 290),
    'd#1': (875, 285),
    'e1': (910, 280),
    'f1': (945, 275),
    'f#1': (980, 270),
    'g1': (1015, 265),
    'g#1': (1050, 260),
    'a1': (1085, 255),
    'a#1': (1120, 250),
    'b1': (1155, 245)
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

