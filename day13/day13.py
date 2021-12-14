#!/usr/bin/env python

from sys import *
from collections import *
from itertools import *
from heapq import *

N = 1500
arr = [[0 for _ in range(N)] for _ in range(N)]
folds = []
for line in stdin:
    if line.strip().startswith("fold"):
        x, y, z = line.strip().split()
        folds.append(z.split('='))
    elif line.strip() == "":
        pass
    else:
        x, y = line.strip().split(',')
        x = int(x)
        y = int(y)
        arr[y][x] = 1

    

# with open("input.txt") as file:
#     inp = file.read().strip()
# for i in range(N):
#     print(arr[i][:30])
for fold1dir, fold1size in folds:
    fold1size = int(fold1size)
    if fold1dir == 'x':
        for i in range(len(arr)):
            for j in range(fold1size+1, len(arr[i])):
                if arr[i][j]  > 0:
                    arr[i][j] = 0
                    arr[i][fold1size - (j - fold1size)] += 1
    else:
        for i in range(fold1size+1, len(arr)):
            for j in range(len(arr[i])):
                # print(i, j, '=>', fold1size - (i - fold1size),j)
                if arr[i][j] >= 1:
                    arr[i][j] = 0
                    arr[fold1size - (i - fold1size)][j] += 1
    # print('----')
    # for i in range(N):
    #     print(arr[i][:30])

ans = 0
hits = []
minI, maxI = float('inf'), float('-inf')
minJ,maxJ =float('inf'), float('-inf')
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] > 0:
            ans += 1
            arr[i][j] = 1
            minI = min(minI, i)
            minJ = min(j, minJ)
            maxI = max(maxI, i)
            maxJ = max(maxJ, j)
            hits.append([i, j])
for i in range(minI, maxI+1):
    for j in range(minJ, maxJ+1):
        print(arr[i][j], end="")
    print()
print(ans)
print(hits)
