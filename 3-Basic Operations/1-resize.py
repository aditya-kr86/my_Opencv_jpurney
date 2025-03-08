#resizing
import cv2
img = cv2.imread('aditya.png')
resized_img = cv2.resize(img, (300, 300))

print(img.shape)
print(resized_img.shape)

cv2.imshow("frame", img)
cv2.imshow("resized image", resized_img)
cv2.waitKey(0)

