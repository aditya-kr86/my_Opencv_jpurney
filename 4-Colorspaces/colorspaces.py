import os
import cv2

img = cv2.imread(os.path.join('..', "aditya.png"))

# covert colors paces
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
image_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("image", img)
cv2.imshow("image_rgb", image_rgb)
cv2.imshow("image_gray", image_gray)
cv2.imshow("image_hsv", image_hsv)
cv2.waitKey(0)
