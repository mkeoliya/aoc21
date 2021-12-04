class Number:
    def __init__(self, num):
        self.num = num
        self.is_marked = False

    def __repr__(self):
        return str(self.num) + str(self.is_marked)


class Board:
    def __init__(self, board):
        self.has_won = False
        self.board = [[Number(val) for val in row] for row in board]
        self.r_count = [0] * 5
        self.c_count = [0] * 5
        self.hash = {}
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                self.hash[val] = (i, j)

    def get_winning_score(self, winning_num):
        sum = 0
        for row in self.board:
            for val in row:
                sum += 0 if val.is_marked else val.num

        return sum * winning_num


with open('input.txt') as f:
    nums = [int(v) for v in f.readline().strip().split(',')]
    boards = []
    while True:
        if not f.readline():
            break

        board = []
        for i in range(5):
            row = [int(v) for v in f.readline().strip().split()]
            board.append(row)

        boards.append(Board(board))

winning_idx = -1
winning_board = None
winning_num = 0
for num in nums:
    for b, board in enumerate(boards):
        if num in board.hash:
            i, j = board.hash[num]

            if board.has_won:
                continue

            board.board[i][j].is_marked = True
            board.r_count[i] += 1
            board.c_count[j] += 1

            if board.r_count[i] == 5 or board.c_count[j] == 5:
                board.has_won = True
                winning_board = board
                winning_num = num

print(winning_board.get_winning_score(winning_num))
