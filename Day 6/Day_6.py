def open_file(filename):
    skip = 1
    start_arr = []
    end_arr = []
    with open(filename, "r") as f:
        line = f.readline()
        return [int(x) for x in line.split(',')]


test_start = open_file('Day 6/test.txt')
input_start = open_file('Day 6/input.txt')


def part_1(input, days):
    for day in range(days):
        for idx in range(len(input)):
            input[idx] -= 1
            if input[idx] == -1:
                input[idx] = 6
                input.append(8)
    return len(input)


print(part_1(test_start, 18))
#print(part_1(test_start, 80))
print(part_1(input_start, 80))


def part_2(input, days):
    fish = {
        -1: 0,
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }
    for values in range(0, 8):
        fish[values] = input.count(values)
    for day in range(days):
        for x in range(0, 9):
            fish[x-1] = fish[x]
        fish[6] = fish[6] + fish[-1]
        fish[8] = fish[-1]
        fish[-1] = 0

    sum = 0
    for value in range(0, 9):
        sum += fish[value]
    return sum

test_start = open_file('Day 6/test.txt')
print(part_2(test_start, 18))
input_start = open_file('Day 6/input.txt')
print(part_2(test_start, 80))
input_start = open_file('Day 6/input.txt')
print(part_2(input_start, 80))

input_start = open_file('Day 6/input.txt')
print(part_2(input_start, 256))
