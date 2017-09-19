'''Trains a simple deep NN on the MNIST dataset.
Gets to 98.40% test accuracy after 20 epochs
(there is *a lot* of margin for parameter tuning).
2 seconds per epoch on a K520 GPU.
'''
from __future__ import print_function

import argparse
import json
#import os
#import re
#import sys


import time
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from keras import regularizers
from keras.constraints import maxnorm




def setTestandTrain():

    num_classes = 10

    # the data, shuffled and split between train and test sets
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train.reshape(60000, 784)
    x_test = x_test.reshape(10000, 784)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')

    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    return {'test': [x_test,y_test], 'train' : [x_train, y_train]}


def run_MINST_example(dataset, dropout_In, dropout_Hid, momentVal, weightDecay, maxWeight, learningRate, decayRate):

    batch_size = 128
    epochs = 20

    x_test = dataset['test'][0]
    y_test = dataset['test'][1]
    x_train = dataset['train'][0]
    y_train = dataset['train'][1]

    model = Sequential()
    model.add(Dense(512, activation='relu', input_shape=(784,)))
    model.add(Dropout(dropout_In))

    # Hidden layers
    model.add(Dense(512, activation='relu',kernel_regularizer=regularizers.l2(weightDecay), kernel_constraint=maxnorm(maxWeight)))
    model.add(Dropout(dropout_Hid))
    model.add(Dense(512, activation='relu',kernel_regularizer=regularizers.l2(weightDecay), kernel_constraint=maxnorm(maxWeight)))
    model.add(Dropout(dropout_Hid))
    model.add(Dense(512, activation='relu',kernel_regularizer=regularizers.l2(weightDecay), kernel_constraint=maxnorm(maxWeight)))
    model.add(Dropout(dropout_Hid))

    # Softmax
    model.add(Dense(10, activation='softmax'))

    model.summary()

    model.compile(loss='categorical_crossentropy',
                  optimizer=SGD(lr=learningRate, momentum=momentVal, decay=decayRate, nesterov=False),
                  metrics=['accuracy'])

    model.fit(x_train, y_train,
                batch_size=batch_size,
                epochs=epochs,
                verbose=1,
                validation_data=(x_test, y_test))


    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])


    start_time = time.time()
    model.predict(x_test, batch_size=1000, verbose=0)
    computTime = (time.time() - start_time)/1000
    print("--- %s seconds ---" % computTime)

    return {'f': score, 'c': computTime}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Submission scoring helper script')
    parser.add_argument( '-dIn','--dropout_In', required=True,
                        help='path to the ground truth folder')
    parser.add_argument('-dHi', '--dropout_Hid', required=True,
                        help='path to the submission folder')
    parser.add_argument('-mo', '--momentVal', required=True,
                        help='path to the submission folder')
    parser.add_argument('-wD', '--weightDecay', required=True,
                        help='path to the submission folder')
    parser.add_argument('-wM', '--maxWeight', required=True,
                        help='path to the submission folder')
    parser.add_argument('-lr', '--learningRate', required=True,
                        help='path to the submission folder')
    parser.add_argument('-dr', '--decayRate', required=True,
                        help='path to the submission folder')
    args = parser.parse_args()


    dataset = setTestandTrain()
    output = run_MINST_example(dataset, float(args.dropout_In), float(args.dropout_Hid),
                               float(args.momentVal), float(args.weightDecay), float(args.maxWeight), 
                               float(args.learningRate), float(args.decayRate))

    print(json.dumps(output))

    f = open( 'output.json' ,'w')
    f.write(json.dumps(output))
    f.close()
