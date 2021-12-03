with open("/home/alex/Projects/advent-of-code-2021/day02/day02.in") as f:
    input = f.read()
A = input.split("\n")[:-1]
h, d, aim = 0, 0, 0
for a in A:
    _dir, amt = a.split(" ")
    if _dir == 'forward':
        h += int(amt)
        d += aim*int(amt)
    elif _dir == 'up':
        aim -= int(amt)
    else:
        aim += int(amt)
print(h*d)