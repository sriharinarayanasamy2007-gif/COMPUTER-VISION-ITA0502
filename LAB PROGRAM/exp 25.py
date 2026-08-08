import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp12.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel gradient masks
gx = np.array([[-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]], dtype=np.float32)

gy = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]], dtype=np.float32)

grad_x = cv2.filter2D(gray, cv2.CV_32F, gx)
grad_y = cv2.filter2D(gray, cv2.CV_32F, gy)

gradient = cv2.magnitude(grad_x, grad_y)
gradient = cv2.convertScaleAbs(gradient)

# Sharpen using gradient mask
sharpened = cv2.add(gray, gradient)

cv2.imshow("Original Image", img)
cv2.imshow("Gradient Mask Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
