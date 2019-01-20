import numpy as np
np.random.seed(1373) 
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils

from keras.utils import multi_gpu_model

batch_size = 1024
nb_classes = 10
nb_epoch = 20


img_rows, img_cols = 28, 28

nb_filters = 32

nb_pool = 2

nb_conv = 3


(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(X_train.shape[0])

X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols,1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols,1)


X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255


print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')


Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

model = Sequential()

model.add(Conv2D(nb_filters, (nb_conv, nb_conv), padding='valid', input_shape=(img_rows, img_cols,1)))
model.add(Activation('relu'))
model.add(Conv2D(nb_filters, (nb_conv, nb_conv)))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes)) 
model.add(Activation('softmax')) 

model = multi_gpu_model(model, gpus=4)

model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=["accuracy"])


history = model.fit(X_train, Y_train, batch_size=batch_size, epochs=nb_epoch, verbose=1, validation_data=(X_test, Y_test))

score = model.evaluate(X_test, Y_test, verbose=0)


model.save('MNIST_CNN.h5')
