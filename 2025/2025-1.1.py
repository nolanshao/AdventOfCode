with open('2025_Advent_input.txt') as f:
    lines = f.readlines()

dial = 50
count = 0

for line in lines:
    l = len(line)
    s = line[1:l]
    if line[0] == 'R':
        dial += int(s)
        if dial > 99:
            dial %= 100
        if dial == 0:
            count += 1
    if line[0] == 'L':
        dial -= int(s)
        if dial < 0:
            dial %= 100
        if dial == 0:
            count += 1

m = -999
m %= 100
print(m)

print(dial)
print(count)