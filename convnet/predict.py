from __future__ import division, print_function, absolute_import
import operator
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
from tflearn.optimizers import Adam
from tflearn.data_augmentation import ImageAugmentation

import numpy as np
from numpy import genfromtxt

X1 = genfromtxt('input_matrix1.csv', delimiter=',')
X2 = genfromtxt('input_matrix2.csv', delimiter=',')
X1 = X1.reshape([-1, 29, 29, 1])
X2 = X2.reshape([-1, 29, 29, 1])
X = np.concatenate((X1, X2))

X1_canny = genfromtxt('input_matrix1(canny).csv', delimiter=',')
X2_canny = genfromtxt('input_matrix2(canny).csv', delimiter=',')
X1_canny = X1_canny.reshape([-1, 29, 29, 1])
X2_canny = X2_canny.reshape([-1, 29, 29, 1])
X_canny = np.concatenate((X1_canny, X2_canny))

X1_FAST = genfromtxt('input_matrix1(FAST).csv', delimiter=',')
X2_FAST = genfromtxt('input_matrix2(FAST).csv', delimiter=',')
X1_FAST = X1_FAST.reshape([-1, 29, 29, 1])
X2_FAST = X2_FAST.reshape([-1, 29, 29, 1])
X_FAST = np.concatenate((X1_FAST, X2_FAST))

X = np.concatenate((X, X_canny), axis=3)
X = np.concatenate((X, X_FAST), axis=3)

# Real-time data augmentation
img_aug = ImageAugmentation()
img_aug.add_random_flip_leftright()
img_aug.add_random_rotation(max_angle=10.)
img_aug.add_random_blur(sigma_max=1.5)

# Building convolutional network
network = input_data(shape=[None, 29, 29, 3], name='input', data_augmentation=img_aug)

network = conv_2d(network, 16, 3, activation='relu')
network = max_pool_2d(network, 2)
network = local_response_normalization(network)
network = conv_2d(network, 32, 3, activation='relu')
network = max_pool_2d(network, 2)
network = local_response_normalization(network)
network = conv_2d(network, 64, 3, activation='relu')
network = max_pool_2d(network, 2)
network = local_response_normalization(network)
network = conv_2d(network, 128, 3, activation='relu')
network = max_pool_2d(network, 2)
network = local_response_normalization(network)

network = fully_connected(network, 256, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 256, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 24, activation='softmax')
adam = Adam(learning_rate=0.001)
network = regression(network, optimizer=adam,
                     loss='categorical_crossentropy', name='target')

# Model Loading
model = tflearn.DNN(network)
model.load('convnet.tflearn')

Y = model.predict(X)
i = 0
result = []
while i < X.shape[0]:
    index, value = max(enumerate(Y[i]), key = operator.itemgetter(1))
    i = i + 1
    result.append(index)

Y = np.matrix(result)
Y = Y.reshape([12544, 1])

np.savetxt("predict_result.csv", Y, delimiter = ",")
