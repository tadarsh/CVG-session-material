import sys
import cv2
import numpy
from sklearn.svm import SVC
def img2vector(img):
    feature = img.reshape(1, 28 * 28)
    return feature

# Loading the dataset and extracting features
images_lines = open(sys.argv[1], 'r').readlines()
trainData = numpy.zeros((60000, 28*28)).astype("uint8")
trainLabels = numpy.loadtxt(sys.argv[2], delimiter=',')

for i in xrange(len(images_lines)):
    if i % 1000 == 0:
        print i, "done"
    feature = img2vector(cv2.imread(images_lines[i].rstrip(), 0))
    trainData[i, :] = feature
print "Loading done"

# Training a classifier
print "Training an SVM"
classifier = SVC(kernel = 'linear', verbose = True)
classifier.fit(trainData, trainLabels)
print "Done training"

print "Predicting on the training set"
predicted =  classifier.predict(trainData)

