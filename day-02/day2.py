import inputs

cmds = inputs.part_1.splitlines()
pos = 0
depth = 0

for cmd in cmds:
    cmd, offset = cmd.split()
    if cmd == 'forward':
        pos += int(offset)
    elif cmd == 'down':
        depth += int(offset)
    elif cmd == 'up':
        depth -= int(offset)

print(pos * depth)

pos = 0
depth = 0
aim = 0

for cmd in cmds:
    cmd, offset = cmd.split()
    if cmd == 'forward':
        pos += int(offset)
        depth += aim * int(offset)
    elif cmd == 'down':
        aim += int(offset)
    elif cmd == 'up':
        aim -= int(offset)

print(pos * depth)
