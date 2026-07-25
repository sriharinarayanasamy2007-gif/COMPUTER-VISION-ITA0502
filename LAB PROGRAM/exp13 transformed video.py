import cv2
import numpy as np

cap = cv2.VideoCapture(r"C:\Users\Srihari\OneDrive\Desktop\Downloads\exp13.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rows, cols = frame.shape[:2]

    # Source points
    pts1 = np.float32([[50, 50],
                       [300, 50],
                       [50, 300],
                       [300, 300]])

    # Destination points
    pts2 = np.float32([[10, 100],
                       [300, 50],
                       [100, 300],
                       [300, 250]])

    # Perspective Transformation Matrix
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply Perspective Transformation
    output = cv2.warpPerspective(frame, M, (cols, rows))

    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", output)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
