'''
Capitalized the first letters in a full name

Input:
chris alan

Output:
Chris Alan

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for word in s[:].split():
        s = s.replace(word, word.capitalize())
    return s

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    print(result)
    #fptr.write(result + '\n')

    #fptr.close()
