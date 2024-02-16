import numpy as np
import h5py
    
def load_dataset():
    train_dataset = h5py.File('datasets/train.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])
    train_set_y_orig = np.array(train_dataset["train_set_y"][:])

    test_dataset = h5py.File('datasets/test.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) 

    classes = np.array(test_dataset["list_classes"][:]) 
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    train_set_x = flatten(train_set_x_orig)
    test_set_x = flatten(test_set_x_orig)

    num_px = train_set_x_orig.shape[1]

    return train_set_x, train_set_y_orig, test_set_x, test_set_y_orig, classes, num_px

def flatten(set_x_orig):
    return set_x_orig.reshape(set_x_orig.shape[0], -1).T / 255
