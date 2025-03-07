import cv2

#read image
img =cv2.imread('aditya.png')

#write image
cv2.imwrite('aditya_output.jpg', img)

#visualize image
cv2.imshow('aditya photo',img)
cv2.waitKey(0)
