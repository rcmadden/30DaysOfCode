#!/bin/python3

import sys


N = int(input().strip())
if N > 20:
    if N % 2 == 0:
        print("Not Weird")
elif 6 <= N <= 20:
    if N % 2 == 0:
        print("Weird")
elif N % 2 == 0:
        if 2 <= N <= 5:
            print("Not Weird")
# odd
else:
    print("Weird")
