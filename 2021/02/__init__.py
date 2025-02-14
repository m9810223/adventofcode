def cast_input(inputs):
    def cast_line(line):
        d, v = line.split()
        return d, int(v)

    return [cast_line(line) for line in inputs.split("\n")]


def part1(inputs):
    depth = position = 0
    for c, x in inputs:
        if c == "forward":
            position += x
        elif c == "down":
            depth += x
        elif c == "up":
            depth -= x
    return depth * position


def part2(inputs):
    aim = depth = position = 0
    for c, x in inputs:
        if c == "down":
            aim += x
        elif c == "up":
            aim -= x
        elif c == "forward":
            position += x
            depth += aim * x
    return depth * position
