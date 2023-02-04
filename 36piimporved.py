import cv2
import pandas as pd

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
