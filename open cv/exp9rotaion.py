import cv2

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp9par.jpg")

# Clockwise Rotation (90°)
clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Counter Clockwise Rotation (90°)
counter = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original Image", img)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter)

cv2.waitKey(0)
cv2.destroyAllWindows()
