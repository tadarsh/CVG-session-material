import sys
import cv2

def img2vector(img):
    feature = img.reshape(1, 28 * 28)
    return feature

images_lines = open(sys.argv[1], 'r').readlines()
labels_lines = open(sys.argv[2], 'r').readlines()

features = numpy.zeros((60000, 28*28))

for i in xrange(len(images_lines)):
    feature = img2vector(cv2.imread(images_lines[i].rstrip(), 0))
    features[i, :] = feature

numpy.savetxt("out.txt", features, delimiter=',')
    


