
"""
Student: Lior Silberman
ID: 316456623
Assignment no. 1
Program: minesweeper.py
"""

import random

class MSSquare:
    def __init__(self, has_mine = False):
        self.has_mine = has_mine
        self.hidden = True
        self.neighbor_mines = 0
        
    def __str__(self):
        '''
        filled square in board
        ''' 
        ret_str = " "
        if not self.hidden and self.has_mine:
            ret_str = "X"
        elif not self.hidden:
            ret_str = "{}".format(self.neighbor_mines)
        return ret_str

    def expose(self):
        '''
        exsose square in board
        '''
        self.hidden = False

    def is_exposed(self):
        '''
        square is expose
        '''
        return not self.hidden

    def is_mined(self):
        '''
        there is mine in square 
        '''
        return self.has_mine

    def num_neighbor_mines(self):
        '''
        give value to square
        '''
        return self.neighbor_mines

class Board:
    def __init__(self, size, mines):
        self.board = []
        self.build_board(size, mines)
        self.size = size
        self.dug = set()
        self.assign_values_to_board()

    def __str__(self):
        '''
        return board design
        '''
        rep_str = ""
        n = 1
        prev_n = 0
        next_n = 0
        for r in range(self.size*2+1):
            for c in range(self.size+1):
                if r%2 == 0 and c < self.size:
                    if c == 0:
                        rep_str += "  "
                    rep_str += "+"
                    rep_str += "---"
                    if c == self.size-1:
                        rep_str += "+"
                if r%2 != 0 and c == 0:
                    rep_str += "{} |".format(n)
                    n += 1
                if r%2 != 0 and c != 0:
                    rep_str += " "
                    rep_str += str(self.board[prev_n][next_n])
                    rep_str += " |"
                    next_n += 1
                if next_n == self.size:
                    prev_n += 1
                    next_n -= next_n
            rep_str += '\n'

        for z in range(self.size):
            if z == 0:
                rep_str += " "
            rep_str += "   " + str(z+1)

        return rep_str

    def build_board(self, size, mines_counter):
        '''
        build baord and plant mines on board
        '''
        # choose mines position on board
        mines_position = []
        for i in range(mines_counter):
            while True:
                x = random.randint(0, size-1)
                y = random.randint(0, size-1)
                if (x,y) not in mines_position:
                    break
            mines_position.append((x,y))

        # build board and plant mines
        for x in range(size):
            self.board.append([])
            for y in range(size):
                plant_mine = True if (x,y) in mines_position else False
                self.board[x].append(MSSquare(has_mine=plant_mine))

    # mark neighbors to mines
    def assign_values_to_board(self):
        '''
        give values for neighbor mines square
        '''
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c].is_mined():
                    continue
                self.board[r][c].neighbor_mines += self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        '''
        helper function for values to neighbor mines
        '''
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.size-1, col+1)+1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c].is_mined():
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def get_board_size(self):
        '''
        return board size
        '''
        return len(self.board)

    # expose all mines if loose
    def expose_all_mines(self):
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y].is_mined():
                    self.board[x][y].expose()
                
    # expose all board
    def expose_all(self):
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                self.board[x][y].expose()

    def mine_sweepered(self):
        '''
        check if all nonmines squares are exsposed
        '''
        sweepered = True
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if not self.board[x][y].is_exposed() and not self.board[x][y].is_mined():
                    sweepered = False
        return sweepered

    
    def dig(self, row, col):
        '''
         dig at location with no neighboring bombs -> recursively dig neighbors!
         '''
        self.dug.add((row, col))
        # cell is mined?
        if self.board[row][col].is_mined():
            return False
        elif self.board[row][col].neighbor_mines > 0:
            return True

        for r in range(max(0, row-1), min(self.size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue # don't dig where you've already dug
                
                # expose cell
                self.board[r][c].expose()
                self.dig(r, c)
        return True

    def expend_selection(self, x, y):
        # cell is mined?
        if self.board[x][y].is_mined():
            return
        # expose cell
        self.board[x][y].expose()

def main():
    while True:
        try:
            size = int(input("Enter size: "))
            if size < 4 or size > 9:
                print("size is illegal")
                continue
            mines = int(input("Enter number of mines (no more than twice the size!): "))
            if mines > 2 * size:
                print("too many mines")
                continue
            break
        except ValueError:
            print("illegal input")

    board = Board(size, mines)
    print(board)

    # start game
    while True:
        # get user move
        move = [int(i)-1 for i in input("Enter your choice (row column) [-1 for quit]:  ").split()]

        # user asked quit?
        if len(move) == 1 and move[0] == -2:
            print("You hit a mine. You lose...")
            board.expose_all()
            print(board)
            break

        # input is legal?
        if len(move) != 2 or move[0] < 0 or move[0] > board.get_board_size()-1 or move[1] < 0 or move[1] > board.get_board_size()-1:
            print("illegal move")
            continue

        # cell is already exposed?
        if board.board[move[0]][move[1]].is_exposed():
            continue

        # cell has mine?
        if board.board[move[0]][move[1]].is_mined():
            board.expose_all_mines()
            print(board)
            print("You hit a mine. You lose...")
            break

        # expend selected cell
        board.expend_selection(move[0], move[1])
        safe = board.dig(move[0], move[1])

        # all mines found?
        if board.mine_sweepered():
            board.expose_all()
            print("You win!")
            print(board)
            break

        # print updated board
        print(board)

main()