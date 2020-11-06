## Test file for drum transcribe

import numpy as np
import tensorflow.keras as keras
from keras.models import Model, Sequential
from keras.layers import Conv2D, MaxPool2D, Dense

import librosa
from librosa.core import load, amplitude_to_db

def main():
    
    input_shape = () #GET INPUT SHAPE 
    
    model = Sequential()
    model.add(Conv2D(10, (7, 3), input_shape=input_shape, activation='relu'))
    model.add(MaxPool2D((1, 3)))
    model.add(Conv2D(20, (3, 3), activation='relu'))
    model.add(MaxPool2D((1, 3)))
    model.add(Dense(256, activation='softmax'))

if __name__ == "__main__" : 
    main()