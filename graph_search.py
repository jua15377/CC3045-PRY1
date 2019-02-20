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
    full_cell = 0
    full_rows = 0
    full_cuadrant = 0
    full_columns = 0
    line_count = 0

    for line in last_sudoku.table:
        if last_sudoku.check_row(line):
            full_rows = full_rows + 1
        if last_sudoku.check_col(last_sudoku.table, line_count):
            full_columns = full_columns + 1
        if last_sudoku.check_cuadrant(last_sudoku.table):
            full_columns = full_columns + 1
        for cell in line:
            if cell == 0:
                empty_cells += 1
            else:
                full_cell = full_cell + 1
        line_count = line_count + 1
    # return (full_rows + full_columns+ full_cell) - empty_cells
    return 3 * empty_cells - 2 * (full_rows + full_cell + full_columns)


def a_star(frontier, problem):
    shortest = frontier[0]
    for path in frontier:
        p_cost = problem.pathCost(shortest)
        h = heuristic(shortest)
        actual = p_cost + h
        new = problem.pathCost(path) + heuristic(path)
        # print('actual', actual, 'new', new)
        if new < actual+1:
            shortest = path
            # print(shortest)
    return shortest


def graph_search(problem):
    frontier = [[problem.s0]]
    explored = []
    count = 0
    while True:
        count = count + 1
        print(count)
        if len(frontier):
            path = a_star(frontier, problem)
            # print("frontier", frontier)
            # print("path", path)
            s = path[len(path)-1]
            explored.append(s)

            if problem.goalTest(s):
                print("SOLVED")
                return path

            for a in problem.actions(s):
                result = problem.results(s, a) #returns a sudoku
                # print(result)
                if result not in explored:
                    # print('explored', explored)
                    new_path = copy.deepcopy(path)
                    new_path.append(result)
                    frontier.append(new_path)
        else:
            return False
    return path
