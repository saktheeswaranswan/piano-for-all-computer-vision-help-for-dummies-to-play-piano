import csv
import numpy as np
import cv2

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Define the mouse callback function to get the coordinates
def get_coords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        with open('coordinates.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([x, y])
        print(f'Coordinates saved: {x}, {y}')
        # Draw a red dot at the point where double-click happened
        cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)

# Create a window to display the video
cv2.namedWindow("Video")

# Set the mouse callback to get_coords function
cv2.setMouseCallback("Video", get_coords)

# Start the video loop
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow("Video", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()

