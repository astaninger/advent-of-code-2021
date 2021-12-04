#!/usr/bin/env python

import sys, itertools, collections

arr = []
for line in sys.stdin:
    arr.append(line.strip())
nums = arr[0].split(',')
boards = []

currBoard = []
for line in arr[2:]:
    if line != '':
        currBoard.append(line.split())
    else:
        boards.append(currBoard)
        currBoard = []

def checkNeighbors(b, i , j):
    for x in range(len(boards[b])):
        if boards[b][x][j] != '*':
            break
    else:
        return True
    
    for x in range(len(boards[b][0])):
        if boards[b][i][x] != '*':
            break
    else:
        return True

    return False
def calculateAns(b, i, j, num):
    ans = 0
    for i in range(len(boards[b])):
        for j in range(len(boards[b][i])):
            if boards[b][i][j] != '*':
                ans += int(boards[b][i][j])
    return ans * int(num)
for num in nums:
    for b in range(len(boards)):
        for i in range(len(boards[0])):
            for j in range(len(boards[0][0])):
                if boards[b][i][j] == num:
                    boards[b][i][j] = '*'
                    if checkNeighbors(b, i , j):
                        print(calculateAns(b, i, j, num))
                        break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break

solved = set()
for num in nums:
    for b in range(len(boards)):
        if b not in solved:
            for i in range(len(boards[0])):
                for j in range(len(boards[0][0])):
                    if boards[b][i][j] == num:
                        boards[b][i][j] = '*'
                        if checkNeighbors(b, i , j):
                            solved.add(b)
                            if len(solved) == len(boards):
                                print(calculateAns(b, i, j, num))
