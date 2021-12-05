def open_file(filename):
    skip = 1
    boards = []
    board = []
    with open(filename, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                line = line.strip('\n')
                seq = [int(n) for n in line.split(',')]
            elif i == 1:
                continue
            elif line == '\n':
                boards.append(board)
                board = []
            else:
                line = line.strip('\n')
                row = line.split(' ')
                board.append([int(n) for n in row if n != ''])    
    boards.append(board)  
    return seq, boards


def check_row(row):
    for n in row: 
        if n is not None:
            return False
    return True

def check_board(board):
    for i, row in enumerate(board):
        if check_row(row):
            return True
    for i in range(0, len(board[0])):
        col = [line[i] for line in board]
        if check_row(col):
            return True
    return False

def part_1(seq, boards):
    boards
    for number in seq:
        for i, board in enumerate(boards):
            for row in board:
                for j, n in enumerate(row):
                    if n == number:
                        row[j] = None
                        if check_board(board):
                            sum = 0
                            for row in board:
                                for num in row:
                                    if num is not None:                                
                                        sum += num
                            return sum * number
                        
test_seq, test_board = open_file('Day 4/test.txt')
seq, board = open_file('Day 4/input.txt')
print(part_1(test_seq, test_board))
print(part_1(seq, board))

def part_2(seq, boards):
    deleted = False
    for number in seq:
        i = 0
        while (i < (len(boards))):
            for row in boards[i]:
                for j, n in enumerate(row):
                    if n == number:
                        row[j] = None
                        if check_board(boards[i]):
                            if len(boards) != 1:
                                del boards[i]
                                deleted = True
                            else:
                                sum = 0
                                for row in boards[i]:
                                    for num in row:
                                        if num is not None:                                
                                            sum += num
                                return sum * number
            if deleted == True:
                deleted = False
                i -= 1
            else:
                i += 1
            
                            
print(part_2(test_seq, test_board))
print(part_2(seq, board))