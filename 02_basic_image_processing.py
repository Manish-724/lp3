# Practical 2: Basic Image Processing
# Loading, cropping, resizing, thresholding, contour analysis and blob detection
# Install: pip install opencv-python numpy
import cv2
import numpy as np

# Create a sample image so the program runs without an external image file
image = np.ones((400, 400, 3), dtype=np.uint8) * 255
cv2.rectangle(image, (50, 50), (150, 150), (0, 0, 0), -1)
cv2.circle(image, (300, 100), 40, (50, 50, 50), -1)
cv2.circle(image, (100, 300), 30, (100, 100, 100), -1)

# To load your own image instead, use:
# image = cv2.imread("your_image.jpg")
# if image is None:
#     raise FileNotFoundError("Image not found. Check the file path.")

print("Created/loaded image successfully!")

# 1. Cropping (array slicing: rows first, then columns)
cropped_image = image[0:200, 0:200]

# 2. Resizing
resized_image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_LINEAR)

# 3. Thresholding
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh_image = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# 4. Contour analysis
contours, _ = cv2.findContours(
    thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 3)

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(contour_image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# 5. Blob detection
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 50
params.maxArea = 10000
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(gray)
blob_image = cv2.drawKeypoints(
    image, keypoints, np.array([]), (0, 0, 255),
    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# 6. Display results
cv2.imshow("Original Image", image)
cv2.imshow("Cropped Image", cropped_image)
cv2.imshow("Resized Image", resized_image)
cv2.imshow("Thresholded Image", thresh_image)
cv2.imshow("Contour Analysis", contour_image)
cv2.imshow("Blob Detection", blob_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
