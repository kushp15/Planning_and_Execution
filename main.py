import random
from collections import deque

# Bock - #
# Open - O
# Bot - P
# Button - B
# Fire - F

D = 5
q = 0.9
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
                deadEndCells.append((randIntX,randIntY))   # for each dead end pick a coordinate to open at random and store in list


# shuffle the list and open 50% of the dead end cells
random.shuffle(deadEndCells) #[(8, 4), (9, 5), (3, 7)]
print("deadendsCells", deadEndCells)
for i in range(int(len(deadEndCells)/2)):
    x,y = deadEndCells[i]
    grid[x][y] = "O"



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


# Find the Position for The Fire Cell
def fire_open_start_position():
    position = random.randint(0, len(openGrid) - 1)
    a, b = openGrid[position]
    openGrid.pop(position)
    grid[a][b] = "F"
    print((a, b))
    # grid[a][b + 1] = "F"
    # grid[a+1][b] = "F"
    # print(a, b, position, grid[a][b], len(queue))
    return a, b


# Initialize Fire
x_fire, y_fire = fire_open_start_position()
fire_pos = (x_fire, y_fire)


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


def is_valid_move_bot(grid, index, pathF, neighborFP, x, y):
    # if index == 1 then for Bot 1
    if index == 1:
        return 0 <= x < D and 0 <= y < D and grid[x][y] != "#" and grid[x][y] != grid[x_fire][y_fire]
    # if index == 2 then for Bot 2
    if index == 2:
        return 0 <= x < D and 0 <= y < D and grid[x][y] != "#" and not((x,y) in pathF)
    # if index == 2 then for Bot 3
    if index == 3:
        return 0 <= x < D and 0 <= y < D and grid[x][y] != "#" and not((x,y) in pathF) and not((x,y) in neighborFP)


def calculate_fire_spread_probability(q, K):
    return 1- (1 - q) ** K


###############################################################
'''
                        FIRE
'''
###############################################################

path_for_fire = {}
path_for_fire[0] = [(x_fire, y_fire)]
neighbors_for_fire = {}
probility_for_bot4 = {}


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
            if index not in neighbors_for_fire:
                neighbors_for_fire[index] = []
            neighbors_for_fire[index].append((x, y))
            # if (x, y) == (x_bot, y_bot):
            #     return None

    # Remove repeated Cells
    valid_neighbor = list(set(valid_neighbor))

    # iterate in neighbor and get the fire neighbor to see the count of burning neighbor cell
    for x, y in valid_neighbor:
        count = find_fire_neighbors(OriginalGrid, x, y)
        probability = calculate_fire_spread_probability(q, count)
        # print(probability)
        # if index not in probility_for_bot4:
        #     probility_for_bot4[index] = []
        # probility_for_bot4[index].append(probability)
        # flamability.append( ( (x,y),calculate_fire_spread_probability(q,count) ) )
        ran = random.random()
        print((x, y), ran, probability)
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
    time = 1
    tempGrid = [row.copy() for row in grid]
    while True:
        tempGrid = fire(tempGrid, time)
        if tempGrid is None:
            break
        time += 1


# Ignition to Fire
start_fire()

result = list(path_for_fire.values())
for i, group in enumerate(result):
    print(f"Group {i}: {group}")
print()
print()
result = list(neighbors_for_fire.values())
for i, group in enumerate(result):
    print(f"Group {i}: {group}")
print()
result = list(probility_for_bot4.values())
for i, group in enumerate(result):
    print(f"Group {i}: {group}")
###############################################################
'''
                        BOT - 1 
'''


###############################################################


def find_shortest_path(original_grid, index, fireP, neighborP,  start, end):
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
                if is_valid_move_bot(original_grid, index, fireP,neighborP, nx, ny):
                    queue.append(((nx, ny), path + [(nx, ny)]))
    return None


def task():
    time = 0
    button_pos = (x_button, y_button)
    bot_pos = (x_bot, y_bot)
    print("bot pos", bot_pos)
    bot_1_grid = [row.copy() for row in grid]
    bot_2_grid = [row.copy() for row in grid]
    bot_3_grid = [row.copy() for row in grid]

    FirePath = list(path_for_fire.values())

    print("***********************************************************")
    print("Bot 1")
    print("***********************************************************")
    initialFireCell = [(x_fire, y_fire)]
    neighborP = initialFireCell
    path = find_shortest_path(bot_1_grid, 1, initialFireCell, neighborP, bot_pos, button_pos)
    print("Main Path", path)
    p1 = bot_pos
    # For Bot 1
    while True:
        for x in bot_1_grid:
            print(' '.join(x))
        print()
        # print(time)
        # print("p",path)
        if time > 0:
            if path is None or path == []:
                print("No path exist for bot 1")
                break
            else:
                p1 = path[0]
            path.pop(0)

        bot_pos = p1
        t, k = bot_pos
        # print(bot_pos)
        bot_1_grid[t][k] = "P"
        # print("Curr pos", bot_pos)

        if (x_button, y_button) == p1:
            print("Bot reached Button. Bot 1 Won")
            break
        if len(FirePath) == 0:
            print("Fire reached to Button. Bot 1 Loss")
            break

        next_fire_cell = FirePath[0]

        for i, j in next_fire_cell:
            bot_1_grid[i][j] = "F"
            initialFireCell.append((i, j))

        if p1 in initialFireCell:
            print("Fire Caught Bot 1 ")
            break

        FirePath.pop(0)
        time += 1
    print(time)
    print("***********************************************************")
    print("Bot 2")
    print("***********************************************************")
    # For Bot 2
    neighborP = initialFireCell
    # print("p",path)
    time = 0
    FirePath = list(path_for_fire.values())
    current_fire_cell = [(x_fire, y_fire)]
    # path2 = []
    p2 = (x_bot, y_bot)
    while True:
        # for x in bot_2_grid:
        #     print(' '.join(x))
        # print()
        # print(time)
        # Initialize the path from time = 1
        # At time t = 0 initialize the bot as per instruction
        if time > 0:
            path2 = find_shortest_path(bot_2_grid, 2, current_fire_cell, neighborP, bot_pos, button_pos)
            # print("p2", path2)
            if path2 is None or path2 == []:
                print("No path exist for bot 2")
                break
            else:
                p2 = path2[0]
            path2.pop(0)
        if (x_button, y_button) == p2:
            print("Bot reached Button. Bot 2 Won")
            break

        bot_pos = p2
        t, k = bot_pos
        bot_2_grid[t][k] = "P"
        # print("pos", bot_pos)

        if len(FirePath) == 0:
            print("Fire reached to Button. Bot 2 Loss")
            break
        f2 = FirePath[0]
        next_fire_cell = f2

        for i, j in next_fire_cell:
            bot_2_grid[i][j] = "F"
            current_fire_cell.append((i, j))
        # print(p2)
        if p2 in current_fire_cell:
            print("Fire Caught Bot 2 ")
            break
        FirePath.pop(0)
        time += 1
    print(time)

    print("***********************************************************")
    print("Bot 3")
    print("***********************************************************")
    # For Bot 3
    time = 0
    FirePath = list(path_for_fire.values())
    neighborP = list(neighbors_for_fire.values())
    neighbor = neighborP[0]
    current_fire_cell = [(x_fire, y_fire)]
    # path2 = []
    p3 = (x_bot, y_bot)
    bot_pos = p3
    # print("p3=", p3)

    while True:
        # for x in bot_3_grid:
        #     print(' '.join(x))
        # print()
        # print(time)
        # Initialize the path from time = 1
        # At time t = 0 initialize the bot as per instruction
        # print(bot_pos)
        # print("fire cell==",current_fire_cell)
        # print("neighbor==",neighbor)
        if time > 0:
            path3 = find_shortest_path(bot_3_grid, 3, current_fire_cell, neighbor, bot_pos, button_pos)

            # print("O==", path3)
            # print("p2", path2)
            if path3 is None or path3 == []:
                path3 = find_shortest_path(bot_3_grid, 2, current_fire_cell, neighbor, bot_pos, button_pos)
                # print("N==", path3)
                if path3 is None or path3 == []:
                    print("No path exist for bot 3")
                    break
            if path3 is not None or path3 != []:
                p3 = path3[0]
            path3.pop(0)

        if (x_button, y_button) == p3:
            print("Bot reached Button. Bot 3 Won")
            break

        bot_pos = p3
        t, k = bot_pos
        bot_3_grid[t][k] = "P"
        # print("pos", bot_pos)

        f3 = FirePath[0]
        next_fire_cell = f3

        for i, j in next_fire_cell:
            bot_3_grid[i][j] = "F"
            current_fire_cell.append((i, j))
            list(set(current_fire_cell))
        # print(p3)
        if p3 in current_fire_cell:
            print("Fire Caught Bot 3 ")
            break

        FirePath.pop(0)
        if len(FirePath) == 0:
            print("Fire reached to Button. Bot 3 Loss")
            break
        if len(neighborP) != 0:
            neighbor = neighborP.pop(0)
            #print("Neighbor",neighbor)
        else:
            break
        time += 1
    print(time)

task()

# for x in grid:
#     print(' '.join(x))
# print()
