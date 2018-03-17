"""
레퍼런스하려는 사이트입니다.
http://kr.mathworks.com/help/vision/examples/automatically-detect-and-recognize-text-in-natural-images.html?s_tid=gn_loc_drop

하단의 코드를 제공한 사이트입니다.
https://stackoverflow.com/questions/34398188/trying-to-plot-opencvs-mser-regions-using-matplotlib
"""
from PIL import Image
import time
import cv2
import os

start_time = time.time()

## Read image and change the color space
imgname = "test_2.jpg"
ig = Image.open(imgname)
img = cv2.imread(imgname)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Get mser, and set parameters
mser = cv2.MSER_create()
mser.setMinArea(1)
mser.setMaxArea(10000)

## Do mser detection, get the coodinates and bboxes
coordinates, bboxes = mser.detectRegions(gray)

rect = []

## Filter the coordinates
vis = img.copy()
viss = img.copy()
for coord in coordinates:
    bbox = cv2.boundingRect(coord)
    x, y, w, h = bbox
    if w < 4 and h < 4:
        continue
    rect.append([x, y, (x + w), (y + h)])
    cv2.rectangle(vis, (x, y), (x + w, y + h), (3, 255, 4), 1)

# cv2.imshow("ok1", vis)
#
# cv2.waitKey(0)

print(len(rect))
temp = 0
rect.sort()

while 1:
    lang = len(rect)
    cost = 1
    if temp == len(rect):
        print("finish")
        break
    else:
        temp = lang
        print(lang)
        print(temp)
        for con in range(0, len(rect) - 1):
            print("new-----------------------------------")
            if con >= (lang - cost):
                break
            for i in range(0, lang):
                print("i : ", i)
                print("cost : ", cost)
                if i >= (lang - cost):
                    break
                elif i == con:
                    continue
                elif rect[con][0] <= rect[i][0] <= rect[con][2] or rect[con][0] <= rect[i][2] <= rect[con][2]:
                    if rect[con][1] <= rect[i][1] <= rect[con][3] or rect[con][1] <= rect[i][3] <= rect[con][3]:
                        rect[con][0] = min(rect[con][0], rect[con][2], rect[i][0], rect[i][2])
                        rect[con][2] = max(rect[con][0], rect[con][2], rect[i][0], rect[i][2])
                        rect[con][1] = min(rect[con][1], rect[con][3], rect[i][1], rect[i][3])
                        rect[con][3] = max(rect[con][1], rect[con][3], rect[i][1], rect[i][3])
                        del rect[i]
                        cost = cost + 1
                else:
                    continue

path = os.path.dirname( os.path.abspath( __file__ ) )+"\image\\"

for a in range(0, len(rect)):
    x = rect[a][0]
    y = rect[a][1]
    w = rect[a][2]
    h = rect[a][3]
    area = (x, y, w, h)
    cropped_img = ig.crop(area)
    cropped_img.save(path+"num"+str(a)+".jpg")
    cv2.rectangle(viss, (x, y), (w, h), (3, 255, 4), 1)

print(len(rect))
print(rect)


print("--- %s seconds ---" % (time.time() - start_time))

cv2.imshow("ok2", viss)

cv2.waitKey(0)
