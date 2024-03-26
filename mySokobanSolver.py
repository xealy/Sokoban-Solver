
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


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def my_team():
    '''
    Return the list of the team members of this assignment submission as a list
    of triplet of the form (student_number, first_name, last_name)
    
    '''
#    return [ (1234567, 'Ada', 'Lovelace'), (1234568, 'Grace', 'Hopper'), (1234569, 'Eva', 'Tardos') ]
    raise NotImplementedError()

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

    def is_corner(warehouse, r, c, wall=0):
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

        # def inside_warehouse(warehouse):
    #     # know that position of worker in the start must be inside the warehouse
    #     cells_inside_warehouse = []
    #     cells_inside_warehouse.append(warehouse.worker)

    #     # check 

    #     cells_inside_warehouse.sort()
    #     return cells_inside_warehouse
    
    # cells_inside_warehouse = inside_warehouse(warehouse)

    inside_game_set = [warehouse.worker]
    frontier_set = []
    for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0)]:
        #if we hit a wall, we are not inside game as player cannot walk there. 
        if warehouse_list[dy + warehouse.worker[1]][dx + warehouse.worker[0]] != '#':
            frontier_set.append((warehouse.worker[0]+dx, warehouse.worker[1]+dy))
    
    while frontier_set:
        elem = frontier_set.pop(0)
        inside_game_set.append(elem)
        for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0)]:
            if warehouse_list[dy + elem[1]][dx+elem[0]] != '#':
                if ((dx + elem[0], dy + elem[1]) not in inside_game_set \
                and (dx + elem[0], dy + elem[1]) not in frontier_set):
                    frontier_set.append((dx + elem[0],dy + elem[1]))
    #sort the inside_game_set in ascending order by x, then y. 
    inside_game_set.sort()

    '''implementing rule 2'''
    # cell can be target cell, blank cell, wall cell or another taboo cell

    warehouse_list_temp = warehouse_list    
    def make_taboo_cells(warehouse_list_2):
        for (r,c) in inside_game_set:
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
                            only_walls_above = all([cell == '#' for cell in warehouse_list_2[r+1][c-1:c_1+1]])
                                
                            # check only walls below
                            only_walls_below = all([cell == '#' for cell in warehouse_list_2[r-1][c-1:c_1+1]])
                            
                            if only_walls_above or only_walls_below:
                                for c_2 in range(c+1,c_1-1):
                                    warehouse_list_temp[r][c_2] = 'X'
                                break
        

                # check vertically if we have two taboo corner cells with 
                # spaces in between
                empty_cell_count = 0
                for r_1 in range(r+1,len(warehouse_list_2)-1):
                    # if cell in row is a target cell 
                    # all cells in between two taboo corners should not be taboo
                    if warehouse_list_2[r_1][c] in target_cells:
                        break
                    # if we hit a wall cell then the taboo cell was not
                    # a corner cell 
                    elif warehouse_list_2[r_1][c] == '#':
                        break
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
                            only_walls_left = all([cell == '#' for cell in warehouse_list_2[r-1:r_1+1][c-1]])
                                
                            # check only walls on right
                            only_walls_right = all([cell == '#' for cell in warehouse_list_2[r-1:r_1+1][c+1]])
                            
                            if only_walls_left or only_walls_right:
                                for r_2 in range(r+1,r_1-1):
                                    warehouse_list_temp[r_2][c] = 'X'
                                break
        return warehouse_list_temp

    warehouse_list = make_taboo_cells(warehouse_list)
            
    '''Converting warehouse representation back into string format'''
    warehouse_string = ""
    for line in warehouse_list:
        warehouse_string += ''.join(line) + '\n'
    warehouse_string = warehouse_string.rstrip('\n')
    
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
        raise NotImplementedError()

    def actions(self, state):
        """
        Return the list of actions that can be executed in the given state.
        
        """
        raise NotImplementedError

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
               string returned by the method  Warehouse.__str__()
    '''
    
    ##         "INSERT YOUR CODE HERE"
    
    raise NotImplementedError()


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
    
    raise NotImplementedError()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

