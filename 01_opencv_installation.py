# Practical 1: OpenCV Installation and Working with Python
# Install in terminal/Colab: pip install opencv-python numpy matplotlib
import cv2
import numpy as np

# Create a blank black canvas (height, width, channels)
canvas = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw shapes (OpenCV uses BGR color order)
cv2.line(canvas, (50, 50), (550, 50), (255, 0, 0), 3)       # Blue line
cv2.rectangle(canvas, (50, 100), (200, 250), (0, 255, 0), -1)  # Green rectangle
cv2.circle(canvas, (400, 175), 60, (0, 0, 255), 4)          # Red circle
cv2.putText(canvas, "OpenCV in Python", (150, 350),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2,
            cv2.LINE_AA)

cv2.imshow("Generated Shape Canvas", canvas)

# Canny edge detection
gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_canvas, 100, 200)
cv2.imshow("Canny Edge Detection", edges)

# Thresholding and contour detection
circle_img = np.zeros((300, 300), dtype=np.uint8)
cv2.circle(circle_img, (150, 150), 80, 255, -1)
contours, hierarchy = cv2.findContours(
    circle_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
print("Number of contours found:", len(contours))

contour_display = cv2.cvtColor(circle_img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_display, contours, -1, (0, 255, 0), 3)
cv2.imshow("Contour Detection", contour_display)
cv2.waitKey(0)
cv2.destroyAllWindows()
