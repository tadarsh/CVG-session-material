import sys
from cv2 import *
import numpy as np
import matplotlib.pyplot as plt

#Loading image
im = imread(sys.argv[1])
#resized_im = resize(im, ((200, 200)))
original_im = im.copy()

#Converting to grayscale
im_gray = cvtColor(im, COLOR_BGR2GRAY)

#Intensity Histogram
plt.hist(im_gray.ravel(),256,[0,256]) 
plt.show()

#Taking Sobel derivatives
laplacian = Laplacian(im_gray,CV_64F)
sobelx = Sobel(im_gray,CV_64F,1,0,ksize=5)
sobely = Sobel(im_gray,CV_64F,0,1,ksize=5)

plt.imshow(sobely, cmap='gray')
plt.show()


#Finding gradient direction at each point
grad_image = np.arctan(sobely.astype(float) / (sobelx.astype(float) + 0.0001))

plt.hist(grad_image.ravel(), 100, [-1.58, 1.58])
hist,bins = np.histogram(grad_image.ravel(),100,[-1.58,1.58])
plt.show()


#Finding the max gradient
bin_max = bins[np.argmax(hist)]
rows, cols = im_gray.shape

#Need to rotate it by bin_max radians
rot_mat = getRotationMatrix2D((cols/2, rows/2), bin_max * 180 / np.pi, 1)
dst = warpAffine(im_gray, rot_mat, (cols, rows))
imwrite("dst.png", dst)
