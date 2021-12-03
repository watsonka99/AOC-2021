def file_to_str_arr(input:str)->list[str]:
    arr = []
    with open(input, "r") as f:
        for line in f:
            arr.append(line.strip('\n'))
    return arr


test_input = file_to_str_arr('Day 3/test.txt')
input = file_to_str_arr('Day 3/input.txt')

def part_1(input):
    gamma = ""
    epislon = ""
    for idx in range(len(input[0])):
        counter=0
        for bin in input:
            if bin[idx] =="1":
                counter += 1
            else:
                counter -= 1
        if counter > 0:
            gamma +="1"
            epislon += "0"
        else:
            gamma += "0"
            epislon += "1"       
    return int(gamma, 2) * int(epislon,2)

print(part_1(test_input))
print(part_1(input))

def o2_gen_rating(input):
    for idx in range(len(input[0])):
        counter=0
        for bin in input:
            if bin[idx] =="1":
                counter += 1
            else:
                counter -= 1
        if counter >= 0:
            input = [bin for bin in input if bin[idx] == "1"]
        else:
            input = [bin for bin in input if bin[idx] == "0"]
    return int(input[0],2)

def o2_scrub_rating(input):
    for idx in range(len(input[0])):
        if len(input) == 1:
            break
        counter=0
        for bin in input:
            if bin[idx] =="1":
                counter += 1
            else:
                counter -= 1
        if counter >= 0:
            input = [bin for bin in input if bin[idx] == "0"]
        else:
            input = [bin for bin in input if bin[idx] == "1"]
    return int(input[0],2)

def part_2(input):
    scrub = o2_scrub_rating(input)
    gen = o2_gen_rating(input)
    return scrub * gen

print(part_2(test_input))
print(part_2(input))