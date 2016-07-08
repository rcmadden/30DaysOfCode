import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#print(list(reversed(arr)))
arr.reverse()

print(*arr, sep=' ')