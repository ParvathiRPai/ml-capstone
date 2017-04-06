# CIFAR-10 and SVM Image Recognition

## Dependencies

The following packages are nedeed to run this project:

- keras, tensorflow, scikit-learn, cv2, numpy

## Training the classifiers
There are 2 classifiers in this project. The main one is a CNN classifier developed with Keras. There is also a SVM classifier built with Scikit-learn that is used to compare results for benchmark reasons

### Keras CNN classifier
The Keras classifier is declared in the [trainning-cnn-larger.py](./trainning-cnn-larger.py) file. To execute the classifier, simply run:

```shell
python trainning-cnn-larger.py
```
The trainning process can take a very long time to complete. You can download the trained classifier [here](https://s3.amazonaws.com/ml-capstone/classifiers/larger-cnn.h5) (20mb) and put it in the 'classifier' folder if you don't have the time or computing power to execute the real thing ;-)

### SVM classifier
The SVM classifier is declared in the [trainning-svm.py](./trainning-svm.py) file. To execute the classifier, simply run:

```shell
python trainning-svm.py
```
As was the case with the CNN classifier. Trainning the SVM model is really time consuming. You can download a ready-to-use classifier [here](https://s3.amazonaws.com/ml-capstone/classifiers/svn-classifier.pkl) (400mb), and put it in the 'classifier' folder as well.

## Predictions
There are iPython Notebooks that can be used to run predictions for the CNN and SVM classifiers. They are:

- [Prediction CNN.ipynb](./Prediction CNN.ipynb)
- [Prediction SVM.ipynb](./Prediction SVM.ipynb)

These notebooks make use of some sample images that are not part of the CIFAR dataset. There are 30 images, 3 for each of the 10 classes that can be downloaded [here](https://s3.amazonaws.com/ml-capstone/images/all.zip). After downloading, unzip the file, and place the images in a folder called 'images'

The images were gathered on the internet, and have various dimensions and sizes, so they are more similar to images that user would submit to the application in a real-world scenario.
