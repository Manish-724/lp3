# Practical 3: Image Annotation
# Drawing lines, text, circles, rectangles and ellipses
# Install: pip install opencv-python numpy
import cv2
import numpy as np

# Create a blank white canvas (height, width, channels)
canvas = np.ones((400, 500, 3), dtype=np.uint8) * 255

# 1. Draw a blue line
cv2.line(canvas, (50, 40), (450, 40), (255, 0, 0), 3)

# 2. Draw rectangles: outlined and filled
cv2.rectangle(canvas, (50, 80), (200, 180), (0, 255, 0), 2)
cv2.rectangle(canvas, (250, 80), (400, 180), (0, 255, 0), -1)

# 3. Draw a red circle
cv2.circle(canvas, (125, 270), 45, (0, 0, 255), 3)

# 4. Draw a purple ellipse
cv2.ellipse(canvas, (325, 270), (60, 30), 45, 0, 360, (255, 0, 255), 2)

# 5. Add text
cv2.putText(canvas, "OpenCV Image Annotation", (90, 380),
            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 0), 2, cv2.LINE_AA)

cv2.imshow("Image Annotation", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
