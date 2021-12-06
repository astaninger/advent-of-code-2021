#!/usr/bin/env python

import sys, itertools, collections

arr1 = []
for line in sys.stdin:
    arr1.append(line.strip())

arr = arr1[0].split(',')
arr2 = arr1[0].split(',')

for _ in range(80):
    currLen = len(arr)
    for i in range(currLen):
        arr[i] = int(arr[i])
        arr[i] -= 1
        if arr[i] == -1:
            arr[i] = 6
            arr.append(8)
print(len(arr))

ans = 0
daysLeft = [0]*7
for n in arr2:
    daysLeft[int(n)] += 1
daysLeft = collections.deque(daysLeft)
babies = collections.deque([0, 0])
for _ in range(256):
    birthing = daysLeft.popleft()
    daysLeft.append(birthing + babies.popleft())
    babies.append(birthing)

print(sum(daysLeft) + sum(babies))
