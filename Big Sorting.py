#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    buckets = {}
    
    for s in unsorted:
        hossz = len(s)
        if hossz not in buckets:
            buckets[hossz] = []
        buckets[hossz].append(s)
    
    sorted_result = []
    
    for hossz in sorted(buckets.keys()):
        buckets[hossz].sort()
        
        sorted_result.extend(buckets[hossz])
        
    return sorted_result

if __name__ == '__main__':
    

    unsorted = ['6', '31415926535897932384626433832795', '1', '3', '10', '3', '5']

    

    result = bigSorting(unsorted)
    print(result)
    
