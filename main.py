import math
import random
import heapq
from collections import deque

# Bock - #
# Open - O
# Bot - P
# Button - B
# Fire - F

D = 40
q = 0.7
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

# grid = [['#', 'O', '#', 'O', '#', '#', 'O', '#', 'O', 'O', 'O', 'O', 'O', 'O', '#', 'O', '#', 'O', '#', 'O'],
# ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '#', 'O', 'O', '#', '#', 'O', 'O', 'O', '#', 'O', '#', 'O'],
# ['O', '#', '#', 'O', '#', 'O', '#', 'O', 'O', 'O', '#', '#', 'O', 'O', '#', '#', 'O', 'O', 'B', 'O'],
# ['#', 'O', 'O', '#', 'O', '#', 'P', 'O', '#', 'O', '#', 'O', 'O', 'O', '#', 'O', 'O', '#', 'O', '#'],
# ['O', '#', 'O', '#', 'O', 'O', 'O', '#', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '#', 'O', '#', '#', 'O'],
# ['O', 'O', 'O', 'O', '#', 'O', 'O', 'F', 'O', '#', 'O', 'O', 'O', 'O', 'O', '#', 'O', 'O', 'O', 'O'],
# ['#', '#', 'O', '#', 'O', 'O', 'O', 'O', '#', '#', 'O', 'O', 'O', 'O', 'O', '#', 'O', '#', '#', 'O'],
# ['O', 'O', 'O', 'O', 'O', '#', 'O', 'O', 'O', 'O', 'O', '#', 'O', '#', 'O', 'O', 'O', 'O', 'O', '#'],
# ['O', '#', 'O', '#', 'O', 'O', 'O', 'O', 'O', '#', '#', 'O', 'O', 'O', '#', '#', 'O', '#', '#', 'O'],
# ['#', 'O', 'O', 'O', '#', 'O', '#', 'O', '#', 'O', 'O', 'O', 'O', '#', '#', 'O', 'O', 'O', '#', 'O'],
# ['O', 'O', 'O', 'O', 'O', 'O', '#', 'O', 'O', '#', 'O', '#', 'O', '#', 'O', 'O', '#', '#', 'O', 'O'],
# ['#', '#', 'O', '#', '#', 'O', 'O', '#', 'O', '#', 'O', '#', 'O', 'O', 'O', 'O', 'O', '#', 'O', '#'],
# ['O', 'O', 'O', '#', 'O', '#', 'O', 'O', 'O', '#', 'O', '#', 'O', '#', 'O', '#', 'O', 'O', 'O', 'O'],
# ['O', 'O', '#', 'O', 'O', 'O', 'O', '#', 'O', 'O', 'O', 'O', 'O', '#', 'O', 'O', 'O', '#', '#', 'O'],
# ['O', '#', 'O', '#', 'O', '#', '#', 'O', '#', '#', '#', '#', 'O', 'O', '#', 'O', '#', 'O', '#', 'O'],
# ['O', 'O', 'O', 'O', '#', 'O', 'O', 'O', 'O', 'O', 'O', '#', '#', 'O', 'O', 'O', 'O', 'O', 'O', '#'],
# ['#', '#', 'O', '#', 'O', 'O', '#', '#', 'O', '#', 'O', 'O', 'O', 'O', '#', 'O', '#', '#', 'O', 'O'],
# ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '#', 'O', '#', 'O', 'O', 'O', 'O', '#', '#', 'O'],
# ['#', 'O', '#', 'O', 'O', '#', 'O', '#', '#', 'O', 'O', 'O', '#', 'O', 'O', '#', 'O', 'O', 'O', 'O'],
# ['O', 'O', 'O', '#', 'O', 'O', 'O', 'O', 'O', '#', '#', 'O', 'O', '#', 'O', '#', 'O', '#', '#', 'O']]


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


# bot_pos = (3,6)
# x_bot, y_bot = bot_pos
# button_pos = (2,18)
# x_button, y_button = button_pos
# fire_pos = (5,7)
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
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < D and 0 <= ny < D and (grid[nx][ny] != "#" and grid[nx][ny] != "F")]

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
        if 0 <= nx < D and 0 <= ny < D and (grid[nx][ny] != "F" and grid[nx][ny] != "#"):
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
#print("Fire Cells")
result = list(path_for_fire.values())
#for i, group in enumerate(result):
#    print(f"Time {i}: {group}")
print()
#print("Fire neighbor Cells")
print()
result = list(neighbors_for_fire.values())
#for i, group in enumerate(result):
#    print(f"Time {i}: {group}")
#print()
#print("Fire neighbior Cells probilities")
result = list(probility_for_bot4.values())
#for i, group in enumerate(result):
#    print(f"Time {i}: {group}")


def estimate_probability(originalgrid, bot_pos, probability_of_neighbor):
    Manhattan_dis_list = []

    x,y = bot_pos
    current_neighbor_cells_of_bot_4 = get_neighbors_bot4(originalgrid,x,y)

    print(current_neighbor_cells_of_bot_4)
    current_neighbor_cells_of_fire = [xy for xy, value in probability_of_neighbor]
    probabilityList = [value for xy, value in probability_of_neighbor]

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


# print(estimate_probability([(0, 0), (0, 1)], [(7, 9), (7, 8), (7, 7)], [0.6, 0.6]))
# output should be ()
###############################################################
'''
                        BFS Implementation
'''
###############################################################

# path = find_shortest_path(bot_4_grid, 2, current_fire_cell, neighborP, fire_pos, button_pos)

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

def find_all_paths(original_grid, index, fireP, neighborP, start, end):
    queue = deque([(start, [])])
    all_paths = []
    visited = set()
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            all_paths.append(path)
            continue
        if (x, y) not in visited:
            visited.add((x, y))
            for nx, ny in get_neighbors(x, y):
                if is_valid_move_bot(original_grid, index, fireP, neighborP, nx, ny):
                    new_path = path + [(nx, ny)]
                    queue.append(((nx, ny), new_path))
    if not all_paths:
        return None
    return all_paths

def heuristic_bot4(bot_4_grid, bot_pos, current_fire_cell, prob, edgefire, fireNeighbor):

    neighborP = []
    neiBFS = []

    neig = []
    x,y = bot_pos
    neig.extend(get_neighbors_bot4(bot_4_grid, x, y))

    print("neighbors of bot 4", neig)
    print("Its Fire Cell", current_fire_cell)
    print("Its edge", edgefire)
    #print("Its neighbor", fireNeighbor)



    for x, y in neig:

        nei_pos = (x, y)
        path = find_shortest_path(bot_4_grid, 2, current_fire_cell, fireNeighbor , nei_pos, button_pos)
        print("Path == ", path)
        if path is None or path == []:
            # path = find_shortest_path(bot_4_grid, 2, current_fire_cell, fireNeighbor, nei_pos, button_pos)
            # if path is None or path == []:
            if bot_4_grid[x][y] == "B":
                return (x,y)
            else:
                neiBFS.append(1)
        else:
            neiBFS.append(len(path))
    print("Path from player neighbor to button",neiBFS)


    # dist from fire to player
    minFP = 999999
    print(bot_pos)
    for x, y in edgefire:
        fire_pos = (x, y)

        path = find_shortest_path(bot_4_grid, 2, current_fire_cell, neighborP, fire_pos, bot_pos)
        if path is None or path == []:
            pass
        else:
            if minFP > len(path):
                minFP = len(path)
        #print("fire, bot, min == ", fire_pos, bot_pos, minFP)
    print("Path from fire to player", minFP)


    if len(neiBFS) is None or len(neiBFS) == 0 :
        return (-1,-1)

    minl = min(neiBFS) # min length from bot to button

    min_indices = [i for i, x in enumerate(neiBFS) if x == minl]

    tempList = []

    if (minFP > minl) or (minFP == minl) or (minFP < minl):
        if len(min_indices) == 1:
            return neig[min_indices[0]]
        if len(min_indices) > 1:
            for i in min_indices:
                tempList.append(prob[i])
            minProbvalue = min(tempList)
            return neig[prob.index(minProbvalue)]



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
#kush
def astarK(grid, start, goal):
    fire_cells = outer_fire_cells(grid)
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    def calculate_cost(cell):
        m = 20
        n = 2
        #print("Outer Fire cells", fire_cells)
        min_distance_FP = min(manhattan_distance(cell, fire) for fire in fire_cells)
        min_distance_BP = manhattan_distance(cell, goal)
        max_possible_distance = 2 * len(grid)
        if min_distance_FP == 0:
            return len(grid)
        cost = m * (min_distance_BP) - n * (min_distance_FP)
        #print("Cost", min_distance_BP, min_distance_FP, cost)
        return cost

    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def get_neighbors(node):
        neighbors = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = node[0] + dx, node[1] + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#' and grid[x][y] != 'F':
                neighbors.append((x, y))
        return neighbors

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}

    g_score = [[float('inf') for _ in row] for row in grid]
    g_score[start[0]][start[1]] = 0

    f_score = [[float('inf') for _ in row] for row in grid]
    f_score[start[0]][start[1]] = heuristic(start)

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current[0]][current[1]] + calculate_cost(neighbor)
            # print("TGS",tentative_g_score)
            if tentative_g_score < g_score[neighbor[0]][neighbor[1]]:
                came_from[neighbor] = current
                g_score[neighbor[0]][neighbor[1]] = tentative_g_score
                f_score[neighbor[0]][neighbor[1]] = g_score[neighbor[0]][neighbor[1]] + heuristic(neighbor)
                if neighbor not in [node[1] for node in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor[0]][neighbor[1]], neighbor))
    return None

def astar(grid, start, goal):
    parent = [[(-1, -1) for _ in range(len(grid))] for _ in range(len(grid))]

    def reconstruct_path(node):
        path = []
        while not(node[0] == start[0] and node[1] == start[1]):
            path.append(node)
            node = parent[node[0]][node[1]]
        return list(reversed(path))

    fire_cells = outer_fire_cells(grid)
    #print("Fire_Cells", fire_cells)
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def calculate_cost(start, end):
        m = D
        n = 1
        min_distance_FS = min(manhattan_distance(start, fire) for fire in fire_cells)
        min_distance_SE = manhattan_distance(start, end)
        if((start[0] == 1 and start[1] == 9) or (start[0] == 3 and start[1] == 9)):
            print("min_distance_FS", min_distance_FS)
            print("min_distance_SE", min_distance_SE)
        cost = m*(min_distance_SE) - n*(min_distance_FS)
        return cost

    open_set = []
    closed_set = set()
    cost = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    reach_cost = [[float('inf') for _ in range(len(grid))] for _ in range(len(grid))]
    reach_cost[start[0]][start[1]] = 0
    heapq.heappush(open_set, (0, start))
    
    while open_set:
        current_cost, current = heapq.heappop(open_set)

        if current[0] == goal[0] and current[1] == goal[1]:
            return reconstruct_path(current)
        
        closed_set.add(current)

        for neighbor in get_neighbors_bot4(grid, current[0], current[1]):
            if neighbor in closed_set:
                continue

            tentative_reach_cost = reach_cost[current[0]][current[1]] + calculate_cost(current, neighbor)

            if (not any((y[0] == neighbor[0] and y[1] == neighbor[1]) for x,y in open_set)) or tentative_reach_cost < reach_cost[neighbor[0]][neighbor[1]]:
                reach_cost[neighbor[0]][neighbor[1]] = tentative_reach_cost
                cost[neighbor[0]][neighbor[1]] = reach_cost[neighbor[0]][neighbor[1]] + calculate_cost(neighbor, goal)
                parent[neighbor[0]][neighbor[1]] = current
            
                if (not any((y[0] == neighbor[0] and y[1] == neighbor[1]) for x,y in open_set)):
                    heapq.heappush(open_set, (cost[neighbor[0]][neighbor[1]], neighbor))
            if(current[0] == 2 and current[1] == 9):
                print("ReachCost at", neighbor, reach_cost[neighbor[0]][neighbor[1]])
                print("TotalCost at", neighbor, cost[neighbor[0]][neighbor[1]])    
    return None

def task_4():
    bot_4_grid = [row.copy() for row in grid]
    FirePath = list(path_for_fire.values())
    # FirePath = [[(5, 6)], [(5, 5), (4, 6)], [(6, 5), (6, 7), (4, 5), (3, 6), (6, 6)], [(4, 4), (7, 7), (5, 8), (6, 4)], [(7, 4), (3, 4), (8, 7), (7, 6), (7, 8)], [(8, 8), (8, 4), (3, 7), (7, 3), (7, 9), (8, 6)], [(2, 7), (7, 10), (7, 2), (8, 5)], [(9, 5), (1, 7), (8, 2)], [(6, 2), (7, 1), (9, 2), (6, 10), (1, 6), (2, 8)], [(10, 5), (1, 5), (0, 6), (2, 9), (5, 10), (9, 1), (9, 7)], [(9, 3), (7, 0), (10, 1), (10, 7), (3, 9), (4, 8), (2, 5)], [(4, 10), (5, 11), (4, 9), (1, 4), (10, 0), (11, 5), (10, 3), (1, 9), (10, 2)], [(10, 8), (6, 11), (10, 4), (0, 9), (11, 6), (4, 11), (1, 3)], [(6, 12), (1, 2), (0, 10), (5, 2), (11, 2), (12, 6), (1, 10), (0, 8), (5, 12), (3, 11)], [(12, 7), (1, 1), (0, 3), (4, 12), (5, 1), (4, 2), (6, 13), (8, 0), (7, 12)], [(4, 13), (5, 3), (5, 13), (2, 3), (8, 12), (13, 6), (3, 2), (12, 8), (11, 8)], [(9, 12), (8, 13), (3, 13), (8, 11), (12, 2), (4, 14), (1, 0), (3, 12)], [(13, 8), (12, 1), (5, 14), (5, 0), (9, 11), (10, 12), (0, 11)], [(0, 1), (9, 10), (3, 1), (12, 0), (2, 0), (2, 13), (0, 12), (2, 12), (13, 5)], [(13, 1), (9, 9), (10, 10), (13, 9)], [(13, 4), (11, 10), (0, 13), (6, 14), (13, 0), (1, 13)], [(12, 4), (4, 0), (14, 4), (13, 10)], [(12, 10), (1, 14), (11, 12), (13, 11), (7, 14)], [(1, 15), (14, 0), (13, 3)], [(12, 12), (13, 12), (7, 15)], [(11, 13), (15, 0), (0, 15), (14, 12)], [(7, 16), (11, 14)], [(7, 17), (15, 1), (14, 13), (11, 15), (6, 16)], [(15, 13), (12, 14)], [(10, 15), (11, 16), (10, 14), (16, 13), (15, 14), (8, 16), (7, 18)], [(17, 13), (9, 15), (16, 12)], [(9, 16), (16, 11), (12, 16), (18, 13), (5, 16)], [(13, 14), (4, 16), (12, 17), (16, 10), (17, 11), (15, 15)], [(13, 16), (3, 16), (15, 16), (13, 15), (9, 17), (12, 18), (14, 15), (15, 2)], [(15, 17), (15, 3), (11, 18), (14, 2), (18, 11), (17, 14), (18, 14)], [(19, 14), (14, 17), (18, 10), (5, 17), (15, 18), (16, 2), (15, 10), (16, 15), (17, 15), (19, 11)], [(16, 18), (17, 16), (12, 19), (18, 9), (19, 12), (17, 2), (15, 9)], [(15, 8), (18, 16), (2, 16), (17, 9), (13, 19), (5, 18)], [(18, 17), (16, 19), (15, 7), (19, 16), (14, 19), (5, 19), (16, 8), (17, 8), (10, 18)], [(17, 1), (2, 17), (4, 19), (17, 19), (17, 3), (15, 6), (18, 18), (6, 19)], [(15, 5), (18, 1), (17, 0), (18, 19), (18, 3), (10, 19), (3, 15), (17, 4)], [(18, 4), (14, 7), (1, 17), (16, 5), (17, 5)], [(17, 7), (9, 19), (19, 1), (19, 19)]]
    FirePath.pop(0)
    print("FirePath","\n",FirePath)
    time = 0
    bot_pos = (x_bot,y_bot)
    print("Bot_Pos ",bot_pos)
    while True:
        for x in bot_4_grid:
             print(' '.join(x))
        print()
        print("Reached", bot_pos, "at", time)
        #path = astarK(bot_4_grid, bot_pos, button_pos)
        path = astar(bot_4_grid, bot_pos, button_pos)
        print("Path ",path)
        print("Button_Pos ",button_pos)
        if path:
            bot_pos = path[0]
            (x,y) = path[0]
            bot_4_grid[x][y] = "P"
            if bot_pos == button_pos:
                print("win")
                break
        else:
            print("loose")
            break

        if len(FirePath) == 0:
            print("Fire reached to Button. Bot 4 Loss")
            break
        f4 = FirePath.pop(0)
        for i,j in f4:
            bot_4_grid[i][j] = "F"
        if bot_pos in f4:
            print("Losse fire caught bot")
            break
        time += 1
    print(time)


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
            # print("Neighbor",neighbor)
        else:
            break
        time += 1
    print(time)





task_4()
task()


# for x in grid:
#     print(' '.join(x))
# print()