import os

import cv2

video_path = "sample_video.mp4"

# read Video
video = cv2.VideoCapture(video_path)

# visualize video
ret = True
while ret:
    ret, frame = video.read()
    if ret:
        cv2.imshow("frame", frame)
        cv2.waitKey(40)

video.release()
cv2.destroyAllWindows()

