import cv2
import random

img = cv2.imread('./assets/coffee.jpg', -1)
print(img.shape)

coffee = img[2000:2500, 600:900]

cv2.imshow('Coffee', coffee)


# cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()