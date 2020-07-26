#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    one= 0
    two= 0
    for count in range(len(arr)):
        one+= arr[count][count]
        two+= arr[count][-1-count]
    return abs(one- two)

if __name__ == '__main__':
41
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)