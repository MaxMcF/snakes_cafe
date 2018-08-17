# snakes_cafe

**Author**: Max McFarland
**Version**: 1.0.0

## Overview
This application allows a user to select items from a pre-built menu, add them to their order, and view the total cost of their meal.

## Getting Started
To run this program, a user must download Python 3.7 and set up a pip virtual environment. After pulling down the application from GitHub, the user must run python3 snakes_cafe.py in their command line. To run any tests, pytest must be downloaded via the pip virtual environment.

## Architecture
This was applicaiton was written in python using VScode. It employs pipenv, as well as pytest.

## API
To use this applicaiton, being by starting your pipenv in your local repo containing the file. Then run the command python3 snakes_cafe.py. This starts the applicaiton.
You can then type in any of the menu items, which then adds them to your "meal".
You can type "quit" at any time to exit out of the program.
Typing any of the menu sections shows only that section of menu items.
Typing "remove" followed by any item added to the menu will remove that item from your order.
The user can add a .csv file to their folder if they want to add an external menu.

## Change Log

08-13-2018 3:30pm - Began adding hard coded strings containing menu items
08-13-2018 4:30pm - Began working on the logic for displaying the menu when the program boots up
08-13-2018 5:00pm - Finished the menu, began working on input logic
08-13-2018 6:00pm - Finished input logic
08-14-2018 4:30pm - Began adding order form logic
08-14-2018 5:30pm - Added extra items to the menu
08-14-2018 4:30pm - fixed decimal problems
08-15-2018 10:00am - Fixed testing, added costs to menu, added more remove functionality
08-15-2018 2:30pm - began refactoring men items to iterate through easier
08-15-2018 6:30pm - finally finished squashing all bugs
08-16-2018 3:30pm - Added logic for importing custom menu
08-16-2018 4:30pm - lots of bugs involved in global variables
08-16-2018 6:30pm - Finished refactoring global variables, testing does not work.
