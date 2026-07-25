import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp12.jpg")

rows, cols = img.shape[:2]

# Source points
src = np.float32([[50, 50],
                  [250, 50],
                  [50, 250],
                  [250, 250]])

# Destination points
dst = np.float32([[20, 100],
                  [280, 50],
                  [80, 280],
                  [300, 250]])

# Direct Linear Transformation (DLT) using Homography
H, _ = cv2.findHomography(src, dst, method=0)

# Apply transformation
output = cv2.warpPerspective(img, H, (cols, rows))

cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformation", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
