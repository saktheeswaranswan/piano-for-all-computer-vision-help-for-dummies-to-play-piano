import cv2
import pandas as pd

# Load the key mapping from notes to positions on the mini keyboard
key_mapping =  {
    'c': (340, 360),
    'c#': (375, 355),
    'd': (410, 350),
    'd#': (445, 345),
    'e': (480, 340),
    'f': (515, 335),
    'f#': (550, 330),
    'g': (585, 325),
    'g#': (620, 320),
    'a': (655, 315),
    'a#': (690, 310),
    'b': (725, 305),
    'c1': (760, 300),
    'c#1': (795, 295),
    'd1': (830, 290),
    'd#1': (865, 285),
    'e1': (900, 280),
    'f1': (935, 275),
    'f#1': (970, 270),
    'g1': (1005, 265),
    'g#1': (1040, 260),
    'a1': (1075, 255),
    'a#1': (1110, 250),
    'b1': (1145, 245),
    'c2': (1180, 240)
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

