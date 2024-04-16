
'''

Quick "sanity check" script to test your submission 'mySokobanSolver.py'

This is not an exhaustive test program. It is only intended to catch major
syntactic blunders!

You should design your own test cases and write your own test functions.

Although a different script (with different inputs) will be used for 
marking your code, make sure that your code runs without errors with this script.


'''


from sokoban import Warehouse
import random, time


try:
    from fredSokobanSolver import my_team, taboo_cells, solve_weighted_sokoban, check_elem_action_seq
    print("Using Fred's solver")
except ModuleNotFoundError:
    from mySokobanSolver import my_team, taboo_cells, solve_weighted_sokoban, check_elem_action_seq
    print("Using submitted solver")

    
def test_taboo_cells():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_01.txt")
    expected_answer = '####  \n#X #  \n#  ###\n#   X#\n#   X#\n#XX###\n####  '
    answer = taboo_cells(wh)
    fcn = test_taboo_cells    
    print('<<  Testing {} >>'.format(fcn.__name__))
    if answer==expected_answer:
        print(fcn.__name__, ' passed!  :-)\n')
    else:
        print(fcn.__name__, ' failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
        
def test_check_elem_action_seq():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_01.txt")
    # first test
    answer = check_elem_action_seq(wh, ['Right', 'Right','Down'])
    expected_answer = '####  \n# .#  \n#  ###\n#*   #\n#  $@#\n#  ###\n####  '
    print('<<  check_elem_action_seq, test 1>>')
    if answer==expected_answer:
        print('Test 1 passed!  :-)\n')
    else:
        print('Test 1 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
    # second test
    answer = check_elem_action_seq(wh, ['Right', 'Right','Right'])
    expected_answer = 'Impossible'
    print('<<  check_elem_action_seq, test 2>>')
    if answer==expected_answer:
        print('Test 2 passed!  :-)\n')
    else:
        print('Test 2 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)

def test_check_elem_action_seq_2():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_01.txt")
    # first test
    answer = check_elem_action_seq(wh, ['Right', 'Right','Down','Left'])
    expected_answer = '####  \n# .#  \n#  ###\n#*   #\n# $@ #\n#  ###\n####  '
    print('<<  check_elem_action_seq, test 1>>')
    if answer==expected_answer:
        print('Test 1 passed!  :-)\n')
    else:
        print('Test 1 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
    # second test
    answer = check_elem_action_seq(wh, ['Right', 'Right','Right'])
    expected_answer = 'Impossible'
    print('<<  check_elem_action_seq, test 2>>')
    if answer==expected_answer:
        print('Test 2 passed!  :-)\n')
    else:
        print('Test 2 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)




def test_solve_weighted_sokoban():
    wh = Warehouse()    
    wh.load_warehouse( "./warehouses/warehouse_8a.txt")
    # first test
    answer, cost = solve_weighted_sokoban(wh)

    expected_answer = ['Up', 'Left', 'Up', 'Left', 'Left', 'Down', 'Left', 
                       'Down', 'Right', 'Right', 'Right', 'Up', 'Up', 'Left', 
                       'Down', 'Right', 'Down', 'Left', 'Left', 'Right', 
                       'Right', 'Right', 'Right', 'Right', 'Right', 'Right'] 
    expected_cost = 431
    print('<<  test_solve_weighted_sokoban >>')
    if answer==expected_answer:
        print(' Answer as expected!  :-)\n')
    else:
        print('unexpected answer!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
        print('Your answer is different but it might still be correct')
        print('Check that you pushed the right box onto the left target!')
    print(f'Your cost = {cost}, expected cost = {expected_cost}')

def test_solve_weighted_sokoban2():
    wh = Warehouse()    
    wh.load_warehouse( "./warehouses/warehouse_09.txt")
    # first test
    print(wh.weights)
    answer, cost = solve_weighted_sokoban(wh)

    expected_answer = ['Up', 'Right', 'Right', 'Down', 'Up', 'Left', 'Left', 'Down', 'Right', 'Down', 'Right', 'Left', 'Up', 'Up', 'Right', 'Down', 'Right', 'Down', 'Down', 'Left', 'Up', 'Right', 'Up', 'Left', 'Down', 'Left', 'Up', 'Right', 'Up', 'Left']
    expected_cost = 396
    print('<<  test_solve_weighted_sokoban >>')
    if answer==expected_answer:
        print(' Answer as expected!  :-)\n')
    else:
        print('unexpected answer!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
        print('Your answer is different but it might still be correct')
        print('Check that you pushed the right box onto the left target!')
    print(f'Your cost = {cost}, expected cost = {expected_cost}')

def test_solve_weighted_sokoban3():
    wh = Warehouse()    
    wh.load_warehouse( "./warehouses/warehouse_147.txt")
    # first test
    answer, cost = solve_weighted_sokoban(wh)

    expected_answer = ['Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Down', 'Down', 'Down', 'Right', 'Right', 'Up', 'Right', 'Down', 'Right', 'Down', 'Down', 'Left', 'Down', 'Left', 'Left', 'Up', 'Up', 'Down', 'Down', 'Right', 'Right', 'Up', 'Right', 'Up', 'Up', 'Left', 'Left', 'Left', 'Down', 'Left', 'Up', 'Up', 'Up', 'Left', 'Up', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Down', 'Right', 'Right', 'Right', 'Up', 'Up', 'Left', 'Left', 'Down', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Down', 'Down', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Left', 'Up', 'Up', 'Left', 'Up', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Left', 'Left', 'Left', 'Left', 'Left', 'Down', 'Down', 'Down', 'Down', 'Right', 'Down', 'Down', 'Right', 'Right', 'Up', 'Up', 'Right', 'Up', 'Left', 'Left', 'Left', 'Down', 'Left', 'Up', 'Up', 'Up', 'Left', 'Up', 'Right', 'Right', 'Right', 'Right', 'Right', 'Down', 'Right', 'Down', 'Right', 'Right', 'Up', 'Left', 'Right', 'Right', 'Up', 'Up', 'Left', 'Left', 'Down', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Down', 'Left', 'Left', 'Up', 'Right', 'Right', 'Down', 'Right', 'Up', 'Left', 'Left', 'Up', 'Left', 'Left']
    expected_cost = 521
    print('<<  test_solve_weighted_sokoban >>')
    if answer==expected_answer:
        print(' Answer as expected!  :-)\n')
    else:
        print('unexpected answer!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
        print('Your answer is different but it might still be correct')
        print('Check that you pushed the right box onto the left target!')
    print(f'Your cost = {cost}, expected cost = {expected_cost}')


def test_solve_weighted_sokoban4():
    wh = Warehouse()    
    wh.load_warehouse( "/Users/alexandraaxcrona/Desktop/CAB320_a1/SokobanSolver/warehouses/warehouse_07.txt")
    # first test
    answer, cost = solve_weighted_sokoban(wh)

    expected_answer = ['Up', 'Up', 'Right', 'Right', 'Up', 'Up', 'Left', 'Left', 'Down', 'Down', 'Right', 'Up', 'Down', 'Right', 'Down', 'Down', 'Left', 'Up', 'Down', 'Left', 'Left', 'Up', 'Left', 'Up', 'Up', 'Right']

    expected_cost = 26
    print('<<  test_solve_weighted_sokoban >>')
    if answer==expected_answer:
        print(' Answer as expected!  :-)\n')
    else:
        print('unexpected answer!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
        print('Your answer is different but it might still be correct')
        print('Check that you pushed the right box onto the left target!')
    print(f'Your cost = {cost}, expected cost = {expected_cost}')
        
def test_solve_weighted_sokoban5():
    wh = Warehouse()    
    wh.load_warehouse( "/Users/alexandraaxcrona/Desktop/CAB320_a1/SokobanSolver/warehouses/warehouse_81.txt")
    # first test
    answer, cost = solve_weighted_sokoban(wh)

    expected_answer = ['Left', 'Up', 'Up', 'Up', 'Right', 'Right', 'Down', 'Left', 'Down', 'Left', 'Down', 'Down', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Left', 'Up', 'Right', 'Up', 'Up', 'Left', 'Left', 'Down', 'Right', 'Up', 'Right', 'Up', 'Right', 'Up', 'Up', 'Left', 'Left', 'Down', 'Down', 'Right', 'Down', 'Down', 'Left', 'Down', 'Down', 'Right', 'Up', 'Up', 'Up', 'Down', 'Left', 'Left', 'Up', 'Right']
    expected_cost = 376
    print('<<  test_solve_weighted_sokoban >>')
    if answer==expected_answer:
        print(' Answer as expected!  :-)\n')
    else:
        print('unexpected answer!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
        print('Your answer is different but it might still be correct')
        print('Check that you pushed the right box onto the left target!')
    print(f'Your cost = {cost}, expected cost = {expected_cost}') 

def test_solve_weighted_sokoban6():
    wh = Warehouse()    
    wh.load_warehouse( "/Users/alexandraaxcrona/Desktop/CAB320_a1/SokobanSolver/warehouses/warehouse_47.txt")
    # first test
    answer, cost = solve_weighted_sokoban(wh)

    expected_answer = ['Right', 'Right', 'Right', 'Up', 'Up', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Left', 'Left', 'Up', 'Up', 'Right', 'Right', 'Up', 'Right', 'Right', 'Right', 'Right', 'Down', 'Left', 'Up', 'Left', 'Down', 'Down', 'Up', 'Up', 'Left', 'Left', 'Down', 'Left', 'Left', 'Down', 'Down', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Down', 'Right', 'Right', 'Up', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Down', 'Left', 'Left', 'Up', 'Up', 'Up', 'Right', 'Right', 'Right', 'Up', 'Right', 'Down', 'Down', 'Up', 'Left', 'Left', 'Left', 'Left', 'Down', 'Down', 'Down', 'Right', 'Right', 'Up', 'Right', 'Right', 'Left', 'Left', 'Down', 'Left', 'Left', 'Up', 'Right', 'Right']
    expected_cost = 179
    print('<<  test_solve_weighted_sokoban >>')
    if answer==expected_answer:
        print(' Answer as expected!  :-)\n')
    else:
        print('unexpected answer!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
        print('Your answer is different but it might still be correct')
        print('Check that you pushed the right box onto the left target!')
    print(f'Your cost = {cost}, expected cost = {expected_cost}') 

def test_solve_weighted_sokoban7():
    wh = Warehouse()    
    wh.load_warehouse( "/Users/alexandraaxcrona/Desktop/CAB320_a1/SokobanSolver/warehouses/warehouse_5n.txt")
    # first test
    answer, cost = solve_weighted_sokoban(wh)

    expected_answer = 'Impossible'
    expected_cost = None
    print('<<  test_solve_weighted_sokoban >>')
    if answer==expected_answer:
        print(' Answer as expected!  :-)\n')
    else:
        print('unexpected answer!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
        print('Your answer is different but it might still be correct')
        print('Check that you pushed the right box onto the left target!')
    print(f'Your cost = {cost}, expected cost = {expected_cost}') 

if __name__ == "__main__":
    pass    
    #print(my_team())
    #test_taboo_cells()
    # test_check_elem_action_seq_2()
    t0 = time.time()
    test_solve_weighted_sokoban4()
    t1 = time.time()
    print(t1-t0)
    # print("Hello")
