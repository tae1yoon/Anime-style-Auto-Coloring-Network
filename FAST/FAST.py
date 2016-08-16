import numpy as np
import cv2

# Load the image
img = cv2.imread('source.jpg')

# Convert it to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, dsize = (112, 112), interpolation = cv2.INTER_AREA)

# Detect the FAST key points
fast = cv2.FastFeatureDetector_create(threshold=25)
keyPoints = fast.detect(gray, None)

# Print some information
print("Threshold: ", fast.getThreshold())
print("Total Keypoints with nonmaxSuppression: ", len(keyPoints))

feature_point = [[0,0] for i in xrange(len(keyPoints))]

for i, keyPoint in enumerate(keyPoints):
    x = int(keyPoint.pt[0])
    y = int(keyPoint.pt[1])
    feature_point[i] = [x, y]

np.savetxt("FAST_source.csv", np.asarray(feature_point), delimiter = ",")

# Paint the key points over the original image
result = cv2.drawKeypoints(gray, keyPoints, None, flags=0)

# Display the results
#cv2.imshow('Key points', result)
#cv2.waitKey(0)
cv2.imwrite('FAST_source.jpg', result)
cv2.destroyAllWindows()

# Load the image
img = cv2.imread('target.jpg')

# Convert it to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, dsize = (112, 112), interpolation = cv2.INTER_AREA)

# Detect the FAST key points
fast = cv2.FastFeatureDetector_create(threshold=25)
keyPoints = fast.detect(gray, None)

# Print some information
print("Threshold: ", fast.getThreshold())
print("Total Keypoints with nonmaxSuppression: ", len(keyPoints))

feature_point = [[0,0] for i in xrange(len(keyPoints))]

for i, keyPoint in enumerate(keyPoints):
    x = int(keyPoint.pt[0])
    y = int(keyPoint.pt[1])
    feature_point[i] = [x, y]

np.savetxt("FAST_target.csv", np.asarray(feature_point), delimiter = ",")

result = cv2.drawKeypoints(gray, keyPoints, None, flags=0)

# Display the results
#cv2.imshow('Key points', result)
#cv2.waitKey(0)
cv2.imwrite('FAST_target.jpg', result)
cv2.destroyAllWindows()
