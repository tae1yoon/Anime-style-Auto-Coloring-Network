import numpy as np
import cv2
from matplotlib import pyplot as plt

black = cv2.imread('black.jpg')
black = cv2.resize(black, dsize = (2000, 1000), interpolation = cv2.INTER_AREA)

img1 = cv2.imread('source.jpg',0) # queryImage
img2 = cv2.imread('target.jpg',0) # trainImage

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 8)
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des1,des2,k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in xrange(len(matches))]

matchnum = 0
# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i]=[1,0]
        matchnum = matchnum + 1

draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 2)

img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
cv2.imwrite('FLANN_result.jpg', img3)

print (np.asarray(kp1).shape)
print (np.asarray(kp2).shape)
print (np.asarray(matchesMask).shape)
print (matchnum)

#plt.imshow(img3,),plt.show()
