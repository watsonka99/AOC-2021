def file_to_int_arr(input:str)->list[int]:
    arr = []
    with open(input, "r") as f:
        for line in f:
            arr.append(int(line))
    return arr

test_input = file_to_int_arr("Day 1/test.txt")
input = file_to_int_arr("Day 1/input.txt")        

def part_1(input: list[int])-> int:
    increase = 0
    for idx in range(1, len(input)):
        if input[idx] > input[idx-1]:
            increase += 1
    return increase

print('Part 1')
print('test_input:',part_1( test_input) , '== 7')
print('input:', part_1(input))

def part_2(input: list[int])-> int:
    increase = 0
    for idx in range(3, len(input)):
        if input[idx] > input[idx-3]:
            increase += 1
    return increase

print('Part 2')
print('test_input:', part_2(test_input), '== 5')
print('input:', part_2(input))
