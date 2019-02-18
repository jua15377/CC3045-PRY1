import sys
from sudoku_framework import *


class sudokuTable:
    def __init__(self):
        self.table = [[0 for x in range(0,4)] for y in range(0,4)]
        self.step = 0
        self.goal = 10
        self.dimension = 4

    def clear_table(self):
        for x in range(0,self.dimension):
            for y in range(0, self.dimension):
                self.table[x][y] = 0

    def check_row(self, row):
        return sum(row) == self.goal

    def check_col(self, table, col_number):
        list = []
        for x in range(0, self.dimension):
            list.append(table[x][col_number])
        return sum(list) == self.goal

    def check_cuadrant(self, table):
        result = []
        result.append(sum([table[0][0],table[0][1],table[1][0],table[1][1]]))
        result.append(sum([table[0][2],table[0][3],table[1][2],table[1][3]]))
        result.append(sum([table[2][0],table[2][1],table[3][0],table[3][1]]))
        result.append(sum([table[2][2],table[2][3],table[3][2],table[3][3]]))
        return all(x == self.goal for x in result)

    def is_solve(self):
        solve_list = []
        # check rows
        for line in self.table:
            solve_list.append(self.check_row(line))
        # check columns
        for col_number in range(0, self.dimension):
            solve_list.append(self.check_col(self.table, col_number))
        # check cuadran
        solve_list.append(self.check_cuadrant(self.able))
        return all(element is True for element in solve_list)

    def get_cuadrant(self, cord):
        if cord is 0:
            return [self.table[0][0],self.table[0][1],self.table[1][0],self.table[1][1]]
        elif cord is 1:
            return [self.table[0][2],self.table[0][3], self.table[1][2], self.table[1][3]]
        elif cord is 2:
            return [self.table[2][0], self.table[2][1], self.table[3][0], self.table[3][1]]
        elif cord is 3:
            return [self.table[2][2], self.table[2][3], self.table[3][2], self.table[3][3]]

    def get_row(self, x):
        return self.table[x]

    def get_col(self, y):
        list = []
        for x in range(0, self.dimension):
            list.append(self.table[x][y])
        return list

    def show_table(self):
        print('--sudoku step: %s --' % (str(self.step)))
        for line in self.table:
            result = '    |'
            for c in line:
                if c == 0:
                    result = result + ' ' + '|'
                else:
                    result = result + str(c) + '|'
            print(result)

input = sys.argv
values = input[1]
values = list(values)
mySudoku = sudokuTable()

cont = 0
try:
    for x in range(0,4):
        for y in range(0,4):
            if values[cont] == '.':
                mySudoku.table[x][y] = 0
            else:
                mySudoku.table[x][y] = int(values[cont])
            cont = cont + 1
except IndexError:
    print('seems like the sudoku is missing something, may be incorrect size!')
    exit(1)

mySudoku.show_table()
print('i have a solution:', mySudoku.is_solve(mySudoku.table))
print(mySudoku.get_col(0))
print(mySudoku.get_row(0))
my_a_star = sudoku_framework(mySudoku)
