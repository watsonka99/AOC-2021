def file_to_str_arr(input:str)->list[str]:
    arr = []
    with open(input, "r") as f:
        for line in f:
            arr.append(line.strip('\n'))
    return arr

def movement(input: list[str])->int:
    pos = [0, 0]
    for __, order in enumerate(input):
        command, quantity = order.split(' ')
        quantity = int(quantity)
        if command == 'forward':
            pos[0] += quantity
        elif command == 'down':
            pos[1] += quantity
        elif command == 'up':
            pos[1] -= quantity
    return pos[0] * pos[1]

test_input = file_to_str_arr('Day 2/test.txt')
input = file_to_str_arr('Day 2/input.txt')
print(movement(test_input))
print(movement(input))

def aim(input: list[str])->int:
    pos = [0, 0, 0]
    for __, order in enumerate(input):
        command, quantity = order.split(' ')
        quantity = int(quantity)
        if command == 'forward':
            pos[1] += pos[2] * quantity
            pos[0] += quantity
        elif command == 'down':
            pos[2] += quantity
        elif command == 'up':
            pos[2] -= quantity
    return pos[0] * pos[1]

print(aim(test_input))
print(aim(input))