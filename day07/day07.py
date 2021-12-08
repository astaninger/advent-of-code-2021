#!/usr/bin/env python

import sys, itertools, collections

arr = []
for line in sys.stdin:
    arr.append(line.strip())
arr = [int(n) for n in arr[0].split(',')]
# with open("input.txt") as file:
#     inp = file.read().strip() 11 = 11*10/2
ans = float('inf')
for i in range(0, max(arr)+1):
    gas = 0
    for n in arr:
        dist = abs(n - i)
        gas += ((dist*(dist+1))//2)
        # print(gas)
    ans = min(ans, gas)
    # print('---')
    # print(line)
print(ans)
# for line in arr:
#     print(line)
