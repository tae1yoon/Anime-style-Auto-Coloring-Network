import numpy as np
import cv2

# Load the image
img = cv2.imread('source.jpg')
gray = cv2.resize(img, dsize = (112, 112), interpolation = cv2.INTER_AREA)
cv2.imwrite("source4knn.jpg", gray)

# Load the image
img = cv2.imread('source.jpg')
# Convert it to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, dsize = (112, 112), interpolation = cv2.INTER_AREA)
cv2.imwrite("basic_source.jpg", gray)

img = cv2.imread('target.jpg')
# Convert it to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, dsize = (112, 112), interpolation = cv2.INTER_AREA)
cv2.imwrite("basic_target.jpg", gray)

# Convert it to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, dsize = (224, 224), interpolation = cv2.INTER_AREA)
cv2.imwrite("basic_target(224).jpg", gray)
