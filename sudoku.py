import sys


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

    def check_col(self, col_number):
        list = []
        for x in range(0, self.dimension):
            list.append(self.table[x][col_number])
        return sum(list) == self.goal

    def check_cuadrant(self):
        result = []
        result.append(sum([self.table[0][0],self.table[0][1],self.table[1][0],self.table[1][1]]))
        result.append(sum([self.table[0][2],self.table[0][3],self.table[1][2],self.table[1][3]]))
        result.append(sum([self.table[2][0],self.table[2][1],self.table[3][0],self.table[3][1]]))
        result.append(sum([self.table[2][2],self.table[2][3],self.table[3][2],self.table[3][3]]))
        return all(x == self.goal for x in result)

    def is_solve(self):
        solve_list = []
        # check rows
        for line in self.table:
            solve_list.append(self.check_row(line))
        # check columns
        for col_number in range(0, self.dimension):
            solve_list.append(self.check_col(col_number))
        # check cuadran
        solve_list.append(self.check_cuadrant())
        return all(element is True for element in solve_list)

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
    print('seems like the sudoku is missing something, may be size is incorrect!')
    exit(1)

mySudoku.show_table()
print('i have a solution:',mySudoku.is_solve())
