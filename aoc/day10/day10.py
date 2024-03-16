from collections import deque

the_ground = [[]]


def populate_the_ground():
    global the_ground
    f = open("input.txt", "r")
    rows = []
    for line in f:
        cols = []
        for col in line:
            cols.append(col)
        rows.append(cols)
    the_ground = rows

def get_symbol_string(symbol, direction):
    if direction == "EAST":
        the_ground = {
            "J": "WN",
            "-": "WE",
            "7": "WS"
        }
        return the_ground.get(symbol)
    if direction == "NORTH":
        the_ground = {
            "F" : "SE",
            "|" : "SN",
            "7" : "SW"
        }
        return the_ground.get(symbol)
    if direction == "SOUTH":
        the_ground = {
            "|" : "NS",
            "J": "NW",
            "L": "NE"
        }
        return the_ground.get(symbol)
    if direction == "WEST":
        the_ground = {
            "-" : "EW",
            "L" : "EN",
            "F": "ES"
        }
        return the_ground.get(symbol)


def get_direction(symbol):
    the_ground = {
        "SE": ("SOUTH", "EAST"),
        "WE": ("WEST","EAST"),
        "NE": ("NORTH", "EAST"),
        "WN": ("WEST", "NORTH"),
        "SN": ("SOUTH","NORTH"),
        "EN": ("EAST","NORTH"),
        "WS": ("WEST","SOUTH"),
        "NS": ("NORTH","SOUTH"),
        "ES": ("EAST", "SOUTH"),
        "EW": ("EAST", "WEST"),
        "SW": ("SOUTH", "WEST"),
        "NW": ("NORTH","WEST")
    }
    return the_ground.get(symbol)

def is_cell_symbol_valid(direction, symbol):
    if symbol == None:
        return False
    if direction == "EAST":
        return symbol in ["WN", "WE", "WS"]
    if direction == "NORTH":
        return symbol in ["SE", "SN", "SW"]
    if direction == "SOUTH":
        return symbol in ["NS", "NW", "NE"]
    if direction == "WEST":
        return symbol in ["EW", "EN", "ES"]

def get_next_cell_symbol(direction, row, col):
    max_rows = len(the_ground)-1
    max_cols = len(the_ground[0])-1
    if direction == "EAST":
        if col < max_cols:
            col+=1
            return the_ground[row][col], row, col
        else:
            return ".", row, max_cols
    if direction == "WEST":
        if col > 0:
            col-=1
            return the_ground[row][col], row, col
        else:
            return ".", row, 0
    if direction == "NORTH":
        if row > 0:
            row-=1
            return the_ground[row][col], row, col
        else:
            return ".", 0, col
    if direction == "SOUTH":
        if row<max_rows:
            row+=1
            return the_ground[row][col], row, col
        else:
            return ".", max_rows, col

class Node:
    directions: []
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y
    def set_directions(self, next_directions):
        self.directions = next_directions
def start_travelling(start_symbol, x, y):
    directions = ["WEST", "EAST", "SOUTH", "NORTH"]
    stack = deque()
    stack.append(Node(start_symbol, x, y))

    while len(stack) != 0:
        found = False
        CurrentNode = stack[len(stack)-1]
        sdirection, edirection = get_direction(CurrentNode.symbol)
        next_directions = [sdirection, edirection]
        CurrentNode.set_directions(next_directions[:])
        has_direction = False
        while len(CurrentNode.directions) != 0:
            nd = CurrentNode.directions.pop()
            next_symbol, next_x, next_y = get_next_cell_symbol(nd, CurrentNode.x, CurrentNode.y)
            next_symbol_string = get_symbol_string(next_symbol, nd)
            if next_symbol == "S":
               found = True
               break
            if is_cell_symbol_valid(nd, next_symbol_string):
               has_direction = True
               stack.append(Node(next_symbol_string, next_x, next_y))
               break

        if found == False and has_direction == False:
            stack.pop()

        if found:
            break

    return stack

def find_start():
    for r, row in enumerate(the_ground):
        for c, col in enumerate(row):
            if col == "S":
                return (r, c)

populate_the_ground()
x, y = find_start()
stack = start_travelling("SE", x, y)
for s in stack:
    the_ground[s.x][s.y]="#"


#6947
print("answer is: ", len(stack)/2)
for arr in the_ground:
       print(arr)
