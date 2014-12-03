import sys
from cv2 import *
import numpy
import matplotlib.pyplot as plt

#Loading image
im = imread(sys.argv[1])
resized_im = resize(im, ((200, 200)))
resized_original = resized_im.copy()

#Converting to grayscale
resized_img = cvtColor(resized_im, COLOR_BGR2GRAY)

#Sobel derivatives
laplacian = Laplacian(resized_img,CV_64F)
sobelx = Sobel(resized_img,CV_64F,1,0,ksize=5)
sobely = Sobel(resized_img,CV_64F,0,1,ksize=5)
plt.subplot(2,2,1),plt.imshow(resized_img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()
#Histogram equalization
#equalized_img = equalizeHist(resized_img)

#Canny
edges = Canny(resized_img, 100, 200)
plt.subplot(121),plt.imshow(resized_img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
#Thresholding image
retval, thresh_image = threshold(resized_img, 50, 255, THRESH_BINARY_INV)

#dilating
kernel = numpy.ones((3, 3), numpy.uint8)
thresh_image = dilate(thresh_image, kernel, iterations=2)

imwrite("thresh.png", thresh_image)
#Finding contours
contours,hierarchy = findContours(thresh_image, RETR_TREE, CHAIN_APPROX_SIMPLE)

#Drawing contours
#drawContours(resized_im, contours, -1, (0, 255, 0), 1)

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
