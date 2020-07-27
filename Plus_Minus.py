#!/bin/python3

import math
import os

# Complete the plusMinus function below.
def plusMinus(arr):
    arr= [True if el>0 else False if el<0 else None for el in arr]
    print('{:.6f}'.format(arr.count(True)/ len(arr)))
    print('{:.6f}'.format(arr.count(False)/ len(arr)))
    print('{:.6f}'.format(arr.count(None)/ len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
