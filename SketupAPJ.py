import cv2

# Load the image
image = cv2.imread("apj.jpg")   # Put your APJ Abdul Kalam image in the same folder as your code

# Convert to gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_image = cv2.bitwise_not(gray_image)

# Blur the inverted image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# Invert the blurred image
inverted_blur = cv2.bitwise_not(blurred)

# Create pencil sketch
sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

# Show output
cv2.imshow("Original", image)
cv2.imshow("Pencil Sketch of APJ", sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()


