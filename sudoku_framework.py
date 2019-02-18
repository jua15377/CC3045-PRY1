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

    def actions(self, s):
        actions_list = []
        def avaliable(s, x, y):
            posible_result = []
            row = s.get_row(x)
            col = s.get_col(y)
            if x <2:
                if y < 2:
                    cuadrant = s.get_cuadrant(0)
                else:
                    cuadrant = s.get_cuadrant(2)
            else:
                if y < 2:
                    cuadrant = s.get_cuadrant(1)
                else:
                    cuadrant = s.get_cuadrant(3)
            for num in range(1, s.dimension + 1):
                if num not in row and num not in col and num not in cuadrant:
                    posible_result.append(num)
            return posible_result

        for i in range(0, len(s.dimension)):
            for j in range(0, len(s.dimension)):
                if s[i][j] == 0:
                    entries = avaliable(s, i, j)
                    for n in entries:
                        new_s = copy.deepcopy(s)
                        new_s.table[i][j] = n
                        if  all(new_s.table != action.table for action in actions_list):
                            actions_list.append(new_s)
        return actions_list

    def results(self, s, a):
        pass

    def goalTest(self, s):
        return s.is_solve()

    def stepCost(self, s, a, s_prime):
        pass

    def pathCost(self, states):
        pass
