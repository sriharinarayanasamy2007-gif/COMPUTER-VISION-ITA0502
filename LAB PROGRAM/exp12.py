import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp12.jpg")

rows, cols = img.shape[:2]

# Four source points
pts1 = np.float32([[50, 50],
                   [200, 50],
                   [50, 200],
                   [200, 200]])

# Four destination points
pts2 = np.float32([[10, 100],
                   [200, 50],
                   [100, 250],
                   [220, 220]])

# Perspective Transformation Matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply Perspective Transformation
perspective = cv2.warpPerspective(img, M, (cols, rows))

cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformed Image", perspective)

cv2.waitKey(0)
cv2.destroyAllWindows()
