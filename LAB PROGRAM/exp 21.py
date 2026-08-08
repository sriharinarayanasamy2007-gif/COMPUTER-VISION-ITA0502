import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp12.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Laplacian mask with diagonal neighbors
mask = np.array([[1, 1, 1],
                 [1, -8, 1],
                 [1, 1, 1]], dtype=np.float32)

laplacian = cv2.filter2D(gray, -1, mask)

# Sharpening: Original - Laplacian
sharpened = cv2.subtract(gray, laplacian)

cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
