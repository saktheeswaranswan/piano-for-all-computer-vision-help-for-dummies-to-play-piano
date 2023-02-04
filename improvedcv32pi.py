import cv2
import pandas as pd

key_mapping = {
    'c': (181,224),
    'c#': (189, 209),
    'd': (272, 245),
    'd#': (280,260),
    'e': (117, 254),
    'f': (365, 292),
    'f#': (361, 398),
    'g': (462, 389),
    'g#': (492, 395),
    'a': (110, 401),
    'a#': (435, 310),
    'b': (470, 305),
}

entries = pd.read_csv('/home/saktheeswaran/Desktop/pianoimpo/flute.csv')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('keyboard_with_mark.mp4', fourcc, 20.0, (640, 480))

cv2.namedWindow("keyboard_with_mark", cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(0)

#Set the number of frames to skip
skip_frames = 2

for index, row in entries.iterrows():
    note = row['Note'].lower()
    center_x, center_y = key_mapping[note]
    duration = row['Duration']
    ret, frame = cap.read()
    cv2.circle(frame, (center_x, center_y), 15, (0, 0, 255), -1)
    out.write(frame)
    cv2.imshow("keyboard_with_mark", frame)
    cv2.waitKey(duration//skip_frames)
    for i in range(skip_frames-1):
        ret, frame = cap.read()
        out.write(frame)

out.release()
cv2.destroyAllWindows()
