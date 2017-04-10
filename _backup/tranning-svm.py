
## Extract Dataset
from keras.datasets import cifar10
from keras import backend as K
K.set_image_data_format('channels_last')

(X_train, y_train), (X_test, y_test) = cifar10.load_data()


## Convert images to grayscale

import cv2

X_train = map(lambda x: cv2.cvtColor(x, cv2.COLOR_BGRA2GRAY), X_train)
X_test = map(lambda x: cv2.cvtColor(x, cv2.COLOR_BGRA2GRAY), X_test)


## Fit

from sklearn import svm
import numpy

clf = svm.SVC(gamma=0.001, C=100.)

X_train = numpy.array(X_train)
X_train = numpy.array(X_train).reshape((X_train.shape[0], -1), order='F')

y_train = numpy.array(y_train).flatten()

clf.fit(X_train, y_train)

## Save classifier to disk

from sklearn.externals import joblib
joblib.dump(clf, 'clasifiers/svn-classifier.pkl')
