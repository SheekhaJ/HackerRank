#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    res = 'NO'

    for s in s1:
        if s in s2:
            res = 'YES'
            break

    return res


if __name__ == '__main__':
    s1 = 'hello'
    s2 = 'world'
    print(twoStrings(s1, s2))

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input())

    # for q_itr in range(q):
    #     s1 = input()

    #     s2 = input()

    #     result = twoStrings(s1, s2)

    #     fptr.write(result + '\n')

    # fptr.close()
