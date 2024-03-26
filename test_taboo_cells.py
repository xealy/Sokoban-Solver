from sokoban import Warehouse

try:
    from fredSokobanSolver import taboo_cells, solve_weighted_sokoban, check_elem_action_seq
    print("Using Fred's solver")
except ModuleNotFoundError:
    from mySokobanSolver import taboo_cells
    print("Using submitted solver")

def test_taboo_cells():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_8a.txt")
    expected_answer = '   ######    \n###XXXXXX### \n#X         X#\n#X          #\n############ '
    answer = taboo_cells(wh)
    fcn = test_taboo_cells    
    print('<<  Testing {} >>'.format(fcn.__name__))
    if answer==expected_answer:
        print(fcn.__name__, ' passed!  :-)\n')
    else:
        print(fcn.__name__, ' failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)

if __name__ == "__main__":   
#    test_warehouse_1() # test Warehouse
#    test_warehouse_2() # test Warehouse
    
#    print(my_team())  # should print your team

    test_taboo_cells() 