from sokoban import Warehouse

try:
    from fredSokobanSolver import taboo_cells, solve_weighted_sokoban, check_elem_action_seq
    print("Using Fred's solver")
except ModuleNotFoundError:
    from mySokobanSolver import check_elem_action_seq
    print("Using submitted solver")

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
    wh.load_warehouse("./warehouses/warehouse_11.txt")
    # first test
    answer = check_elem_action_seq(wh, ['Right', 'Right','Right','Up'])
    expected_answer = 'Impossible'
    print('<<  check_elem_action_seq, test 1>>')
    if answer==expected_answer:
        print('Test 1 passed!  :-)\n')
    else:
        print('Test 1 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
    # second test
    answer = check_elem_action_seq(wh, ['Up','Left','Left', 'Left', 'Down','Down'])
    expected_answer = '  ###### \n  #    # \n  # ## ##\n###@# $ #\n# ..# $ #\n#       #\n#  ######\n####     '
    print('<<  check_elem_action_seq, test 2>>')
    if answer==expected_answer:
        print('Test 2 passed!  :-)\n')
    else:
        print('Test 2 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)

def test_check_elem_action_seq_3():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_61.txt")
    # first test
    answer = check_elem_action_seq(wh, ['Left', 'Down','Down','Up'])
    expected_answer = '######## \n#      # \n# #### # \n# #... # \n# ###@###\n# #     #\n#  $$$$ #\n####   ##\n   #.### \n   ###   '
    print('<<  check_elem_action_seq, test 1>>')
    if answer==expected_answer:
        print('Test 1 passed!  :-)\n')
    else:
        print('Test 1 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
    # second test
    answer = check_elem_action_seq(wh, ['Up','Left','Left', 'Left', 'Down','Down'])
    expected_answer = 'Impossible'
    print('<<  check_elem_action_seq, test 2>>')
    if answer==expected_answer:
        print('Test 2 passed!  :-)\n')
    else:
        print('Test 2 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
    # third test
    answer = check_elem_action_seq(wh, ['Right','Left','Left', 'Left', 'Down','Down'])
    expected_answer = 'Impossible'
    print('<<  check_elem_action_seq, test 2>>')
    if answer==expected_answer:
        print('Test 3 passed!  :-)\n')
    else:
        print('Test 3 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
    # fourth test
    answer = check_elem_action_seq(wh, ['Up', 'Up', 'Left','Left','Left', 'Left', 'Left', 'Down','Down'])
    expected_answer = '######## \n#      # \n# #### # \n#@#... # \n# ###$###\n# #     #\n#  $$ $ #\n####   ##\n   #.### \n   ###   '
    print('<<  check_elem_action_seq, test 2>>')
    if answer==expected_answer:
        print('Test 4 passed!  :-)\n')
    else:
        print('Test 4 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)

def test_check_elem_action_seq_5():
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_151.txt")
    # first test
    answer = check_elem_action_seq(wh, ['Left', 'Up','Up','Left'])
    expected_answer = 'Impossible'
    print('<<  check_elem_action_seq, test 1>>')
    if answer==expected_answer:
        print('Test 1 passed!  :-)\n')
    else:
        print('Test 1 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
    # second test
    answer = check_elem_action_seq(wh, ['Left','Left','Down', 'Left', 'Up','Left','Left','Up','Up','Up','Right','Up','Right','Right','Up','Right','Down'])
    expected_answer = '   ####     \n   #  #     \n ###  #     \n##   @#     \n#   #$#     \n# #$$ ######\n# #$  #   .#\n#         .#\n###  ####..#\n  ####  ####'
    print('<<  check_elem_action_seq, test 2>>')
    if answer==expected_answer:
        print('Test 2 passed!  :-)\n')
    else:
        print('Test 2 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
    # third test
    answer = check_elem_action_seq(wh, ['Down','Left','Left', 'Left', 'Down','Down'])
    expected_answer = 'Impossible'
    print('<<  check_elem_action_seq, test 2>>')
    if answer==expected_answer:
        print('Test 3 passed!  :-)\n')
    else:
        print('Test 3 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)
    # fourth test
    answer = check_elem_action_seq(wh, ['Right', 'Down', 'Right','Right','Right','Right','Right','Right','Down', 'Down', 'Right', 'Right'])
    expected_answer = 'Impossible'
    print('<<  check_elem_action_seq, test 2>>')
    if answer==expected_answer:
        print('Test 4 passed!  :-)\n')
    else:
        print('Test 4 failed!  :-(\n')
        print('Expected ');print(expected_answer)
        print('But, received ');print(answer)

if __name__ == "__main__":
    pass    
#    test_check_elem_action_seq()   #Warehouse 01
#    test_check_elem_action_seq_2() #Warehouse 11
#    test_check_elem_action_seq_3() #Warehouse 61
#    test_check_elem_action_seq_4() #Warehouse 99
#    test_check_elem_action_seq_5() #Warehouse 151