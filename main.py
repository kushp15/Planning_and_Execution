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
                        Helper Methods
'''
###############################################################


def find_fire_neighbors(grid, x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    count = [(nx, ny) for nx, ny in neighbors if 0 <= nx < D and 0 <= ny < D and grid[nx][ny] == "F"]
    return len(count)


def get_neighbors(x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < D and 0 <= ny < D]


def is_valid_move(grid, x, y):
    return 0 <= x < D and 0 <= y < D and grid[x][y] != "#" and grid[x][y] != "F"


def is_valid_move_bot(grid, index, pathF, x, y):
    if index == 1:
        return 0 <= x < D and 0 <= y < D and grid[x][y] != "#" and grid[x][y] != grid[x_fire][y_fire]
    if index == 2:
        for i, j in pathF:
            return 0 <= x < D and 0 <= y < D and grid[x][y] != "#" and grid[x][y] != grid[i][j]


def is_valid_move_bot_2(grid, x, y):
    pass


def calculate_fire_spread_probability(q, K):
    return 1 - (1 - q) ** K


###############################################################
'''
                        FIRE
'''
###############################################################

path_for_fire = {}


def fire(OriginalGrid, index):
    temp_grid = [row.copy() for row in OriginalGrid]

    neighbor_coordinates = []
    valid_neighbor = []
    flamability = []

    # Get the Fire Cells on Grid
    fire_cell = [(x, y) for x in range(D) for y in range(D) if OriginalGrid[x][y] == "F"]

    # path.append((fire_cell,index))
    # print("pp==",path)

    # Get the Fire Neighbors
    for x, y in fire_cell:
        neighbor_coordinates.extend(get_neighbors(x, y))

    # Check they are valid and if the position is itself bot then return None
    for x, y in neighbor_coordinates:
        if is_valid_move(OriginalGrid, x, y):
            valid_neighbor.append((x, y))
            if (x, y) == (x_bot, y_bot):
                return None

    # Remove repeated Cells
    valid_neighbor = list(set(valid_neighbor))

    # iterate in neighbor and get the fire neighbor to see the count of burning neighbor cell
    for x, y in valid_neighbor:
        count = find_fire_neighbors(OriginalGrid, x, y)
        probability = calculate_fire_spread_probability(q, count)
        # flamability.append( ( (x,y),calculate_fire_spread_probability(q,count) ) )
        ran = random.random()
        # print((x, y), ran, probability)
        if ran < probability:
            if OriginalGrid[x][y] != "B":  # OriginalGrid[x][y] != "P" or
                temp_grid[x][y] = "F"
                if index not in path_for_fire:
                    path_for_fire[index] = []
                path_for_fire[index].append((x, y))
                # path_for_fire.append(((x, y), index))
                # print("pp==", path_for_fire)
            else:
                return None

    # for x in temp_grid:
    #     print(' '.join(x))
    # print()
    return temp_grid


# Spread Fire and Store the path Value:
def start_fire():
    time = 0
    tempGrid = [row.copy() for row in grid]
    while True:
        tempGrid = fire(tempGrid, time)
        if tempGrid is None:
            break
        time += 1


# Ignition to Fire
start_fire()

###############################################################
'''
                        BOT - 1 
'''


###############################################################


def find_shortest_path(original_grid, index, fireP, start, end):
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
                if is_valid_move_bot(original_grid, index, fireP, nx, ny):
                    queue.append(((nx, ny), path + [(nx, ny)]))
    return None


def task():
    time = 0
    button_pos = (x_button, y_button)
    bot_pos = (x_bot, y_bot)
    print("bot pos", bot_pos)
    bot_1_grid = [row.copy() for row in grid]
    bot_2_grid = [row.copy() for row in grid]

    FirePath = list(path_for_fire.values())

    # path = find_shortest_path(bot_1_grid,1, bot_pos, button_pos)

    result = list(path_for_fire.values())
    for i, group in enumerate(result):
        print(f"Group {i}: {group}")
    # print("p",path)

    # # For Bot 1
    # while True:
    #     print(len(FirePath))
    #     if (x_button,y_button) == path[0]:
    #         print("Bot reached Button. Bot 1 Won")
    #         break
    #     if len(FirePath) == 0:
    #         print("Fire reached to Button. Bot 1 Loss")
    #         break
    #     if path == []:
    #         print("No path exist for bot 1")
    #         break
    #     if path[0] in FirePath[0]:
    #         print("Fire Caught Bot 1 ")
    #         break
    #     print(time)
    #     print(FirePath.pop(0))
    #     print("pp==", path.pop(0))
    #     time += 1

    # For Bot 2

    # print("p",path)
    time = 0
    FirePath = list(path_for_fire.values())

    while True:
        # print(len(FirePath))

        for x in bot_2_grid:
            print(' '.join(x))
        print()

        f2 = FirePath.pop(0)
        next_fire_cell = f2
        for i, j in next_fire_cell:
            bot_2_grid[i][j] = "F"

        path2 = find_shortest_path(bot_2_grid, 2, next_fire_cell, bot_pos, button_pos)

        p2 = path2.pop(0)

        if (x_button, y_button) == p2:
            print("Bot reached Button. Bot 1 Won")
            break

        print("p2", path2)
        bot_pos = p2
        t, k = bot_pos
        bot_2_grid[t][k] = "P"
        print("pos", bot_pos)

        if len(FirePath) == 0:
            print("Fire reached to Button. Bot 1 Loss")
            break
        if path2 == []:
            print("No path exist for bot 1")
            break
        if p2 in f2:
            print("Fire Caught Bot 1 ")
            break
        print(time)

        # print(FirePath.pop(0))
        # print("pp==", path2.pop(0))
        time += 1


task()

for x in grid:
    print(' '.join(x))
print()
