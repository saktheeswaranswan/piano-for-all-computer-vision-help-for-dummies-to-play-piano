import csv
import numpy as np
import  cv2

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Define the mouse callback function to get the coordinates
def get_coords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        with open('coordinates.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([x, y])
        print(f'Coordinates saved: {x}, {y}')

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



#In this code, the cv2.VideoCapture object is used to capture the video from the default camera (camera index 0). The cv2.setMouseCallback function is used to set the mouse callback function to get_coords which will be called whenever a left double-click event occurs. In the get_coords function, the coordinates are saved in a csv file named coordinates.csv using the csv module. The video loop runs until the q key is pressed and displays the video frames using the cv2.imshow function. The video capture object is released and all windows are closed when the loop is broken.

#Note: This code is just a sample and may need some modifications to fit your specific use case. You may also need to install the OpenCV library by running pip install opencv-python.
