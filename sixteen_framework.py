import copy
import math
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


def manhattan(game):
    dist = 0
    m = copy.deepcopy(game.board)
    for i in range(len(game.goal)):
        sym = m[i]
        goal_cell = game.goal.index(sym)
        dist += distance(i, goal_cell)
    return dist


def not_sorted(game):
    bad = 0
    m = copy.deepcopy(game.board)
    for i in range(len(game.goal)):
        if m[i] != game.goal[i]:
            bad += 1
    return bad

def distance(index_a, index_b):
    # Section A
    floor_a = math.floor(index_a / 4)
    module_a = index_a % 4

    # Section B
    floor_b = math.floor(index_b / 4)
    module_b = index_b % 4
    return abs(floor_a - floor_b) + abs(module_a - module_b)


class Framework:
    def __init__(self, my_object):
        self.s0 = copy.deepcopy(my_object)


    def actions(self, s):
        nb = s.get_neighbor_by_symbol('.')
        new_nb = filter(None, nb)
        return new_nb

    def results(self, s, a):
        if a is not None:
            new_state = copy.deepcopy(s)
            new_state.move(a)
        else:
            new_state = copy.deepcopy(s)
        return new_state

    def goalTest(self, s):
        return s.is_solve()

    def stepCost(self, s, a, s_prime):
        return 1

    def pathCost(self, states):
        return len(states)
        # return 1

    def heuristic(self, list):
        last = list[len(list) - 1]
        # return not_sorted(last)
        return (manhattan(last) + not_sorted(last) )*-1
