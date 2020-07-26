#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    res=[0,0]
    for num in range(len(a)):
        if a[num] > b[num]:
            res[0]+= 1
        elif a[num] < b[num]:
            res[1]+= 1
    return res

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)
