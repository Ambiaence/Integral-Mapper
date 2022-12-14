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
    def __init__(self, numOfQuestions, f, start, end):
        self.__totalArea = quad(f, start, end)[0]
        self.__divisions = [] # list of points on the map
        self.__integralSliceLength = (end-start)/numOfQuestions #Length of each sub interval
        for i in range(0, numOfQuestions):
            print(i)
            sliceProgress = self.__integralSliceLength * (i+1) 
            self.__divisions.append(quad(f, start, sliceProgress)[0]/self.__totalArea)
        
        for x in self.__divisions:
            print(x)

    def pickRandomIndex(self):
        index = 0
        value = random.uniform(0, 1)
        for x in self.__divisions:
            if value < x:
                return index
            index = index + 1
        return index

f = lambda x: 4*x

hype = integralMap(2, f, 0, 1.5)
ls = []
for x in range(0, 4):
    ls.append(0)
for x in range(0, 100000):
    index = hype.pickRandomIndex()
    ls[index] = ls[index] + 1

for x in range(0, 4):
    print(ls[x])
