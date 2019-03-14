directions = [0,0,0,0]
direction = 0

with open('advent_data.txt') as f:
    data = f.read()

moves = data.split(', ')
for move in moves:
    letter = move[0]
    number = int(move[1:])
    if letter == 'L':
        direction -= 1
    else:
        direction += 1
    direction %= len(directions)
    directions[direction] += number

print(abs(directions[0] - directions[2]) + abs(directions[1] - directions[3]))
