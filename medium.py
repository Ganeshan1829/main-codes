#!/bin/python3

import math
import os
import random
import re
import sys
import hashlib
#
# Complete the 'find_nonce' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING data
#  2. INTEGER difficulty
#

def find_nonce(data, difficulty):
     
    
    prefix = "0" * difficulty
    nonce = 0
    
    while True:
        text = data + str(nonce)
        hash_value = hashlib.sha256(text.encode()).hexdigest()
        
        if hash_value.startswith(prefix):
            return nonce
        
        nonce += 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    data = input()

    difficulty = int(input().strip())

    result = find_nonce(data, difficulty)

    fptr.write(str(result) + '\n')

    fptr.close()
