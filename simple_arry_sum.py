import os
import sys

def simpleArraySum(ar):
    sum =0
    for el in ar:
        sum+= el
    return sum

if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    print(result)
