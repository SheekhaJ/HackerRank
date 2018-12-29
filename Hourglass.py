#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    s = []
    
    for row in range(4):
           for col in range(4):
                  s.append(getHouGlassElementsSum(arr, row, col))
    
    return max(s)

def getHouGlassElementsSum(arr, row, col):
       #To see the hour-glass structures across the cols first use following expression.
       elements = []
       [[elements.append(arr[row+j][col+i]) for i in range(3)] for j in range(3)]
       # print('elements: ', elements) 

       elements.remove(arr[row+1][col])
       elements.remove(arr[row+1][col+2])
       
       #To see the hour-glass structures across the rows first use following expression. 
       # elements = [[arr[row+j][col+i] for i in range(3)] for j in range(3)]
       # print('elements: ', elements) 
       s = 0
       s += sum(elements)
       
       return s


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    # fptr.write(str(result) + '\n')

    # fptr.close()

    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]

    print(hourglassSum(arr))