with open("/home/alex/Projects/advent-of-code-2021/day01/day01.in") as f:
    input = f.read()
A = input.split("\n")[:-1]
ans = 0
lastSum = None
for i in range(1, len(A)-1):
    newSum = int(A[i-1]) + int(A[i]) + int(A[i+1])
    if lastSum is not None and newSum >lastSum:
        ans += 1
    lastSum = newSum
print(ans)
