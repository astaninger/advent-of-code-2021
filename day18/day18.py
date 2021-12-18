#!/usr/bin/env python

from sys import *
from collections import *
from itertools import *
from heapq import *
from math import *

arr = []
for line in stdin:
    arr.append(eval(line.strip()))

class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

def convertToTree(A, par):
    if type(A) is int:
        return Node(A, par)
    root = Node(-1, par)
    root.left = convertToTree(A[0], root)
    root.right = convertToTree(A[1], root)
    return root

def reduce(node):
    last= None
    addToNext= None
    def explode(node, height):
        nonlocal last, addToNext
        if not node:
            return
        if addToNext is not None and node.val != -1:
            node.val += addToNext
            addToNext = None
            raise Exception()
        if addToNext is None and height >= 4 and node.val == -1 and node.left.val != -1 and node.right.val !=-1:
            if last:
                last.val += node.left.val
            addToNext = node.right.val
            node.val = 0
            node.left = None
            node.right = None
            return
        if node.val != -1:
            last = node
        explode(node.left, height+1)
        explode(node.right, height+1)
    def split(node):
        if not node:
            return
        if node.val > 9:
            node.left = Node(floor(node.val/2.0))
            node.right = Node(ceil(node.val/2.0))
            node.val = -1
            raise Exception()
        split(node.left)
        split(node.right)

    mod = True
    while mod:
        mod = False
        try:
            explode(node, 0)
        except:
            mod = True
            continue
        try:
            split(node)
        except:
            mod = True
        last= None
        addToNext= None

root = convertToTree(arr[0], None)
for line in arr[1:]:
    temp = root
    root = Node(-1)
    root.left = temp
    root.right = convertToTree(line, root)
    root.left.parent = root
    reduce(root)

def dfs(node):
    if node.val != -1:
        return node.val
    
    left = dfs(node.left)
    right = dfs(node.right)
    return 3*left + 2*right
ans = dfs(root)
print("ANS", ans)

ans = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j: continue
        root = Node(-1)
        root.left = convertToTree(arr[i], root)
        root.right = convertToTree(arr[j], root)
        reduce(root)
        ans = max(ans, dfs(root))
print("ANS", ans)       