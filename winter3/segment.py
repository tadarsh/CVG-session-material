import sys
from cv2 import *
import numpy

#Loading image
im = imread(sys.argv[1])
resized_im = resize(im, ((200, 200)))
resized_original = resized_im.copy()

#Converting to grayscale
resized_img = cvtColor(resized_im, COLOR_BGR2GRAY)

#Histogram equalization
#equalized_img = equalizeHist(resized_img)

#Thresholding image
retval, thresh_image = threshold(resized_img, 50, 255, THRESH_BINARY_INV)

#dilating
kernel = numpy.ones((3, 3), numpy.uint8)
thresh_image = dilate(thresh_image, kernel, iterations=2)

imwrite("thresh.png", thresh_image)
#Finding contours
contours,hierarchy = findContours(thresh_image, RETR_TREE, CHAIN_APPROX_SIMPLE)

#Drawing contours
drawContours(resized_im, contours, -1, (0, 255, 0), 3)

#Eliminating small contours
new_contours = []
index = 0
for contour in contours:
    if arcLength(contour, True) > 50:
        
        #Adding it to a new list
        new_contours.append(contour)
        
        #Drawing a bouding rect for each contour
        x, y, w, h = boundingRect(contour)
        rectangle(resized_im,(x,y),(x+w,y+h),(255, 255,0),2)
        
        img = resized_original[y: y + h, x: x + w]
        imwrite("cropped" + str(index) + ".png", img)
        index = index + 1;

imwrite("resized_img.png", resized_im)
