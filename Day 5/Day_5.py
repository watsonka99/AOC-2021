def open_file(filename):
    skip = 1
    start_arr = []
    end_arr = []
    with open(filename, "r") as f:
        for __, line in enumerate(f):
            line = line.strip('\n')
            start, end = line.split('->')
            start = start.strip()
            end = end.strip()
            start_arr.append([int(x) for x in start.split(',')])
            end_arr.append([int(x) for x in end.split(',')])

    return start_arr, end_arr


test_start, test_end = open_file('Day 5/test.txt')

input_start, input_end = open_file('Day 5/input.txt')


def part_1(start, end):
    lines = set()
    crossover_point = set()
    for i, point in enumerate(start):
        x_1, y_1 = point
        x_2, y_2 = end[i]
        if x_1 != x_2 and y_1 == y_2:
            if x_1 > x_2:
                x_1, x_2 = x_2, x_1
            for j in range(x_1, x_2+1):
                if (j, y_1) in lines:
                    crossover_point.add((j, y_1))
                else:
                    lines.add((j, y_1))
        elif y_1 != y_2 and x_1 == x_2:
            if y_1 > y_2:
                y_1, y_2 = y_2, y_1
            for j in range(y_1, y_2+1):
                if (x_1, j) in lines:
                    crossover_point.add((x_1, j))      
                else:
                    lines.add((x_1, j))
    return len(crossover_point)


print(part_1(test_start, test_end))
print(part_1(input_start, input_end))


def part_2(start, end):
    lines = set()
    crossover_point = set()
    for i, point in enumerate(start):
        x_1, y_1 = point
        x_2, y_2 = end[i]
        x_increase = 0
        y_increase = 0
        if x_1 != x_2:
            x_increase = 1
            if x_1 > x_2:
                x_increase = -1
        if y_1 != y_2:
            y_increase = 1
            if y_1 > y_2:
                y_increase = -1
        if (x_1, y_1) in lines:
            crossover_point.add((x_1, y_1))
        else:
            lines.add((x_1, y_1))
        while (x_1, y_1) != (x_2, y_2):
            x_1 += x_increase
            y_1 += y_increase
            if (x_1, y_1) in lines:
                crossover_point.add((x_1, y_1))
            else:
                lines.add((x_1, y_1))
    return len(crossover_point)


print(part_2(test_start, test_end))
print(part_2(input_start, input_end))
