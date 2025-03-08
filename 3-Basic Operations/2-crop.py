import cv2

# read image
img = cv2.imread('aditya.png')
print(img.shape)

cv2.imshow("image", img)
cropped_img = img[90:450, 100:425]
cv2.imshow("cropped image", cropped_img)
cv2.waitKey(0)
