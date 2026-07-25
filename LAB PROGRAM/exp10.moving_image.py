import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp9par.jpg")

rows, cols = img.shape[:2]

# Move image: 100 pixels right and 50 pixels down
M = np.float32([[1, 0, 100],
                [0, 1, 50]])

moved = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("Original Image", img)
cv2.imshow("Moved Image", moved)

cv2.waitKey(0)
cv2.destroyAllWindows()
