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


def heuristic(list):
    last_sudoku = list[len(list) - 1]
    empty_cells = 0
    full_rows = 0
    full_columns = 0
    line_count = 0

    for line in last_sudoku.table:
        if last_sudoku.check_row(line):
            full_rows = full_rows + 1
        if last_sudoku.check_col(last_sudoku.table, line_count):
            full_columns = full_columns +1
        for cell in line:
            if cell == 0:
                empty_cells = empty_cells + 1
        line_count = line_count + 1
    return (full_rows  + full_columns) - empty_cells

def a_star(frontier, problem):
    shortest = []
    for path in frontier:
        if len(shortest) == 0 or problem.pathCost(shortest) + heuristic(shortest) > problem.pathCost(path) + heuristic(path):
            shortest.append(path)
    return shortest


def graph_search(problem):
    frontier = [problem.s0]
    explored = []

    while True:
        if len(frontier):
            path = a_star(frontier, problem)
            s = path[len(path)-1]
            explored.append(path)

            if problem.goalTest(s):
                return path

            for a in problem.actions(s):
                result = problem.results(s, a)
                if all(result.table != a for a in explored):
                    print(explored[0])
                    print("explored", explored)
                    print("result", result.show_table())

                    new_path = []
                    new_path = copy.deepcopy(path)
                    new_path.append(result)
                    frontier.append(new_path)
        else:
            return False

