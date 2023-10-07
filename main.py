import math
import random
from collections import deque

# Bock - #
# Open - O
# Bot - P
# Button - B
# Fire - F

D = 20
q = 0.6
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
                deadEndCells.append(
                    (randIntX, randIntY))  # for each dead end pick a coordinate to open at random and store in list

# shuffle the list and open 50% of the dead end cells
random.shuffle(deadEndCells)  # [(8, 4), (9, 5), (3, 7)]
print("deadendsCells", deadEndCells)
for i in range(int(len(deadEndCells) / 2)):
    x, y = deadEndCells[i]
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

# grid = [
#     ["O", "O", "#", "O", "P", "O", "#", "#", "O", "O"],
#     ["#", "O", "O", "#", "#", "O", "O", "#", "O", "O"],
#     ["O", "O", "O", "#", "#", "O", "#", "O", "O", "O"],
#     ["#", "O", "O", "#", "O", "O", "O", "O", "O", "O"],
#     ["O", "O", "F", "O", "#", "O", "#", "#", "O", "O"],
#     ["#", "O", "O", "O", "O", "O", "O", "#", "O", "O"],
#     ["#", "O", "#", "O", "#", "O", "#", "O", "O", "O"],
#     ["O", "O", "#", "#", "O", "O", "O", "O", "O", "#"],
#     ["#", "#", "O", "#", "#", "B", "#", "O", "O", "#"],
#     ["O", "O", "O", "O", "O", "O", "O", "#", "O", "O"]
# ]
#
# bot_pos = (0,4)
# x_bot, y_bot = bot_pos
# button_pos = (8,5)
# x_button, y_button = button_pos
# fire_pos = (4,2)
# x_fire, y_fire = fire_pos

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

def get_neighbors_bot4(grid, x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < D and 0 <= ny < D and grid[nx][ny] != "#"]

def is_valid_move(grid, x, y):
    return 0 <= x < D and 0 <= y < D and grid[x][y] != "#" and grid[x][y] != "F"


def is_valid_move_bot(grid, index, pathF, neighborFP, x, y):
    # if index == 1 then for Bot 1
    if index == 1:
        return 0 <= x < D and 0 <= y < D and grid[x][y] != "#" and grid[x][y] != grid[x_fire][y_fire]
    # if index == 2 then for Bot 2
    if index == 2:
        return 0 <= x < D and 0 <= y < D and grid[x][y] != "#" and not ((x, y) in pathF)
    # if index == 2 then for Bot 3
    if index == 3:
        return 0 <= x < D and 0 <= y < D and grid[x][y] != "#" and not ((x, y) in pathF) and not ((x, y) in neighborFP)


def calculate_fire_spread_probability(q, K):
    return 1 - (1 - q) ** K


# 1 - (1-0.2) ** 2 = 1 - (0.8)^2 = 0.36
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
        if index not in probility_for_bot4:
            probility_for_bot4[index] = []
        probility_for_bot4[index].append(((x,y), probability))
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

# Helper Method
def is_outer_fire(grid, x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for nx, ny in neighbors:
        if 0 <= nx < D and 0 <= ny < D and grid[nx][ny] == "O":
            return True
    return False

# Method for Outer Fire
def outer_fire_cells(originalGrid):
    outer_fire_cells = []

    # Step 1: Get all the fire cells of the originalGrid
    fire_cells = [(i, j) for i in range(D) for j in range(D) if originalGrid[i][j] == "F"]

    for x,y in fire_cells:
        if is_outer_fire(originalGrid, x, y):
            outer_fire_cells.append((x, y))
    return outer_fire_cells

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
print("Fire Cells")
result = list(path_for_fire.values())
for i, group in enumerate(result):
    print(f"Time {i}: {group}")
print()
print("Fire neighbor Cells")
print()
result = list(neighbors_for_fire.values())
for i, group in enumerate(result):
    print(f"Time {i}: {group}")
print()
print("Fire neighbior Cells probilities")
result = list(probility_for_bot4.values())
for i, group in enumerate(result):
    print(f"Time {i}: {group}")


def estimate_probability(originalgrid, bot_pos, probability_of_neighbor):
    Manhattan_dis_list = []

    x,y = bot_pos
    current_neighbor_cells_of_bot_4 = get_neighbors_bot4(originalgrid,x,y)

    print(current_neighbor_cells_of_bot_4)
    current_neighbor_cells_of_fire = [xy for xy, value in probability_of_neighbor]
    probabilityList = [value for xy, value in probability_of_neighbor]

    #current_neighbor_cells_of_fire , probabilityList = probability_of_neighbor

    # print(current_neighbor_cells_of_bot_4, current_neighbor_cells_of_fire, probability_of_neighbor)
    # print(probability_of_neighbor)
    if len(current_neighbor_cells_of_bot_4) != 0:
        for i,j in current_neighbor_cells_of_bot_4:
            distance = 0
            for index, (x,y) in enumerate(current_neighbor_cells_of_fire):
                probability = probabilityList[index]
                manhattanDist = (abs(x - i) + abs(y - j))
                if manhattanDist != 0:
                    distance += probability / manhattanDist
                else: distance = 0
            Manhattan_dis_list.append(distance)
    else:
        return []

    print("manhattan",Manhattan_dis_list)
    return Manhattan_dis_list


#print(estimate_probability([(0, 0), (0, 1)], [(7, 9), (7, 8), (7, 7)], [0.6, 0.6]))
# output should be ()
###############################################################
'''
                        BOT - 1 
'''
###############################################################


def find_shortest_path(original_grid, index, fireP, neighborP, start, end):
    queue = deque([(start, [])])
    visited = set()
    visited_dfs = set()
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        if (x, y) not in visited:
            visited.add((x, y))
            visited_dfs.add((x, y))
            # print(visited)
            for nx, ny in get_neighbors(x, y):
                if is_valid_move_bot(original_grid, index, fireP, neighborP, nx, ny):
                    queue.append(((nx, ny), path + [(nx, ny)]))
            visited_dfs.remove((x, y))
    return None

def heuristic_bot4(bot_4_grid, bot_pos, current_fire_cell, prob, edgefire):
    # list of prob
    # prob = [0.5, 0.8, 0.6, 0.8]

    # list of current neighbor cells
    #neig = [(1, 2), (3, 4), (5, 6), (7, 8)]

    # list of lengths of BFS from curr neighbor cells to Button
    neighborP = []
    neiBFS = []

    neig = []
    x,y = bot_pos
    neig.extend(get_neighbors_bot4(bot_4_grid, x, y))

    print(neig)
    for x, y in neig:
        nei_pos = (x, y)
        path = find_shortest_path(bot_4_grid, 2, current_fire_cell, neighborP, nei_pos, button_pos)
        if path is None or path == []:
            neiBFS.append(0)
        else:
            neiBFS.append(len(path))

    # list of edge fire cells
    # edgefire = [(2, 3), (1, 3), (4, 6)]

    # distance between button and fire
    # create new index for valid for BFS and ignore fire position
    current_fire_cell = []
    minfire = 999999
    for x, y in edgefire:
        fire_pos = (x, y)
        path = find_shortest_path(bot_4_grid, 2, current_fire_cell, neighborP, fire_pos, button_pos)
        if minfire > len(path):
            minfire = len(path)

    # Calculating risk factor for each neighbor cell
    risk_factor = []
    for i in range(len(prob)):
        risk_factor.append(prob[i]*(neiBFS[i]**2))

    # Now we have risk factor, neiBFS, and minfire. we return neigh[i] which we want to move to
    # max = max(neiBFS)
    minl = min(neiBFS)

    if (1/3)*minfire < minl:
        print("maximum")
        res = 9999
        rf = 0
        index = 0
        for x in range(len(prob)):
            if risk_factor[x] != 0 and neiBFS[x] < res or (neiBFS[x] == res and rf < risk_factor[x]):
                res = neiBFS[x]
                index = x
                rf = risk_factor[x]
        return neig[index]
    else:
        print("minimum")
        rf = 9999
        index = 0
        for x in range(len(prob)):
            if risk_factor[x] !=0 and rf > risk_factor[x]:
                rf = risk_factor[x]
                index = x
        return neig[index]


def prob_for_cell(originalGrid, bot_pos):

    temp_grid = [row.copy() for row in originalGrid]

    # Step 1: Get all the fire cells of the originalGrid
    fire_cells = [(i, j) for i in range(D) for j in range(D) if temp_grid[i][j] == "F"]

    # Step 2: Initialize 2D array prob_for_cell with each element equal to 0
    prob_for_cell = [[0 for j in range(D)] for i in range(D)]

    # Step 3: Set prob[fire_cell] = 1 for each fire_cells
    for i, j in fire_cells:
        prob_for_cell[i][j] = 1

    # Step 4: while fire_cells is Not Empty
    while fire_cells:
        current_fire_cell = fire_cells.pop()

        # Step 4a: mul_factor = prob[fire_cell]
        mul_factor = prob_for_cell[current_fire_cell[0]][current_fire_cell[1]]

        # Step 4b: Find valid neighbors of fire_cell using get_neighbors and is_valid_move
        neighbors = get_neighbors(current_fire_cell[0], current_fire_cell[1])

        # Step 4c: For each neighbor in neighbors
        for neighbor in neighbors:
            if(is_valid_move(temp_grid, neighbor[0], neighbor[1])):
                x, y = neighbor
                # Step 4ci: update prob_for_cell[neighbor] += mul_factor * calculate_fire_spread_probability(q, fire_neighbors)
                prob_for_cell[x][y] += mul_factor * calculate_fire_spread_probability(q, find_fire_neighbors(temp_grid, x, y))

                # Step 4cii: Add neighbor in fire_cells
                if neighbor not in fire_cells:
                    fire_cells.append(neighbor)
                    temp_grid[x][y] = "F"

    # Step 5: return prob_for_cell
    neighbors = get_neighbors_bot4(originalGrid, bot_pos[0], bot_pos[1])
    neighbor_prob_list = []
    for neighbor in neighbors:
        neighbor_prob_list.append(prob_for_cell[neighbor[0]][neighbor[1]])

    return neighbor_prob_list


def task_bot4():
    time  = 0
    button_pos = (x_button, y_button)
    bot_pos = (x_bot, y_bot)

    print("bot pos", bot_pos)
    bot_4_grid = [row.copy() for row in grid]
    FirePath = list(path_for_fire.values())
    currentNeighbor = list(neighbors_for_fire.values())
    probabilityCell = list(probility_for_bot4.values())
    current_fire_cell = [(x_fire, y_fire)]

    print()
    for x in bot_4_grid:
        print(' '.join(x))
    print()

    neighbor = currentNeighbor[0]
    prob = probabilityCell[0]

    while True:

        for x in bot_4_grid:
            print(' '.join(x))
        print()

        # Huzaif - Probability Queue
        # probability_bot_4 = prob_for_cell(bot_4_grid,bot_pos)

        # Kush - Probability Queue
        probability_bot_4 = estimate_probability(bot_4_grid, bot_pos, prob)

        edge_fire_cell = outer_fire_cells(bot_4_grid)

        x,y = heuristic_bot4(bot_4_grid,bot_pos,current_fire_cell,probability_bot_4,edge_fire_cell)
        print("x,y", (x,y))


        bot_pos = (x,y)
        bot_4_grid[x][y] = "P"

        if len(FirePath) == 0:
            print("Fire reached to Button. Bot 4 Loss")
            break
        f4 = FirePath[0]
        if (x_button, y_button) == bot_pos:
            print("Bot reached Button. Bot 4 Won")
            break

        next_fire_cell = f4

        for i, j in next_fire_cell:
            bot_4_grid[i][j] = "F"
            current_fire_cell.append((i, j))
            list(set(current_fire_cell))

        FirePath.pop(0)

        if bot_pos in current_fire_cell:
            print("Fire Caught Bot 4 ")
            break

        # if len(currentNeighbor) != 0:
        #     neighbor = currentNeighbor.pop(0)

        if len(probabilityCell) != 0:
            prob = probabilityCell.pop(0)

        time+=1

    print(time)


task_bot4()




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
    # print("Main Path", path)
    p1 = bot_pos
    # For Bot 1

    while True:
        # for x in bot_1_grid:
        #     print(' '.join(x))
        # print()
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
        # bot_1_grid[t][k] = "P"
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
        #print(time)
        # Initialize the path from time = 1
        # At time t = 0 initialize the bot as per instruction
        # print(bot_pos)
        # print("fire cell==",current_fire_cell)
        # print("neighbor==",neighbor)
        if time > 0:
            path3 = find_shortest_path(bot_3_grid, 3, current_fire_cell, neighbor, bot_pos, button_pos)

            #print("O==", path3)
            # print("p2", path2)
            if path3 is None or path3 == []:
                path3 = find_shortest_path(bot_3_grid, 2, current_fire_cell, neighbor, bot_pos, button_pos)
                #print("N==", path3)
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
            # print("Neighbor",neighbor)
        else:
            break
        time += 1
    print(time)






#task()

# for x in grid:
#     print(' '.join(x))
# print()
