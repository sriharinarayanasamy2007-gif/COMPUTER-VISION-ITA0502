import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp12.jpg")

rows, cols = img.shape[:2]

# Source points
pts1 = np.float32([[50, 50],
                   [250, 50],
                   [50, 250],
                   [250, 250]])

# Destination points
pts2 = np.float32([[10, 100],
                   [300, 50],
                   [100, 300],
                   [300, 250]])

# Compute Homography Matrix
H, status = cv2.findHomography(pts1, pts2)

# Apply Homography Transformation
output = cv2.warpPerspective(img, H, (cols, rows))

cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformation", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
