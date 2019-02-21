import copy
# state s
'''
Una función actions(s) → {a1,a2 , .., an-1, an}
Una función result(s, a) → s’
Una función goalTest(s) → {True, False}
Una función stepCost(s, a, s’) → R
Una función pathCost(s1, s2 .. , sn) → R , para si = result(si-1, ai)
frontera?
explorados, no explorados
'''

class sudoku_framework:
    def __init__(self, my_object):
        self.s0 = copy.deepcopy(my_object)

    def avaliable(self, s, x, y):
        posible_result = []
        row = s.get_row(x)
        col = s.get_col(y)
        if x < 2:
            if y < 2:
                cuadrant = s.get_cuadrant(0)
            else:
                cuadrant = s.get_cuadrant(1)
        else:
            if y < 2:
                cuadrant = s.get_cuadrant(2)
            else:
                cuadrant = s.get_cuadrant(3)
        for num in range(1, s.dimension + 1):
            if num not in row and num not in col and num not in cuadrant:
                posible_result.append(num)
        return posible_result

    def actions(self, s):
        actions_list = []
        for x in range(s.dimension):
            for y in range(s.dimension):
                if s.table[x][y] == 0:
                    entries = self.avaliable(s, x, y)
                    for n in entries:
                        new_s = copy.deepcopy(s)
                        new_s.table[x][y] = n
                        if new_s not in actions_list:
                            actions_list.append(new_s)
        return actions_list

    def results(self, s, a):
        new_state = a
        return new_state

    def goalTest(self, s):
        return s.is_solve()

    def stepCost(self, s, a, s_prime):
        return 1

    def pathCost(self, states):
        # return len(states)
        return 1

    def heuristic(self, list):
        last_sudoku = list[len(list) - 1]
        empty_cells = 0
        full_cell = 0
        full_cuadrant = 0

        for line in last_sudoku.table:
            for cell in line:
                if cell == 0:
                    empty_cells += 1
                else:
                    full_cell += 1
        return empty_cells - full_cuadrant
