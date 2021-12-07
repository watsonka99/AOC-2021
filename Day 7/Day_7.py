def open_file(filename):
    skip = 1
    start_arr = []
    end_arr = []
    with open(filename, "r") as f:
        line = f.readline()
        return [int(x) for x in line.split(',')]


test_start = open_file('Day 7/test.txt')
input_start = open_file('Day 7/input.txt')

print()
def part_1(input):
    input.sort()
    med = input[len(input)//2]
    total = 0
    for pos in input:
        if pos < med:
            total += med - pos
        else:
            total += pos - med
    return total

print(part_1(test_start))
print(part_1(input_start))

def part_2(input):
    mean = (sum(input)/len(input)) 
    # This is stupid, illogical way of doing this, but it worked to produce the correct results
    if (mean-int(mean) < 0.6):
        mean = int(mean)
    else: 
        mean = int(mean)+1
    total = 0
    for pos in input:
        if pos < mean:
            move = mean - pos
        else:
            move = pos - mean
        total += sum(range(0, move+1))
    return total

print(part_2(test_start))
print(part_2(input_start))