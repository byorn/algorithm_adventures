from collections import deque

the_ground = [[]]


def populate_the_ground():
    global the_ground
    f = open("input.txt", "r")
    rows = []
    for line in f:
        cols = []
        for col in line:
            if col != '\n':
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
            "F": "SE",
            "|": "SN",
            "7": "SW"
        }
        return the_ground.get(symbol)
    if direction == "SOUTH":
        the_ground = {
            "|": "NS",
            "J": "NW",
            "L": "NE"
        }
        return the_ground.get(symbol)
    if direction == "WEST":
        the_ground = {
            "-": "EW",
            "L": "EN",
            "F": "ES"
        }
        return the_ground.get(symbol)


def get_direction(symbol):
    the_ground = {
        "SE": ("SOUTH", "EAST"),
        "WE": ("WEST", "EAST"),
        "NE": ("NORTH", "EAST"),
        "WN": ("WEST", "NORTH"),
        "SN": ("SOUTH", "NORTH"),
        "EN": ("EAST", "NORTH"),
        "WS": ("WEST", "SOUTH"),
        "NS": ("NORTH", "SOUTH"),
        "ES": ("EAST", "SOUTH"),
        "EW": ("EAST", "WEST"),
        "SW": ("SOUTH", "WEST"),
        "NW": ("NORTH", "WEST")
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
    max_rows = len(the_ground) - 1
    max_cols = len(the_ground[0]) - 1
    if direction == "EAST":
        if col < max_cols:
            col += 1
            return the_ground[row][col], row, col
        else:
            return ".", row, max_cols
    if direction == "WEST":
        if col > 0:
            col -= 1
            return the_ground[row][col], row, col
        else:
            return ".", row, 0
    if direction == "NORTH":
        if row > 0:
            row -= 1
            return the_ground[row][col], row, col
        else:
            return ".", 0, col
    if direction == "SOUTH":
        if row < max_rows:
            row += 1
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
    stack = deque()
    stack.append(Node(start_symbol, x, y))

    while len(stack) != 0:
        found = False
        CurrentNode = stack[len(stack) - 1]
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
                return r, c


populate_the_ground()
x, y = find_start()
stack = start_travelling("SE", x, y)


def is_point_inside_polygon(x, y, poly):
    """
    Returns True if the point (x, y) is inside the polygon defined by poly.
    poly is a list of (x, y) tuples representing the vertices of the polygon.
    """
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def mark_cells_inside_polygon(array, poly):
    """
    Marks cells inside the polygon with 'Y' in the given 2D array.
    """
    min_x = min(p[0] for p in poly)
    max_x = max(p[0] for p in poly)
    min_y = min(p[1] for p in poly)
    max_y = max(p[1] for p in poly)

    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            if is_point_inside_polygon(j, i, poly):
                    if array[i][j] == "." or not is_cell_belong_to_polygon(j, i, poly):
                        array[i][j] = 'I'

    return array

def is_cell_belong_to_polygon(x, y, poly):
    for r in range(len(poly) - 1):
        if x == poly[r][0] and y == poly[r][1]:
            return True
    return False


def convert_stack_to_poly(stack):
    poly = []
    while(len(stack) != 0):
        node: Node = stack.pop()
        poly.append((node.y, node.x))
    return poly
#6947
print("answer is: ", len(stack) / 2)

poly = convert_stack_to_poly(stack)

the_ground = mark_cells_inside_polygon(the_ground, poly)

for row in the_ground:
    print(row)


count = 0
for row in the_ground:
    for cell in row:
        if cell == "I":
            count += 1

#print (the_ground)
print("answer is: ", count)
#answer is 273

