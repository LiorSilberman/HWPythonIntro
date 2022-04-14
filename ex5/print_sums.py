# -*- coding: utf-8 -*-
class Cell(object):
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.visited = False

def main():
    n = 30   # Works ... but not, for example, for 40.
    board = [[Cell(i,j) for j in range(n)] for i in range(n)]
    uncover_cells(0, 0, board)
    for row in board:
        for cell in row:
            assert cell.visited

main()