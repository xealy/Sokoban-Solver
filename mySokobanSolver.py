
'''

    Sokoban assignment


The functions and classes defined in this module will be called by a marker script. 
You should complete the functions and classes according to their specified interfaces.

No partial marks will be awarded for functions that do not meet the specifications
of the interfaces.

You are NOT allowed to change the defined interfaces.
In other words, you must fully adhere to the specifications of the 
functions, their arguments and returned values.
Changing the interfacce of a function will likely result in a fail 
for the test of your code. This is not negotiable! 

You have to make sure that your code works with the files provided 
(search.py and sokoban.py) as your code will be tested 
with the original copies of these files. 

Last modified by 2022-03-27  by f.maire@qut.edu.au
- clarifiy some comments, rename some functions
  (and hopefully didn't introduce any bug!)

'''

# You have to make sure that your code works with 
# the files provided (search.py and sokoban.py) as your code will be tested 
# with these files
import search 
import sokoban
import math


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def my_team():
    '''
    Return the list of the team members of this assignment submission as a list
    of triplet of the form (student_number, first_name, last_name)
    
    '''
    return [(10494588, 'Alexandra', 'Chua Rossiter'), (11941472, 'Alexandra', 'Axcrona'), (11925230, 'Belen', 'Sogo Mielgo')]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def taboo_cells(warehouse):
    '''  
    Identify the taboo cells of a warehouse. A "taboo cell" is by definition
    a cell inside a warehouse such that whenever a box get pushed on such 
    a cell then the puzzle becomes unsolvable. 
    
    Cells outside the warehouse are not taboo. It is a fail to tag an 
    outside cell as taboo.
    
    When determining the taboo cells, you must ignore all the existing boxes, 
    only consider the walls and the target  cells.  
    Use only the following rules to determine the taboo cells;
     Rule 1: if a cell is a corner and not a target, then it is a taboo cell.
     Rule 2: all the cells between two corners along a wall are taboo if none of 
             these cells is a target.
    
    @param warehouse: 
        a Warehouse object with the worker inside the warehouse

    @return
       A string representing the warehouse with only the wall cells marked with 
       a '#' and the taboo cells marked with a 'X'.  
       The returned string should NOT have marks for the worker, the targets,
       and the boxes.  
    '''
    ##         "INSERT YOUR CODE HERE"    
    # lists of cell types useful for later
    target_cells = ['!', '.', '*']
    cells_to_remove = ['@', '$']
    
    '''Convert the warehouse to an array consisting of each of the separate rows for convenience
    and replace the player cells and box cells (but not target cells) with blank cells
    '''
    warehouse_string = str(warehouse)
    for cell in cells_to_remove:
        warehouse_string = warehouse_string.replace(cell,' ')

    warehouse_list = []
    for row in warehouse_string.split('\n'):
        warehouse_list.append(list(row))


    '''
    Cell is a corner if there are one or more wall cells above OR below 
    AND one or more wall cells to the left OR right
    But remember that cell also has to be INSIDE for it to be taboo
    '''

    def is_corner(warehouse, r, c):
        nr_walls_left_right = 0
        nr_walls_up_down = 0

        '''Checking for walls left and right'''
        if warehouse[r][c + 1] == '#':
            nr_walls_left_right += 1 
        if warehouse[r][c - 1] == '#':
            nr_walls_left_right += 1 

        '''Checking for walls up and down'''
        if warehouse[r + 1][c] == '#':
                nr_walls_up_down += 1 
        if warehouse[r - 1][c] == '#':
                nr_walls_up_down += 1 

        if (nr_walls_left_right >= 1 and nr_walls_up_down >= 1):
            return True
        else:
            return False

    '''implementing rule 1'''
    for r in range(len(warehouse_list)-1):
        inside_warehouse = False
        for c in range(len(warehouse_list[0])-1):
            if not inside_warehouse:
                if warehouse_list[r][c] == '#':
                    inside_warehouse = True
            else:
                all_empty = True
                for cell in warehouse_list[r][c:]:
                    if cell != ' ':
                        all_empty = False
                        break
                if all_empty:
                    break

                cell = warehouse_list[r][c]
                if cell not in target_cells:
                    if cell != '#':
                        if is_corner(warehouse_list, r, c):
                            warehouse_list[r][c] = 'X'

        def inside_warehouse(warehouse, warehouse_list):
            # know that position of worker in the start must be inside the warehouse
            cells_inside_warehouse = []
            worker = tuple_swap(warehouse.worker)
            cells_inside_warehouse.append(worker)
            boundary = []
            
            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            for d in directions:
                if warehouse_list[worker[0] + d[0]][worker[1] + d[1]] != '#':
                    boundary.append((worker[0] + d[0],worker[1] + d[1]))

            while len(boundary) != 0:
                inside = boundary.pop(0)
                cells_inside_warehouse.append(inside)
                for d in directions:
                    if warehouse_list[inside[0] + d[0]][inside[1] + d[1]] != '#':
                        if (inside[0] + d[0], inside[1] + d[1]) not in boundary:
                            if (inside[0] + d[0], inside[1] + d[1]) not in cells_inside_warehouse:
                                boundary.append((inside[0] + d[0], inside[1] + d[1]))
            return cells_inside_warehouse
    
    cells_inside_warehouse = inside_warehouse(warehouse, warehouse_list)


    '''implementing rule 2'''
    # cell can be target cell, blank cell, wall cell or another taboo cell
    warehouse_list_temp = warehouse_list
    def implement_rule_2(warehouse_list_2):
        for (r,c) in cells_inside_warehouse:
            # iterate over all cells inside the warehouse
            # only cells inside the warehouse can become taboo cells
            if warehouse_list_2[r][c] == 'X':
                # check horisontally if we have two taboo corner cells with 
                # spaces in between
                empty_cell_count = 0
                for c_1 in range(c+1,len(warehouse_list_2[0])-1):
                    # if cell in row is a target cell 
                    # all cells in between two taboo corners should not be taboo
                    if warehouse_list_2[r][c_1] in target_cells:
                        break
                    # if we hit a wall cell then the taboo cell was not
                    # a corner cell 
                    elif warehouse_list_2[r][c_1] == '#':
                        break
                    elif warehouse_list_2[r][c_1] == ' ':
                        empty_cell_count += 1
                        continue
                    elif warehouse_list_2[r][c_1] == 'X':
                        if empty_cell_count != 0:
                            # Check if there is wall on the columns directly either up or down
                            # of the column containing the taboo cells, between the two taboo cells.
                            # Must be at least one empty cell between the two taboo cells in order to 
                            # add taboo cells between them.

                            # check only walls above
                            only_walls_above = all([cell == '#' for cell in warehouse_list_2[r+1][c:c_1]])
                                
                            # check only walls below
                            only_walls_below = all([cell == '#' for cell in warehouse_list_2[r-1][c:c_1]])
                            
                            if only_walls_above or only_walls_below:
                                for c_2 in range(c+1,c_1):
                                    warehouse_list_temp[r][c_2] = 'X'
                                break
        

                # check vertically if we have two taboo corner cells with 
                # spaces in between
                empty_cell_count = 0
                for r_1 in range(r+1,len(warehouse_list_2)-1):
                    # print((r, r_1, c))

                    # if cell in row is a target cell 
                    # all cells in between two taboo corners should not be taboo
                    if warehouse_list_2[r_1][c] in target_cells:
                        break
                    # if we hit a wall cell then the taboo cell was not
                    # a corner cell or all cells between should not be taboo
                    elif warehouse_list_2[r_1][c] == '#':
                        break
                    # if we hit an empty cell, we could be along a wall between two taboo cells
                    # so want to continue searching
                    elif warehouse_list_2[r_1][c] == ' ':
                        empty_cell_count += 1
                        continue
                    elif warehouse_list_2[r_1][c] == 'X':
                        if empty_cell_count != 0:
                            # Check if there is wall on the columns directly either the left or right
                            # of the column containing the taboo cells, between the two taboo cells.
                            # Must be at least one empty cell between the two taboo cells in order to 
                            # add taboo cells between them.

                            # check only walls on left
                            only_walls_left = True
                            for r_2 in range(r,r_1):
                                if warehouse_list_2[r_2][c-1] != '#':
                                    only_walls_left = False
                                
                            # check only walls on right
                            only_walls_right = True
                            for r_3 in range(r,r_1):
                                if warehouse_list_2[r_3][c+1] != '#':
                                    only_walls_right = False
                            
                            if only_walls_left or only_walls_right:
                                for r_4 in range(r+1,r_1):
                                    warehouse_list_temp[r_4][c] = 'X'
                                break
        return warehouse_list_temp

    warehouse_list = implement_rule_2(warehouse_list)
            
    # Converting warehouse representation back into string format
    warehouse_string = ""
    for line in warehouse_list:
        warehouse_string += ''.join(line) + '\n'
    warehouse_string = warehouse_string.rstrip('\n')
    
    # now remove target cells
    for cell in target_cells:
        warehouse_string = warehouse_string.replace(cell, ' ')
    
    return warehouse_string

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class SokobanPuzzle(search.Problem):
    '''
    An instance of the class 'SokobanPuzzle' represents a Sokoban puzzle.
    An instance contains information about the walls, the targets, the boxes
    and the worker.

    Your implementation should be fully compatible with the search functions of 
    the provided module 'search.py'. 
    
    '''
    
    #
    #         "INSERT YOUR CODE HERE"
    #
    #     Revisit the sliding puzzle and the pancake puzzle for inspiration!
    #
    #     Note that you will need to add several functions to 
    #     complete this class. For example, a 'result' method is needed
    #     to satisfy the interface of 'search.Problem'.
    #
    #     You are allowed (and encouraged) to use auxiliary functions and classes

    
    def __init__(self, warehouse):
        self.warehouse = warehouse
        self.worker = tuple(warehouse.worker)
        self.boxes = tuple(warehouse.boxes)
        self.targets = tuple(warehouse.targets)
        self.walls = warehouse.walls
        self.weights = warehouse.weights

        self.initial = (self.worker, self.boxes)

        self.goal = self.targets
        
        temp_warehouse_taboo_check = taboo_cells(warehouse)
        warehouse_list_taboo_check = []
        for row in temp_warehouse_taboo_check.split('\n'):
            warehouse_list_taboo_check.append(list(row))

        self.taboo_cells = warehouse_list_taboo_check

        


    def actions(self, state):
        """
        Return the list of actions that can be executed in the given state.
        
        """

        valid_actions = ['Left', 'Right', 'Up', 'Down']
        action_mapping = {'Left': (-1,0), 'Right': (1,0), 'Up': (0,-1), 'Down': (0,1)}

        # temp_warehouse =self.warehouse.copy(state[0], state.boxes[:], self.warehouse.weights)
        temp_warehouse = self.warehouse.copy(state[0], state[1], self.warehouse.weights)
        x, y = state[0]


        # print(warehouse_list_taboo_check)

        L = []  # list of legal actions
        for action in valid_actions:
            x_new_worker, y_new_worker = x+action_mapping[action][0], y+action_mapping[action][1]
            x_new_box, y_new_box = x_new_worker+action_mapping[action][0], y_new_worker+action_mapping[action][1]
            
            # temp_worker_pos = tuple_swap((x_new_worker, y_new_worker))
            # temp_box_pos = tuple_swap((x_new_box, y_new_box))

            # print(warehouse_list_taboo_check[temp_box_pos[0]][temp_box_pos[1]])


            if (x_new_worker, y_new_worker) not in temp_warehouse.walls:
                if (x_new_worker, y_new_worker) in temp_warehouse.boxes: # if new coordinates are a box
                    if self.taboo_cells[y_new_box][x_new_box] != 'X':
                        if (x_new_box, y_new_box) not in temp_warehouse.walls and (x_new_box, y_new_box) not in temp_warehouse.boxes:
                            L.append(action)
                else:
                    L.append(action)

        return L
    
    def result(self, state, action):
        assert action in self.actions(state)  # defensive programming

        action_mapping = {'Left': (-1,0), 'Right': (1,0), 'Up': (0,-1), 'Down': (0,1)}
        boxes = list(state[1])

        # action_list = [action]
        # new_warehouse = check_elem_action_seq(self.warehouse, action_list) 
        # new_warehouse = self.warehouse.from_string(new_warehouse) # check if this is correct

        # return (new_warehouse.worker, tuple(new_warehouse.boxes))

        worker_position = add_tuples(state[0], action_mapping[action])
        if worker_position in boxes:
            box_position = add_tuples(worker_position, action_mapping[action])
            worker_index = boxes.index(worker_position)
            boxes.pop(worker_index)
            boxes.insert(worker_index, box_position)
        else:
            # if box not moved, return new position of worker 
            return (worker_position, tuple(boxes))
        
        return (worker_position, tuple(boxes))
    

    def goal_test(self, state):
        goal_reached = True
        for box in state[1]:
            if box not in self.goal:
                goal_reached = False
        return goal_reached
        

    def path_cost(self, c, state1, action, state2):
        boxes1 = list(state1[1])
        boxes2 = list(state2[1])

        # state 1 -> (action) -> state 2
        if self.weights:
            # cost of moving box
            idx = None
            for i in range(len(boxes1)):
                if boxes1[i] != boxes2[i]:
                    idx = i # get the index of that box
                    break
            if idx != None:
                # enters here if box has changed position from state1 to state2, this means box is moved
                # get the corresponding weight of that box
                # cost of moving box
                weight = self.weights[idx]
                c += weight
            # cost of moving worker
            c += 1
        else:
            # boxes don't have weights, so cost of moving (even if you also move a box) is only cost of moving worker
            c += 1
        # return the total path cost
        return c


    def h(self, n):
        return heuristic_function(self,n)
        # return 0
        

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def check_elem_action_seq(warehouse, action_seq):
    '''
    Determine if the sequence of actions listed in 'action_seq' is legal or not.
    
    Important notes:
      - a legal sequence of actions does not necessarily solve the puzzle.
      - an action is legal even if it pushes a box onto a taboo cell.
        
    @param warehouse: a valid Warehouse object

    @param action_seq: a sequence of legal actions.
           For example, ['Left', 'Down', Down','Right', 'Up', 'Down']
           
    @return
        The string 'Impossible', if one of the action was not valid.
           For example, if the agent tries to push two boxes at the same time,
                        or push a box into a wall.
        Otherwise, if all actions were successful, return                 
               A string representing the state of the puzzle after applying
               the sequence of actions.  This must be the same string as the
               string returned by the method Warehouse.__str__()
    '''
    ##         "INSERT YOUR CODE HERE"
    

    valid_actions = ['Left', 'Right', 'Up', 'Down']
    action_mapping = {'Left': (-1,0), 'Right': (1,0), 'Up': (0,-1), 'Down': (0,1)}

    # Get location of Worker (warehouse.worker)
    temp_warehouse =warehouse.copy(warehouse.worker, warehouse.boxes[:], warehouse.weights)
    x, y = temp_warehouse.worker
    impossible_string = 'Impossible'

    # if there are no actions in the list, return the warehouse unchanged 
    if len(action_seq) == 0:
        print('Nothing')
        return temp_warehouse.__str__()

    # loop through each action in action_seq to check if valid
    for action in action_seq:

        # Impossible if action is not valid
        if action not in valid_actions:
            return impossible_string
    
        print(action)
        x_new_worker, y_new_worker = x+action_mapping[action][0], y+action_mapping[action][1]
        x_new_box, y_new_box = x_new_worker+action_mapping[action][0], y_new_worker+action_mapping[action][1]

        if (x_new_worker, y_new_worker) in temp_warehouse.walls: # if new coordinates are a wall
            return impossible_string # Failed: player is blocked
            
        if (x_new_worker, y_new_worker) in temp_warehouse.boxes: # if new coordinates are a box
            if (x_new_box, y_new_box) not in temp_warehouse.walls and (x_new_box, y_new_box) not in temp_warehouse.boxes: # if box is pushed into wall or another box, illegal action
                temp_warehouse.boxes.remove((x_new_worker, y_new_worker))
                temp_warehouse.boxes.append((x_new_box, y_new_box))
                y = y_new_worker # Successful: can move the worker + box, update with new y coordinate
                x = x_new_worker # Successful: can move the worker + box, update with new x coordinate
            else:
                return impossible_string # Failed: box is blocked, either pushed box into a wall or into another box
        else: 
            y = y_new_worker 
            x = x_new_worker   
    
    # Update worker location at the end of action sequence (with latest location)
    temp_warehouse.worker = x, y

    return temp_warehouse.__str__()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def solve_weighted_sokoban(warehouse):
    '''
    This function analyses the given warehouse.
    It returns the two items. The first item is an action sequence solution. 
    The second item is the total cost of this action sequence.
    
    @param 
     warehouse: a valid Warehouse object

    @return
    
        If puzzle cannot be solved 
            return 'Impossible', None
        
        If a solution was found, 
            return S, C 
            where S is a list of actions that solves
            the given puzzle coded with 'Left', 'Right', 'Up', 'Down'
            For example, ['Left', 'Down', Down','Right', 'Up', 'Down']
            If the puzzle is already in a goal state, simply return []
            C is the total cost of the action sequence C

    '''


    sokoban_puzzle = SokobanPuzzle(warehouse)

    # returns a node object if there is a solution and None if there is not
    solution_sokoban_puzzle = search.astar_graph_search(sokoban_puzzle)
    print(solution_sokoban_puzzle)

    if solution_sokoban_puzzle:
        S = solution_sokoban_puzzle.solution()
        C = solution_sokoban_puzzle.path_cost 
    else:
        return 'Impossible', None
    
    return S, C


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def tuple_swap(tup):
    return (tup[1], tup[0])

def add_tuples(tup1, tup2):
    a,b = tup1[0], tup1[1]
    c,d = tup2[0], tup2[1]
    return (a+c,b+d)

# def move_tuple_left(tup):
#     return add_tuples(tup, (-1,0))

# def move_tuple_right(tup):
#     return add_tuples(tup, (1,0))

# def move_tuple_up(tup):
#     return add_tuples(tup, (0,-1))

# def move_tuple_down(tup):
#     return add_tuples(tup, (0,1))

def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def heuristic_function(self, n):
    """
    Heuristic function is manhattan distance between the boxes and the targets.
    Each of the manhattan distances is multiplied by the box weights.
    Add the shortest manhattan distance between the worker and the closest box.
    """
    # total value returned by the heuristic function
    h_n = 0

    # boxes
    boxes = list(n.state[1])

    # weights
    weights = list(self.weights)

    # targets
    targets = list(self.goal)

    # need to check that the number of boxes equals the number of targets
    assert len(boxes) == len(targets)

    # Compute the shortest distance between each box and its corresponding target
    for box in boxes:
        minimum_distance = float('inf')  # initialize with infinity
        for target in targets:
            distance = abs(box[0] - target[0]) + abs(box[1] - target[1]) # Manhattan distance
            if distance < minimum_distance:
                minimum_distance = distance
        # multiply by the weight value
        idx = boxes.index(box)
        weight = weights[idx]
        h_n += minimum_distance # add the shortest distance to the total heuristic value

    # worker position
    worker = n.state[0]

    # Add the shortest euclidean distance between the worker and the closest box
    #minimum_worker_box_distance = min([math.sqrt((box[0] - worker[0])**2 + (box[1] - worker[1])**2) for box in boxes])
    #h_n += minimum_worker_box_distance

    return h_n




