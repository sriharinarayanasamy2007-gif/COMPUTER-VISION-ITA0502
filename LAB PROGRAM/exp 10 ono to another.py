import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp10.nature.jpg")

rows, cols = img.shape[:2]

# Translation matrix (move 100 pixels right and 50 pixels down)
M = np.float32([[1, 0, 100],
                [0, 1, 50]])

translated = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()
