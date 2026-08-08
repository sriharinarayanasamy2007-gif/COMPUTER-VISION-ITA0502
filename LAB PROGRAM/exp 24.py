import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp12.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

A = 2

mask = np.array([[0, -1, 0],
                 [-1, A + 4, -1],
                 [0, -1, 0]], dtype=np.float32)

sharpened = cv2.filter2D(gray, -1, mask)

cv2.imshow("Original Image", img)
cv2.imshow("High Boost Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
