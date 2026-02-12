#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longest_chain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY lengths
#  2. INTEGER_ARRAY valid
#

def longest_chain(lengths, valid):
    max_len = -1
    result = -1
    
    for i in range(len(lengths)):
        if valid[i] == 1 and lengths[i] > max_len:
            max_len = lengths[i]
            result = i
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    lengths = list(map(int, input().rstrip().split()))

    valid = list(map(int, input().rstrip().split()))

    result = longest_chain(lengths, valid)

    fptr.write(str(result) + '\n')

    fptr.close()
