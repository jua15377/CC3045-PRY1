import copy
from sixteen import Sixteen
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
    distance = 0
    assert isinstance(game, Sixteen)
    m = copy.deepcopy(game.board)
    for i in range(len(game.goal)):
        sym = m[i]
        goal_cell = game.goal.index(sym)
        dist = abs(i - goal_cell)
        distance += dist
    return distance


def not_sorted(game):
    bad = 0
    assert isinstance(game, Sixteen)
    m = copy.deepcopy(game.board)
    for i in range(len(game.goal)):
        if m[i] != game.goal[i]:
            bad += 1
    return bad



class Sixteen_framework:
    def __init__(self, my_object):
        self.s0 = copy.deepcopy(my_object)

    def actions(self, s):
        assert isinstance(s, Sixteen)
        nb =  s.get_neighbor_by_symbol('.')
        return nb

    def results(self, s, a):
        assert isinstance(s, Sixteen)
        if a is not None:
            new_state = copy.deepcopy(s)
            new_state.move(a)
        return new_state

    def goalTest(self, s):
        return s.is_solve()

    def stepCost(self, s, a, s_prime):
        return 1

    def pathCost(self, states):
        return len(states)
        # return 1
