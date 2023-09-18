import random
from collections import deque

# Bock - #
# Open - O
# Bot - P
# Button - B
# Fire - F

D = 10
q = 0.2
grid = [["#" for _ in range(D)] for _ in range(D)]
openBlockPosArr = []
deadEndCells = []
openGrid = []

randIntX = random.randint(1, D - 2)
randIntY = random.randint(1, D - 2)
grid[randIntX][randIntY] = "O"
openBlockPosArr.append((randIntX, randIntY))

effX1 = randIntX - 1
effX2 = randIntX + 1
effY1 = randIntY - 1
effY2 = randIntY + 1

# debug info
# print("picked: " + "(" + str(randIntX) + ", " + str(randIntY) + ")")


while openBlockPosArr:
    openBlockPosArr = []
    for x in range(effX1, effX2 + 1):
        for y in range(effY1, effY2 + 1):
            openBlockPos = 0
            if grid[x][y] == "#":
                a = x + 1
                b = x - 1
                c = y + 1
                d = y - 1
                if a <= effX2 and grid[a][y] == "O":
                    openBlockPos += 1
                if b >= effX1 and grid[b][y] == "O":
                    openBlockPos += 1
                if c <= effY2 and grid[x][c] == "O":
                    openBlockPos += 1
                if d >= effY1 and grid[x][d] == "O":
                    openBlockPos += 1
                if openBlockPos == 1:
                    openBlockPosArr.append((x, y))
    if openBlockPosArr:

        # debug info
        # print()
        # print(openBlockPosArr)
        # print()

        randIndex = random.randint(0, len(openBlockPosArr) - 1)
        randIntX, randIntY = openBlockPosArr[randIndex]
        grid[randIntX][randIntY] = "O"

        if 0 < effX1 == randIntX:
            effX1 = randIntX - 1
        if D - 1 > effX2 == randIntX:
            effX2 = randIntX + 1
        if 0 < effY1 == randIntY:
            effY1 = randIntY - 1
        if D - 1 > effY2 == randIntY:
            effY2 = randIntY + 1

        # debug info
        # print()
        # for x in grid:
        #     print(' '.join(x))
        # print()

for x in range(D):
    for y in range(D):
        deadEndBlock = 0
        deadEndBlockArr = []
        if grid[x][y] == "O":
            a = x + 1
            b = x - 1
            c = y + 1
            d = y - 1
            if 0 <= a <= D - 1 and grid[a][y] == "#":
                deadEndBlock += 1
                deadEndBlockArr.append((a, y))
            if 0 <= b <= D - 1 and grid[b][y] == "#":
                deadEndBlock += 1
                deadEndBlockArr.append((b, y))
            if 0 <= c <= D - 1 and grid[x][c] == "#":
                deadEndBlock += 1
                deadEndBlockArr.append((x, c))
            if 0 <= d <= D - 1 and grid[x][d] == "#":
                deadEndBlock += 1
                deadEndBlockArr.append((x, d))
            if deadEndBlock >= 3:
                randIndex = random.randint(0, len(deadEndBlockArr) - 1)
                randIntX, randIntY = deadEndBlockArr[randIndex]
                grid[randIntX][randIntY] = "O"

####################################################
'''
    INITIALIZE BOT, BUTTON, AND FIRE POSITION
'''
####################################################

# Appending Open Cell to OpenGrid List
for x in range(D):
    for y in range(D):
        if grid[x][y] == "O":
            openGrid.append((x, y))


# Find the Position for the Bot Cell
def bot_open_start_position():
    position = random.randint(0, len(openGrid) - 1)
    a, b = openGrid[position]
    openGrid.pop(position)
    grid[a][b] = "P"
    # print(a, b, position, grid[a][b], len(queue))
    return a, b


# Initialize Bot
x_bot, y_bot = bot_open_start_position()
bot_pos = (x_bot, y_bot)


# Find the Position for The Button Cell
def button_open_position():
    position = random.randint(0, len(openGrid) - 1)
    a, b = openGrid[position]
    openGrid.pop(position)
    grid[a][b] = "B"
    # print(a, b, position, grid[a][b], len(queue))
    return a, b


# Initialize Button
x_button, y_button = button_open_position()
button_pos = (x_button, y_button)


# Find the Position for The Fire Cell
def fire_open_start_position():
    position = random.randint(0, len(openGrid) - 1)
    a, b = openGrid[position]
    openGrid.pop(position)
    grid[a][b] = "F"
    # print(a, b, position, grid[a][b], len(queue))
    return a, b


# Initialize Fire
x_fire, y_fire = fire_open_start_position()
fire_pos = (x_fire, y_fire)

###############################################################
'''
                        FIRE
'''
###############################################################


def find_side_neighbors_for_fire(x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < D and 0 <= ny < D and grid[nx][ny] == "O"]


def find_fire_neighbors(x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    count = [(nx, ny) for nx, ny in neighbors if 0 <= nx < D and 0 <= ny < D and grid[nx][ny] == "F"]
    return len(count)


def fire(OriginalGrid):
    # create new grid
    temp_grid = [row.copy() for row in OriginalGrid]
    flammability = []
    valid_fire_neighbors = []
    fire_cell = [(x, y) for x in range(D) for y in range(D) if OriginalGrid[x][y] == "F"]
    for x, y in fire_cell:
        # check if the directions are Valid or not with size constraint
        valid_fire_neighbors.extend(find_side_neighbors_for_fire(x, y))
    # print(valid_fire_neighbors)
    valid_fire_neighbors = list(set(valid_fire_neighbors))
    # print(valid_fire_neighbors)

    # Get the probability for each neighbor
    if valid_fire_neighbors:
        for x, y in valid_fire_neighbors:
            count = find_fire_neighbors(x, y)
            if count:
                # print(count)
                flammability.append(1 - pow(1 - q, count))
                total = sum(flammability)
                probability = [value / total for value in flammability]

        # print('valid==', valid_fire_neighbors)
        # print('flame==', flammability)
        # print('proba==', probability)
    return temp_grid


###############################################################
'''
                        BOT - 1 
'''
###############################################################


def get_neighbors(x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < D and 0 <= ny < D]


def is_valid_move(grid, x, y):
    return 0 <= x < D and 0 <= y < D and grid[x][y] != "#"


def find_shortest_path(original_grid, start, end):
    queue = deque([(start, [])])

    visited = set()

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        if (x, y) not in visited:
            visited.add((x, y))
            # print(visited)
            for nx, ny in get_neighbors(x, y):
                if is_valid_move(original_grid, nx, ny):
                    queue.append(((nx, ny), path + [(nx, ny)]))
    return None


def task_bot_1():
    time = 0
    bot_pos = (x_bot, y_bot)
    button_pos = (x_button, y_button)

    bot_1_grid = [row.copy() for row in grid]

    path = find_shortest_path(grid, bot_pos, button_pos)
    print("path==", path)
    while True:

        if bot_pos == button_pos:
            print("Bot 1 reached to button. Bot-1 Win!")
            break

        if path:
            path.pop(0)
            bot_next_pos = path[0]
            bot_1_grid[bot_pos[0]][bot_pos[1]] = "P"
            bot_pos = bot_next_pos
            bot_1_grid[bot_pos[0]][bot_pos[1]] = "P"
        else:
            print("No Path Found")

        fire_grid = fire(bot_1_grid)

        if fire_grid is None:
            print("Fire Got Bot -1.. You Lost! ")
            break

        time += 1

    for x in fire_grid:
        print(' '.join(x))
    print()


# def task_bot_2():
#     time = 0
#     bot_pos = (x_bot, y_bot)
#     button_pos = (x_button, y_button)
#
#     bot_2_grid = [row.copy() for row in grid]
#
#     while True:
#
#         if bot_pos == button_pos:
#             print("Bot 2 reached to button. Bot-2 Win!")
#             break
#         path = find_shortest_path(grid, bot_pos, button_pos)
#         if path:
#             path.pop(0)
#             bot_next_pos = path[0]
#             bot_2_grid[bot_pos[0]][bot_pos[1]] = "O"
#             bot_pos = bot_next_pos
#             bot_2_grid[bot_pos[0]][bot_pos[1]] = "P"
#         else:
#             print("No Path Found")
#
#         fire_grid = fire(bot_2_grid)
#
#         if fire_grid is None:
#             print("Fire Got Bot - 2.. You Lost! ")
#             break
#
#         time += 1
#
#     for x in fire_grid:
#         print(' '.join(x))
#     print()


task_bot_1()
# task_bot_2()
for x in grid:
    print(' '.join(x))
print()
