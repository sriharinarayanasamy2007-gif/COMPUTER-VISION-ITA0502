import cv2

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp12.jpg")

# Crop image
crop = img[50:250, 50:250]

# Copy crop
copy = crop.copy()

# Paste into original image
img[300:500, 300:500] = copy

cv2.imshow("Original and Pasted Image", img)
cv2.imshow("Cropped Image", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()
