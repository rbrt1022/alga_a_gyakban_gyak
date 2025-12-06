#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr.sort()
    diffMin = -1
    for i in range(len(arr)-k):
        sub = arr[i:i+k]
        print(sub)
        diff = max(sub) - min(sub)
        print(f"Difi: {diff}")
        if diffMin == -1 or diff < diffMin:
            diffMin = diff
            print(f"DifiMini: {diffMin}")
    return diffMin   
    

if __name__ == '__main__':

    #arr = [7, 3, 10, 100, 300, 200, 1000, 20, 30]
    arr = [
    100000, 10000, 58457907, 37850775, 19743393, 70718573, 34395679, 
    32448076, 48664348, 12492248, 77695616, 66342676, 38120300, 9282025, 
    55261855, 43659379, 33441482, 86981291, 40931037, 88952744
    ]
    k = 3

    result = maxMin(k, arr)
    print(result)
