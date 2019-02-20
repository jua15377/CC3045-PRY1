import sys
from random import randint

class sixtenn:
    def __init__(self, input):
        self.board = input
        self.empty_cell = input.index('.')
        self.left_frontier = [0,4,8,12]
        self.right_frontier = [3,7,11,15]
        self.top_frontier = [0,1,2,3]
        self.bottom_frontier = [12,13,14,15]
        self.goal = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','.']

    def move_up(self, symbol):
        index_of_symbol =  self.board.index(symbol)
        if index_of_symbol not in self.top_frontier:
            new_index_of_symbol = index_of_symbol - 4
            if new_index_of_symbol == self.empty_cell:
                self.board[self.empty_cell] = symbol
                self.board[index_of_symbol] = '.'
                self.empty_cell = index_of_symbol
                return True
            else:
                return False
        else:
            return False

    def move_down(self, symbol):
        index_of_symbol =  self.board.index(symbol)
        if index_of_symbol not in self.bottom_frontier:
            new_index_of_symbol = index_of_symbol + 4
            if new_index_of_symbol == self.empty_cell:
                self.board[self.empty_cell] = symbol
                self.board[index_of_symbol] = '.'
                self.empty_cell = index_of_symbol
                return True
            else:
                return False
        else:
            return False

    def move_left(self, symbol):
        index_of_symbol = self.board.index(symbol)
        if index_of_symbol not in self.left_frontier:
            new_index_of_symbol = index_of_symbol - 1
            if new_index_of_symbol == self.empty_cell:
                self.board[self.empty_cell] = symbol
                self.board[index_of_symbol] = '.'
                self.empty_cell = index_of_symbol
                return True
            else:
                return False
        else:
            return False

    def move_right(self, symbol):
        index_of_symbol = self.board.index(symbol)
        if index_of_symbol not in self.right_frontier:
            new_index_of_symbol = index_of_symbol + 1
            if new_index_of_symbol == self.empty_cell:
                self.board[self.empty_cell] = symbol
                self.board[index_of_symbol] = '.'
                self.empty_cell = index_of_symbol
                return True
            else:
                return False
        else:
            return False

    def move(self, symbol):

        if not self.move_down(symbol):
            if not self.move_left(symbol):
                if not self.move_up(symbol):
                    if self.move_right(symbol):
                        return True
                    else:
                        return False

    def  is_solve(self):
        return self.board == self.goal

    def __str__(self):
        result = '--sixteen-- \n'
        cont = 0
        for line in range(4):
            result = result + ' |'
            for c in range(4):
                result = result + self.board[cont] + '|'
                cont += 1
            result = result + '\n'
        return result

try:
    input = sys.argv
    values = input[1]
    values = list(values)
    if len(values) != 16:
        print('no valid input!!')
        exit(1)
    else:
        my_game = sixtenn(values)
except IndexError:
    print('no valid input!!')
    exit(1)

cont = 0

while not my_game.is_solve():
    cont += 1
    symbol = my_game.board[randint(0,15)]
    my_game.move(symbol)
    print(symbol)
    print(cont)
    print(my_game)

# my_game.move('4')
# print(my_game)


