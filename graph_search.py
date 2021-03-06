'''
def graph_search(problem):
    frontier = [Path([problem.initial])]
    explored = []

    while True:
        if len(frontier):
            path = criteria(frontier)
            s = path.end
            explored.append(path)

            if problem.goal_test(s):
                return path

            for a in problem.actions(s):
                result = problem.result(s, a)

                if not is_explored(path, result, explored):
                    new_path = Path([])
                    new_path.extendFrom(path)
                    new_path.addStep(problem.result(s, a))
                    frontier.append(new_path)
        else:
            return Falss
'''
import copy


def a_star(frontier, framw_work):
    shortest = frontier[0]
    for path in frontier:
        p_cost = framw_work.pathCost(shortest)
        h = framw_work.heuristic(shortest)
        actual = p_cost + h
        new = framw_work.pathCost(path) + framw_work.heuristic(path)
        if new < actual:
            shortest = path
    return shortest


def graph_search(framw_work):
    frontier = [[framw_work.s0]]
    explored = []
    count = 0
    while True:
        count = count + 1
        if count > 500:
            print('can\'t get the answer, sorry!\n so far i get:\n')
            return path
        if len(frontier):
            path = a_star(frontier, framw_work)
            # print("frontier", frontier)
            # print("path", path)
            s = copy.deepcopy(path[len(path)-1])
            explored.append(s)

            if framw_work.goalTest(s):
                print("SOLVED")
                return path

            for a in framw_work.actions(s):
                result = framw_work.results(s, a)
                if result not in explored:
                    new_path = copy.deepcopy(path)
                    new_path.append(result)
                    frontier.append(new_path)
        else:
            return False
