import cv2

img = cv2.imread(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\man.exp2.jpg")

blur = cv2.GaussianBlur(img, (15, 15), 0)

cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
