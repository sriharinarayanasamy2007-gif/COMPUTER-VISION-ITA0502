import cv2

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp12.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create blurred image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Unsharp mask = Original - Blurred
unsharp_mask = cv2.subtract(gray, blur)

# Sharpened image = Original + Unsharp Mask
sharpened = cv2.add(gray, unsharp_mask)

cv2.imshow("Original Image", img)
cv2.imshow("Unsharp Mask", unsharp_mask)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
