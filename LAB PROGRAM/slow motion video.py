import cv2

cap = cv2.VideoCapture(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\car exp6.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Slow Motion", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
