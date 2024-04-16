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

def test_taboo_cells_2():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_11.txt")
    expected_answer = '  ###### \n  #XXXX# \n  # ## ##\n### #X X#\n#X  #  X#\n#X     X#\n#XX######\n####     '
    answer = taboo_cells(wh)
    fcn = test_taboo_cells    
    print('<<  Testing {} >>'.format(fcn.__name__))
    if answer==expected_answer:
        print(fcn.__name__, ' passed!  :-)\n')
    else:
        print(fcn.__name__, ' failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)

def test_taboo_cells_3():   # Test taboo cell for Warehouse 01
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
        print('But, received '); print(answer)

def test_taboo_cells_4():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_03_impossible.txt")
    expected_answer = '  ####   \n###XX####\n#X     X#\n#X# ## X#\n#X   #XX#\n#########'
    answer = taboo_cells(wh)
    fcn = test_taboo_cells    
    print('<<  Testing {} >>'.format(fcn.__name__))
    if answer==expected_answer:
        print(fcn.__name__, ' passed!  :-)\n')
    else:
        print(fcn.__name__, ' failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received '); print(answer)

def test_taboo_cells_5():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_03.txt")
    expected_answer = '  ####   \n###XX####\n#X     X#\n#X#  # X#\n#X   #XX#\n#########'
    answer = taboo_cells(wh)
    fcn = test_taboo_cells    
    print('<<  Testing {} >>'.format(fcn.__name__))
    if answer==expected_answer:
        print(fcn.__name__, ' passed!  :-)\n')
    else:
        print(fcn.__name__, ' failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received '); print(answer)

def test_taboo_cells_6():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_6n.txt")
    expected_answer = ' #### #### \n##XX###XX##\n#X  #X#  X#\n#X       X#\n###     ###\n #X     X# \n###     X# \n#X      X# \n#X  #XXX## \n##XX####   \n ####      '
    answer = taboo_cells(wh)
    fcn = test_taboo_cells    
    print('<<  Testing {} >>'.format(fcn.__name__))
    if answer==expected_answer:
        print(fcn.__name__, ' passed!  :-)\n')
    else:
        print(fcn.__name__, ' failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received '); print(answer)

def test_taboo_cells_7():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_17.txt")
    expected_answer = '##### \n#XXX# \n#   # \n#   ##\n#   X#\n#XXXX#\n######'
    answer = taboo_cells(wh)
    fcn = test_taboo_cells    
    print('<<  Testing {} >>'.format(fcn.__name__))
    if answer==expected_answer:
        print(fcn.__name__, ' passed!  :-)\n')
    else:
        print(fcn.__name__, ' failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received '); print(answer)

def test_taboo_cells_8():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_29.txt")
    expected_answer = '     ##### \n     #XXX##\n     #X  X#\n ######X X#\n##XXXXX# X#\n#X       ##\n#X###### # \n#XXXXXXXX# \n########## '
    answer = taboo_cells(wh)
    fcn = test_taboo_cells
    print('<<  Testing {} >>'.format(fcn.__name__))
    if answer==expected_answer:
        print(fcn.__name__, ' passed!  :-)\n')
    else:
        print(fcn.__name__, ' failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received '); print(answer)

def test_taboo_cells_9():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_43.txt")
    expected_answer = '     ####\n     #XX#\n     #  #\n######  #\n#X      #\n#X   #X #\n#X   ####\n###XX#   \n  ####   '
    answer = taboo_cells(wh)
    fcn = test_taboo_cells
    print('<<  Testing {} >>'.format(fcn.__name__))
    if answer==expected_answer:
        print(fcn.__name__, ' passed!  :-)\n')
    else:
        print(fcn.__name__, ' failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received '); print(answer)

def test_taboo_cells_10():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_55.txt")
    expected_answer = '########  \n#XXX#XX#  \n#X     #  \n#####  #  \n    #  ###\n ## #    #\n ## #XX###\n    ####  '
    answer = taboo_cells(wh)
    fcn = test_taboo_cells
    print('<<  Testing {} >>'.format(fcn.__name__))
    if answer==expected_answer:
        print(fcn.__name__, ' passed!  :-)\n')
    else:
        print(fcn.__name__, ' failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received '); print(answer)

def test_taboo_cells_11():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_59.txt")
    expected_answer = '############ \n#XXXXXXXXXX# \n#X#######  ##\n#X#X       X#\n#X#     X#  #\n#X   #####  #\n###XX# #X   #\n  #### #XXXX#\n       ######'
    answer = taboo_cells(wh)
    fcn = test_taboo_cells
    print('<<  Testing {} >>'.format(fcn.__name__))
    if answer==expected_answer:
        print(fcn.__name__, ' passed!  :-)\n')
    else:
        print(fcn.__name__, ' failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received '); print(answer)

if __name__ == "__main__":   
#    test_warehouse_1() # test Warehouse
#    test_warehouse_2() # test Warehouse 


#    print(my_team())  # should print your team

    # test_taboo_cells()  # Test Taboo cells from Warehouse 8a
#    test_taboo_cells_2() # Test Taboo cells from Warehouse 11
#    test_taboo_cells_3() # Test Taboo cells from Warehouse 01
#    test_taboo_cells_4() # Test Taboo cells from Warehouse 03 impossible
   test_taboo_cells_5() # Test Taboo cells from Warehouse 03
#    test_taboo_cells_6() # Test Taboo cells from Warehouse 6n
#    test_taboo_cells_7() # Test Taboo cells from Warehouse 17
#    test_taboo_cells_8() # Test Taboo cells from Warehouse 29
#    test_taboo_cells_9() # Test Taboo cells from Warehouse 43
#    test_taboo_cells_10() # Test Taboo cells from Warehouse 55
#    test_taboo_cells_11() # Test Taboo cells from Warehouse 59