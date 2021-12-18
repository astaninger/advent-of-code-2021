#!/usr/bin/env python

from sys import *
from collections import *
from itertools import *
from heapq import *

arr = []
for line in stdin:
    arr.append(line.strip())

num = arr[0]
binary = bin(int(num, 16))[2:].zfill(len(num)*4)
versionSum = 0

def getNum(i):
    num = ""
    while binary[i] == '1':
        num += binary[i+1:i+5]
        i+=5
    num += binary[i+1:i+5]
    return int(num,2), i+5

def getType1(i, j):
    numberOfSubPackets = int(binary[i+7:i+18], 2)
    k = i+18
    nums = []
    for _ in range(numberOfSubPackets):
        num, k = parse(k, j)
        nums.append(num)
    return nums, k

def getType0(i, j):
    totalLengthOfSubPackets = int(binary[i+7:i+22], 2)
    k = i+22
    nums = []
    while k < i+22+totalLengthOfSubPackets:
        num, k = parse(k, totalLengthOfSubPackets)
        nums.append(num)
    return nums, k

def parse(i, j):
    global versionSum
    version = int(binary[i:i+3], 2)
    versionSum += version
    typeId = int(binary[i+3:i+6], 2)

    if typeId == 0:
        lengthTypeId = binary[i+6:i+7]
        nums, k = getType1(i, j) if lengthTypeId == '1' else getType0(i, j)
        num = sum(nums)
    elif typeId == 1:
        lengthTypeId = binary[i+6:i+7]
        nums, k = getType1(i, j) if lengthTypeId == '1' else getType0(i, j)
        num = 1
        for n in nums:
            num *= n
    elif typeId == 2:
        lengthTypeId = binary[i+6:i+7]
        nums, k = getType1(i, j) if lengthTypeId == '1' else getType0(i, j)
        num = min(nums)
    elif typeId == 3:
        lengthTypeId = binary[i+6:i+7]
        nums, k = getType1(i, j) if lengthTypeId == '1' else getType0(i, j)
        num = max(nums)
    if typeId == 4:
        return getNum(i+6)
    elif typeId == 5:
        lengthTypeId = binary[i+6:i+7]
        nums, k = getType1(i, j) if lengthTypeId == '1' else getType0(i, j)
        num = 1 if nums[0] > nums[1] else 0
    elif typeId == 6:
        lengthTypeId = binary[i+6:i+7]
        nums, k = (getType1(i, j) if lengthTypeId == '1' else getType0(i, j))
        num = 1 if nums[0] < nums[1] else 0
    elif typeId == 7:
        lengthTypeId = binary[i+6:i+7]
        nums, k = (getType1(i, j) if lengthTypeId == '1' else getType0(i, j))
        num = 1 if nums[0] == nums[1] else 0
    return num, k


ans = parse(0, len(binary))
print(versionSum)
print(ans[0])
