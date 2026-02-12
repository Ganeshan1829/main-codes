#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'detect_duplicates' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY tx as parameter.
#

def detect_duplicates(tx):
    if len(tx) != len(set(tx)):
        return "Duplicate Found"
    else:
        return "All Unique"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    tx = input().rstrip().split()

    result = detect_duplicates(tx)

    fptr.write(result + '\n')

    fptr.close()
