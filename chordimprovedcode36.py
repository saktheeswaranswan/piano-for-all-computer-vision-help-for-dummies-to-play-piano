import cv2
import pandas as pd

# Load the key mapping from notes to positions on the mini keyboard
key_mapping = {
    'c': (265,410),
    'c#': (291, 402),
    'd': (340, 396),
    'd#': (366, 390),
  
}

# Load the entries from the csv file
entries = pd.read_csv('/home/saktheeswaran/Desktop/pianoimpo/chordpiano/chordcsv.csv')

# Set the number of frames to skip
skip_frames = 4

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('keyboard_with_mark.mp4', fourcc, 20.0, (640, 480))

# Open a window to display the video feed
cv2.namedWindow("keyboard_with_mark", cv2.WINDOW_NORMAL)

# Start the webcam stream
cap = cv2.VideoCapture(0)

# Loop through each entry in the csv file
for index, row in entries.iterrows():
    # Extract the note, duration, and color information from the current row
    note1 = row['NoteOne'].lower()
    note2 = row['NoteTwo'].lower()
    note3 = row['NoteThree'].lower()
    duration = row['Duration']
    
    # Read a frame from the webcam stream
    for i in range(skip_frames):
        ret, frame = cap.read()
    
    # Draw circles for each of the three notes
    center_x1, center_y1 = key_mapping[note1]
    cv2.circle(frame, (center_x1, center_y1), 5, (255, 0, 0), -1)
    
    center_x2, center_y2 = key_mapping[note2]
    cv2.circle(frame, (center_x2, center_y2), 5, (0, 255, 0), -1)
    
    center_x3, center_y3 = key_mapping[note3]
    cv2.circle(frame, (center_x3, center_y3), 5, (0, 0, 255), -1)
    
    # Write the frame to the video file
    out.write(frame)
    
    # Display the video feed
    cv2.imshow("keyboard_with_mark", frame)
    
    # Wait for the specified duration before displaying the next entry
    cv2.waitKey(duration)

# Release the video writer and close the window
out.release()
cv2.destroyAllWindows()
