"""
https://stackoverflow.com/questions/40078625/opencv-mser-detect-text-areas-python
"""
import cv2
import numpy as np

#Create MSER object
mser = cv2.MSER_create()

#Your image path i-e receipt path
img = cv2.imread('test_2.jpg')

#Convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mser.setMinArea(1)
mser.setMaxArea(10000)

vis = img.copy()

#detect regions in gray scale image
regions, _ = mser.detectRegions(gray)

#save hull
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]

cv2.polylines(vis, hulls, 1, (0, 255, 0))

cv2.imshow('img', vis)

cv2.waitKey(0)

mask = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)

for contour in hulls:

    cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)

#this is used to find only text regions, remaining are ignored
test = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("test shot", test)

cv2.waitKey(0)

cv2.imwrite("testshot.jpg", test)