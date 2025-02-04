# Sokoban Solver

## About
Sokoban is a puzzle game where a player moves boxes around a maze, aiming to place them in specific target locations. Sokoban simulates the behaviour of a robot moving boxes in a warehouse, making it a suitable model for automated planning problems. 

The aim of this project was to task was to write functions with the aim of implementing a solver for the Weighted Sokoban Problem. In the Weighted Sokoban Problem, the goal is that the worker pushes all boxes into target positions with a minimum cost and without making the problem unsolvable by pushing boxes into taboo cells. To summarise the main purpose of the implemented functions:
* **check_elem_action_seq()**: This function is to determine if a given sequence of actions is legal or not based on the worker and its surroundings.
* **taboo_cells()**: This function is designed to identify the taboo cells of a given warehouse. A taboo cell is defined as a cell inside the warehouse that if a box gets pushed into it, it renders the puzzle unsolvable.
* **solve_weighted_sokoban()**: This function analyses a given warehouse and implements A* graph search on the puzzle to find if a solution exists or not.

## How to run
Rough steps:
* Create an instance of the Warehouse class -> wh = Warehouse()
* Load in a warehouse text file -> wh.load_warehouse("path/to/warehouse.txt")
* Run the solve_weighted_sokoban() function -> answer, cost = solve_weighted_sokoban(wh)

You can view/run the test functions in 'sanity_check.py' for examples of how to run.

**NOTE**: You can also run the 'gui_sokoban.py' file and load in a warehouse manually to visualise and play through the game yourself.
