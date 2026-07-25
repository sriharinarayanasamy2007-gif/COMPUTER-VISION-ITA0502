import cv2

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp8.los.jpg")

# Bigger Image (2x)
bigger = cv2.resize(img, None, fx=2, fy=2)

# Smaller Image (0.5x)
smaller = cv2.resize(img, None, fx=0.5, fy=0.5)

cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()
