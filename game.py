import statistics 
import time
import copy
import pickle
import random
import numpy 
import sympy
import scipy
from scipy.integrate import quad

class integralMap:
    def __init__(self, numOfQuestions):
        self.__divisions = [] # list of points on the map
        self.__integralSliceLength = 1/numOfQuestions #Length of each sub interval
        print("test")
        f = lambda x: -numpy.log(x) # Function which detrmines the distrobution of weights
        for i in range(0, numOfQuestions-1):
            sliceProgress = self.__integralSliceLength * (i+1) 
            self.__divisions.append(quad(f, 0, sliceProgress)[0])

    def pickRandomIndex(self):
        index = 0
        value = random.uniform(0, 1)
        for x in self.__divisions:
            if value < x:
                return index
            index = index + 1
        return index

    def __function(x):
        return numpy.log(x) 
hype = integralMap(100)
ls = []
for x in range(0, 100):
    ls.append(0)
for x in range(0, 100000):
    index = hype.pickRandomIndex()
    ls[index] = ls[index] + 1

for x in range(0, 100):
    print(ls[x])
