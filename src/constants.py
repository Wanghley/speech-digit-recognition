import os
import numpy as np
from enum import Enum

TRAIN_FILE = os.path.join('../data/Train_Arabic_Digit.txt')
TEST_FILE = os.path.join('../data/Test_Arabic_Digit.txt')
DF_FILE = os.path.join('../data/dataframe.csv')

NUM_MFCC = 13
ALL_COEFFS = np.arange(0, NUM_MFCC, 1)

NUM_DIGITS = 10