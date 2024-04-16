
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

    # lists of target cells and cells we need to remove
    target_cells = ['!', '.', '*']
    cells_to_remove = ['@', '$']
    
    # convert the warehouse to an array consisting of each of the separate rows 
    # and replace the worker and boxes (but not target cells) with blank cells
    # this will be used throughout the implementation of rule 1 and 2
    
    warehouse_string = str(warehouse)
    for cell in cells_to_remove:
        warehouse_string = warehouse_string.replace(cell,' ')

    warehouse_list = []
    for row in warehouse_string.split('\n'):
        warehouse_list.append(list(row))

    # get a list of all positions INSIDE the warehouse
    cells_inside_warehouse = get_inside_warehouse_cells(warehouse, warehouse_list)

    # rule 1
    # iterate over each position inside the warehouse
    for position in cells_inside_warehouse:
        r = position[0]
        c = position[1]
        # check that position is not a target cell and is a corner
        if warehouse_list[r][c] not in target_cells and check_corner(warehouse_list, r, c) == True:
            # if so, mark as a taboo cell
            warehouse_list[r][c] = 'X'


    # create copy of warehouse list representation for comparison
    warehouse_list_temp = warehouse_list.copy()

    # rule 2

    # iterate over all cells inside the warehouse
    # only cells inside the warehouse can become taboo cells
    for (r,c) in cells_inside_warehouse:
        # found a taboo cell
        if warehouse_list[r][c] == 'X':
            # check horisontally if we have two taboo corner cells with 
            # spaces in between
            # need empty cell count later to check if there are spaces between two taboo corners
            empty_cell_count = 0
            # check after current position and onwards
            for c_1 in range(c+1,len(warehouse_list[0])-1):
                # if cell in row is a target cell 
                # all cells in between two taboo corners should not be taboo
                # do not need to continue
                if warehouse_list[r][c_1] in target_cells:
                    break
                # if the cell is not inside the warehouse do not continue
                elif (r,c_1) not in cells_inside_warehouse:
                    break
                # if we hit a wall cell do not continue
                elif warehouse_list[r][c_1] == '#':
                    break
                # if we hit a blank cell, increment the empty cell counter and continue checking
                elif warehouse_list[r][c_1] == ' ':
                    empty_cell_count += 1
                    continue
                # if we hit another taboo cell
                elif warehouse_list[r][c_1] == 'X':
                    # if there are empty cells between the two taboo cells
                    if empty_cell_count != 0:
                        # check that all cells either above or below row containing the two taboo cells
                        # are only walls

                        # check only walls above
                        only_walls_above = True
                        for cell in warehouse_list[r+1][c:c_1]:
                            if cell != '#':
                                only_walls_above = False
                                break

                        # check only walls below
                        only_walls_below = True
                        for cell in warehouse_list[r-1][c:c_1]:
                            if cell != '#':
                                only_walls_below = False
                                break
                        
                        # if there are only walls either above or below
                        if only_walls_above or only_walls_below:
                            # add taboo cells between the two taboo corners
                            for c_2 in range(c+1,c_1):
                                warehouse_list_temp[r][c_2] = 'X'
                            break
    

            # check vertically if we have two taboo corner cells with only spaces in between
            # set blank space counter back to 0 
            empty_cell_count = 0
            for r_1 in range(r+1,len(warehouse_list)-1):
                # if cell in between two taboo corners is target cell
                # then all cells in between two taboo corners should not be taboo
                if warehouse_list[r_1][c] in target_cells:
                    break
                # if we meet a cell not inside the warehouse it cannot be a 
                # taboo cell, do not continue
                elif (r_1,c) not in cells_inside_warehouse:
                    break
                # if we hit a wall cell, do not continue
                elif warehouse_list[r_1][c] == '#':
                    break
                # if we hit an empty cell, increment empty cell counter
                # and continue checking for another potential taboo cell
                elif warehouse_list[r_1][c] == ' ':
                    empty_cell_count += 1
                    continue
                # we have hit another taboo cell
                elif warehouse_list[r_1][c] == 'X':
                    # check that there is at least one blank between the two taboo cells
                    if empty_cell_count != 0:
                        # check that column to the left or right of the one containing 
                        # the two taboo cells is only walls

                        # check only walls on left
                        only_walls_left = True
                        for r_2 in range(r,r_1):
                            if warehouse_list[r_2][c-1] != '#':
                                only_walls_left = False
                            
                        # check only walls on right
                        only_walls_right = True
                        for r_3 in range(r,r_1):
                            if warehouse_list[r_3][c+1] != '#':
                                only_walls_right = False
                        
                        # if there are only walls on the left and right of the column 
                        # containing the two taboo cells, then mark the spaces between
                        # the taboo corners as taboo cells
                        if only_walls_left or only_walls_right:
                            for r_4 in range(r+1,r_1):
                                warehouse_list_temp[r_4][c] = 'X'
                            break
    
    warehouse_list = warehouse_list_temp
            
    # converting warehouse list back into string format
    warehouse_string = ""
    for line in warehouse_list:
        warehouse_string += ''.join(line) + '\n'
    warehouse_string = warehouse_string.rstrip('\n')
    
    # now remove target cells
    for cell in target_cells:
        warehouse_string = warehouse_string.replace(cell, ' ')

    # return string representation of the warehouse
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
    #     Revisit the sliding puzzle and the pancake puzzle for inspiration!
    #
    #     Note that you will need to add several functions to 
    #     complete this class. For example, a 'result' method is needed
    #     to satisfy the interface of 'search.Problem'.
    #
    #     You are allowed (and encouraged) to use auxiliary functions and classes

    '''
    The state representation of the puzzle is a tuple consisting of the position of the worker as a tuple
    and the boxes as a tuple of tuples. The positions are (x,y) coordinates (x <-> columns, y <-> rows).

    The possible actions are represented by strings: 'Left', 'Right', 'Up', 'Down'
    and their respective direction mappings are: (-1,0), (1,0), (0,-1), (0,1).
    '''

    
    def __init__(self, warehouse):
        """
        This constructor specifies the current puzzle's warehouse attributes, as well as
        the initial state and the goal conditions of the puzzle. Here, the taboo cells 
        in the puzzle are also initialised and set as an attribute. 

        @param warehouse: 
            Warehouse instance

        @return
            Nothing.
        """
        self.warehouse = warehouse
        self.targets = warehouse.targets
        self.walls = warehouse.walls
        self.weights = warehouse.weights

        # this is the initial state
        self.initial = (warehouse.worker, tuple(warehouse.boxes))

        # this is the target position of the goals
        self.goal = self.targets
        
        # initialise a list with overview of the taboo cells
        temp_warehouse_taboo_check = taboo_cells(warehouse)
        warehouse_list_taboo_check = []
        for row in temp_warehouse_taboo_check.split('\n'):
            warehouse_list_taboo_check.append(list(row))

        # make this an attribute so that it can be used later without repetition 
        self.taboo_cells = warehouse_list_taboo_check


    def actions(self, state):
        """
        This function takes the current state of the Sokoban puzzle, and checks how many actions
        from the full set of actions that can be executed by the worker (moving Left, Right, Up
        or Down) are legal based on the obstacles around a worker, and the box it may be pushing.

        @param state: 
            The current state, containing the current position of the worker and the boxes,
            represented by a tuple of tuples.

        @return
            Returns a list of legal actions that can be executed by the worker in the given state.
        """

        valid_actions = ['Left', 'Right', 'Up', 'Down']
        action_mapping = {'Left': (-1,0), 'Right': (1,0), 'Up': (0,-1), 'Down': (0,1)}

        # get the box positions
        boxes = state[1]
        # get the worker position
        x, y = state[0]

        # list of legal actions
        L = []  
        # test if each possible action is valid or not
        for action in valid_actions:
            # new position of worker after action is taken
            x_new_worker, y_new_worker = x+action_mapping[action][0], y+action_mapping[action][1]
            # new position of box after action is taken
            x_new_box, y_new_box = x_new_worker+action_mapping[action][0], y_new_worker+action_mapping[action][1]

            # check that worker is not moving into a wall 
            if (x_new_worker, y_new_worker) not in self.walls:
                # if new coordinates are a box
                if (x_new_worker, y_new_worker) in boxes: 
                    # check that box is not moved into a taboo cell
                    if self.taboo_cells[y_new_box][x_new_box] != 'X':
                        # checks that the box is not pushed into a wall or another box
                        if (x_new_box, y_new_box) not in self.walls and (x_new_box, y_new_box) not in boxes:
                            # add this action as a legal action
                            L.append(action)
                else:
                    # add this action as a legal action
                    L.append(action)

        # return the list of legal actions for this state
        return L
    
    
    def result(self, state, action):
        '''
        This function takes singular legal action, changes the worker's position based on 
        that action. If the worker's new position lands on a box, change the position of the box
        to reflect that it has been pushed. 

        @param state: 
            The current state, containing the current position of the worker and the boxes,
            represented by a tuple of tuples.
        @ param action:
            A string presenting a single action for the worker to take (either Left, Right,
            Up or Down).

        @return
            A tuple of tuples representing the the new state of the puzzle after the action
            has been applied. The new state contains the new position of the worker, and
            the new positions of the boxes.
        '''
         
        assert action in self.actions(state)  # defensive programming

        action_mapping = {'Left': (-1,0), 'Right': (1,0), 'Up': (0,-1), 'Down': (0,1)}
        # list of box positions
        boxes = list(state[1])

        # get current position of the worker
        current_worker_position = state[0]
        # find position worker is in after action is taken
        new_worker_position = (current_worker_position[0] + action_mapping[action][0], current_worker_position[1] + action_mapping[action][1])
        # check if worker moves into a box
        if new_worker_position in boxes:
            # find the new position of the box
            box_position = (new_worker_position[0] + action_mapping[action][0], new_worker_position[1] + action_mapping[action][1])
            # add new position of the box to the list of boxes
            # but retain the order of the boxes
            # so that the boxes still correspond to the correct weights
            idx = boxes.index(new_worker_position)
            boxes.pop(idx)
            boxes.insert(idx, box_position)
        # worker does not move into a box
        else:
            # if box not moved, return new position of worker
            boxes = tuple(boxes) 
            return (new_worker_position, boxes)
        
        boxes = tuple(boxes)
        # return the new state
        return (new_worker_position, boxes)
    

    def goal_test(self, state):
        """
        This function takes the current state of the puzzle, and iterates through the box positions
        to check if they all are located at a target goal. If there is even one box that is not
        in a target goal position, then the function returns that the goal state hasn't been reached.

        @param state: 
            The current state, containing the current position of the worker and the boxes,
            represented by a tuple of tuples.

        @ return
            A boolean value that returns True if the goal state has been reached, and False if
            it has not.
        """
        goal_reached = True
        for box in state[1]:
            # if any box is not in a target goal position, we have not yet reached the goal state
            if box not in self.goal:
                goal_reached = False
        return goal_reached
        

    def path_cost(self, c, state1, action, state2):
        """
        This function returns the cost c of a solution path that goes from state1 to state2 including the cost
        of also arriving at state1. Only one action is taken to get from state1 to state2. Therefore, the cost
        of this action is either the sum of the cost of moving the worker and the box (if a box is moved) or 
        just the cost of moving the worker (if a box is not moved).

        @ param c
            An integer variable that stores the path cost as a path is being explored.
        @ param state1
            A tuple of tuples containing the current state of the Sokoban puzzle.
        @ param action
            A string representing the action taken to arrive at state2 from state1 (This
            parameter is unused).
        @ param state2
            A tuple of tuples containing the prospective state of the Sokoban puzzle
            that is to be explored.

        @ return
            The total path cost accumulated up until state2.
        """
        # make lists of the box positions in the state before action is taken and after action is taken
        boxes1 = list(state1[1])
        boxes2 = list(state2[1])

        # state 1 -> (action) -> state 2
        # case if the boxes have weights
        if self.weights:
            # calculate the cost of moving a box
            idx = None
            for i in range(len(boxes1)):
                # if a box has changed position from state1 to state2
                if boxes1[i] != boxes2[i]:
                    idx = i # get the index of that box
                    # only one box can move after an action is taken
                    # so break out of loop if that box is found
                    break
            if idx != None:
                # enters here if box has changed position from state1 to state2, this means box is moved
                # get the corresponding weight of that box
                weight = self.weights[idx]
                # add the cost of moving the box
                c += weight
            # cost of moving worker
            c += 1
        # case if the boxes do not have weights
        else:
            # boxes don't have weights, so cost of moving (even if you also move a box) is only cost of moving worker
            c += 1
        # return the total current path cost up to state2
        return c


    def h(self, n):
        """
        Heuristic function is the sum of two things:
        1. The smallest manhattan distance between each box and any target multiplied by the weight of the box.
        If the weight of a box is 0, then the smallest manhattan distance between the box and a target is NOT multiplied by 0.
        2. The manhattan distance for the worker to reach the nearest box. This is given by the Manhattan distance
        between the worker and its closest box minus the value of 1. We subtract 1 from the manhattan distance between the worker 
        and the nearest box as we want to find the distance to get the worker next to the box. 

        @param n: Node representing the current state.
            
        @return
        The value of the heuristic function.

        """
        # total value returned by the heuristic function
        h_n = 0

        # list of the box coordinates
        boxes = list(n.state[1])

        # list of the weights
        # if there are no weights, assign a weight of 0 to each of the boxes
        if self.weights == None:
            weights = [0] * len(boxes)
        else:
            weights = list(self.weights)

        # list of the target coordinates
        targets = list(self.goal)

        # need to check that the number of boxes equals the number of targets - defensive programming
        assert len(boxes) == len(targets)

        # store minimum manhattan distance from each box to a target
        minimum_distances = []
        for box in boxes:
            minimum_distance = min(abs(box[0] - target[0]) + abs(box[1] - target[1]) for target in targets)
            minimum_distances.append(minimum_distance)

        # find corresponding weight of each box
        # multiply this by the minimum manhattan distance of that box to a target
        # and add this to the heuristic value 
        for idx in range(len(boxes)):
            # if the weight is 0 
            if weights[idx] == 0:
               h_n += minimum_distances[idx]
            else:
                h_n += (minimum_distances[idx] * weights[idx])

        # worker position
        worker = n.state[0]

        # Add the shortest manhattan distance between the worker and the closest box minus 1
        minimum_worker_box_distance = min([abs(box[0] - worker[0]) + abs(box[1] - worker[1]) for box in boxes])
        h_n += (minimum_worker_box_distance - 1)
    
        return h_n
        

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
    # list of valid actions
    valid_actions = ['Left', 'Right', 'Up', 'Down']
    # maps action to the relevant tuple representing the action
    action_mapping = {'Left': (-1,0), 'Right': (1,0), 'Up': (0,-1), 'Down': (0,1)}

    # make a shallow copy of the warehouse so that we do not change it 
    temp_warehouse = warehouse.copy(warehouse.worker, warehouse.boxes[:], warehouse.weights[:])
    # get location of the worker
    x, y = temp_warehouse.worker
    impossible_string = 'Impossible'

    # if there are no actions in the list, return the warehouse unchanged 
    if len(action_seq) == 0:
        return temp_warehouse.__str__()

    # loop through each action in action_seq to check if valid
    for action in action_seq:

        # Impossible if action is not valid
        if action not in valid_actions:
            return impossible_string
    
        x_new_worker, y_new_worker = x+action_mapping[action][0], y+action_mapping[action][1]
        x_new_box, y_new_box = x_new_worker+action_mapping[action][0], y_new_worker+action_mapping[action][1]

        if (x_new_worker, y_new_worker) in temp_warehouse.walls: # if new coordinates are a wall
            return impossible_string # Failed: worker is blocked
            
        if (x_new_worker, y_new_worker) in temp_warehouse.boxes: # if new coordinates are a box
            if (x_new_box, y_new_box) not in temp_warehouse.boxes and (x_new_box, y_new_box) not in temp_warehouse.walls: # if box is pushed into wall or another box, illegal action
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

    # return string version of the warehouse
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

    # initialise an instance of sokoban puzzle class with given warehouse
    sokoban_puzzle = SokobanPuzzle(warehouse)

    # returns a node object if there is a solution and None if there is not
    # using A* graph search to find a potential solution
    solution_sokoban_puzzle = search.astar_graph_search(sokoban_puzzle)

    # if the search algorithm returns a solution
    if solution_sokoban_puzzle:
        # get a list of actions that solves the puzzle using function from Node class
        S = solution_sokoban_puzzle.solution()
        # get the total path cost using attribute from Node class
        C = solution_sokoban_puzzle.path_cost 
    else:
        # there is no solution
        return 'Impossible', None
    # return list of actions to solve puzzle and total cost
    return S, C


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def check_corner(warehouse_list, r, c):
    '''
    This function checks if position (r,c) is a corner (r <-> rows, c <-> columns).
    If there is at least one wall cell to the left or right of the position we are checking and
    at least one wall cell above and below the position we are checking then the position is a
    corner.

    @param warehouse_list: a list representation of the warehouse
    @param r: row coordinate 
    @param c: column coordinate

    @return
    A boolean True or False. True if the position checked (r,c) is a corner cell and False if not.  

    '''
    
    nr_walls_left_right = 0
    nr_walls_up_down = 0

    # checking for walls left and right
    if warehouse_list[r][c + 1] == '#':
        nr_walls_left_right += 1 
    if warehouse_list[r][c - 1] == '#':
        nr_walls_left_right += 1 

    # checking for walls up and down
    if warehouse_list[r + 1][c] == '#':
        nr_walls_up_down += 1 
    if warehouse_list[r - 1][c] == '#':
        nr_walls_up_down += 1 

    # if there is at least one wall left or right AND above or below then
    # the cell we are checking is a corner cell
    if (nr_walls_left_right >= 1 and nr_walls_up_down >= 1):
        return True
    else:
        return False

def tuple_swap(tup):
    '''
    Swaps positions of elements in a tuple with two elements.

    @param tup: a tuple

    @return
    A tuple with coordinates swapped

    '''
    return (tup[1], tup[0])
    
def get_inside_warehouse_cells(warehouse, warehouse_list):
    '''
    This function finds the positions of all the cells inside the warehouse.

    @param warehouse: instance of a warehouse
    @param warehouse_list: a list representation of the warehouse

    @return
    A list of the position tuples with all positions inside the warehouse.
    All positions are coordinates (r,c) (r <-> rows, c <-> columns)

    '''
    # it is given that position of worker in the start must be inside the warehouse
    cells_inside_warehouse = []
    # swap position of coordinates around just to make it easier to follow when using to index list later on
    worker = tuple_swap(warehouse.worker)
    cells_inside_warehouse.append(worker)
    boundary = []
    
    # list of tuples with all possible directions
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    # checks all directions around the worker 
    # if position is not a wall, add coordinate to the boundary list
    for d in directions:
        if warehouse_list[worker[0] + d[0]][worker[1] + d[1]] != '#':
            boundary.append((worker[0] + d[0],worker[1] + d[1]))

    # while there are still cells to be explored
    while len(boundary) != 0:
        # get the next cell in the boundary list that we know is inside the warehouse
        inside_cell = boundary.pop(0)
        # add this to list of cells we know are inside the warehouse
        cells_inside_warehouse.append(inside_cell)
        # now expand this cell
        for d in directions:
            if warehouse_list[inside_cell[0] + d[0]][inside_cell[1] + d[1]] != '#':
                # if cell is already in the boundary, do not add it again (will be explored)
                if (inside_cell[0] + d[0], inside_cell[1] + d[1]) not in boundary:
                    # if cell is not already in list of cells we know are inside the warehouse
                    if (inside_cell[0] + d[0], inside_cell[1] + d[1]) not in cells_inside_warehouse:
                        # add it to the boundary list
                        boundary.append((inside_cell[0] + d[0], inside_cell[1] + d[1]))
    # return complete list with cells we know are inside the warehouse
    return cells_inside_warehouse












