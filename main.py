import math
import random
from collections import deque
import heapq

D = 40
q = 0.8

print("Block Cell -> 🟫")
print("Open Cell -> ⬜")
print("Bot Cell -> 🤖")
print("Button Cell -> 🟩")

# D = int(input("Enter Size For Grid -> "))
# q = float(input("Enter q value for Fire (0 - 1)-> "))

##############################################################
'''                   BUILD GRID LAYOUT                    '''
##############################################################

grid = [["🟫" for _ in range(D)] for _ in range(D)]

openBlockPosArr = []
deadEndCells = []
openGrid = []

randIntX = random.randint(1, D - 2)
randIntY = random.randint(1, D - 2)
grid[randIntX][randIntY] = "⬜️"
openBlockPosArr.append((randIntX, randIntY))

effX1 = randIntX - 1
effX2 = randIntX + 1
effY1 = randIntY - 1
effY2 = randIntY + 1

while openBlockPosArr:
    openBlockPosArr = []
    for x in range(effX1, effX2 + 1):
        for y in range(effY1, effY2 + 1):
            openBlockPos = 0
            if grid[x][y] == "🟫":
                a = x + 1
                b = x - 1
                c = y + 1
                d = y - 1
                if a <= effX2 and grid[a][y] == "⬜️":
                    openBlockPos += 1
                if b >= effX1 and grid[b][y] == "⬜️":
                    openBlockPos += 1
                if c <= effY2 and grid[x][c] == "⬜️":
                    openBlockPos += 1
                if d >= effY1 and grid[x][d] == "⬜️":
                    openBlockPos += 1
                if openBlockPos == 1:
                    openBlockPosArr.append((x, y))
    if openBlockPosArr:

        randIndex = random.randint(0, len(openBlockPosArr) - 1)
        randIntX, randIntY = openBlockPosArr[randIndex]
        grid[randIntX][randIntY] = "⬜️"

        if 0 < effX1 == randIntX:
            effX1 = randIntX - 1
        if D - 1 > effX2 == randIntX:
            effX2 = randIntX + 1
        if 0 < effY1 == randIntY:
            effY1 = randIntY - 1
        if D - 1 > effY2 == randIntY:
            effY2 = randIntY + 1

for x in range(D):
    for y in range(D):
        deadEndBlock = 0
        deadEndBlockArr = []
        if grid[x][y] == "⬜️":
            a = x + 1
            b = x - 1
            c = y + 1
            d = y - 1
            if 0 <= a <= D - 1 and grid[a][y] == "🟫":
                deadEndBlock += 1
                deadEndBlockArr.append((a, y))
            if 0 <= b <= D - 1 and grid[b][y] == "🟫":
                deadEndBlock += 1
                deadEndBlockArr.append((b, y))
            if 0 <= c <= D - 1 and grid[x][c] == "🟫":
                deadEndBlock += 1
                deadEndBlockArr.append((x, c))
            if 0 <= d <= D - 1 and grid[x][d] == "🟫":
                deadEndBlock += 1
                deadEndBlockArr.append((x, d))
            if deadEndBlock >= 3:
                randIndex = random.randint(0, len(deadEndBlockArr) - 1)
                randIntX, randIntY = deadEndBlockArr[randIndex]
                deadEndCells.append(
                    (randIntX, randIntY))  # for each dead end pick a coordinate to open at random and store in list

# shuffle the list and open 50% of the dead end cells
random.shuffle(deadEndCells)
for i in range(int(len(deadEndCells) / 2)):
    x, y = deadEndCells[i]
    grid[x][y] = "⬜️"

########################################################################################################
'''                            INITIALIZE BOT, BUTTON, AND FIRE POSITION                             '''
########################################################################################################

# Appending Open Cell to OpenGrid List
for x in range(D):
    for y in range(D):
        if grid[x][y] == "⬜️":
            openGrid.append((x, y))


# Find the Position for the Bot Cell
def bot_open_start_position():
    position = random.randint(0, len(openGrid) - 1)
    a, b = openGrid[position]
    openGrid.pop(position)
    grid[a][b] = "🤖"
    return a, b


# Initialize Bot
x_bot, y_bot = bot_open_start_position()
bot_pos = (x_bot, y_bot)


# Find the Position for The Fire Cell
def fire_open_start_position():
    position = random.randint(0, len(openGrid) - 1)
    a, b = openGrid[position]
    openGrid.pop(position)
    grid[a][b] = "🔥"
    return a, b


# Initialize Fire
x_fire, y_fire = fire_open_start_position()
fire_pos = (x_fire, y_fire)


# Find the Position for The Button Cell
def button_open_position():
    position = random.randint(0, len(openGrid) - 1)
    a, b = openGrid[position]
    openGrid.pop(position)
    grid[a][b] = "🟩"
    return a, b


# Initialize Button
x_button, y_button = button_open_position()
button_pos = (x_button, y_button)

print("Initial Grid")
for x in grid:
    print(' '.join(x))
print()


def find_fire_neighbors(grid, x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    count = [(nx, ny) for nx, ny in neighbors if 0 <= nx < D and 0 <= ny < D and grid[nx][ny] == "🔥"]
    return len(count)


def get_neighbors(x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < D and 0 <= ny < D]


def is_valid_move(grid, x, y):
    return 0 <= x < D and 0 <= y < D and grid[x][y] != "🟫" and grid[x][y] != "🔥"


def is_valid_move_bot(grid, index, pathF, neighborFP, x, y):
    # if index == 1 then for Bot 1
    if index == 1:
        return 0 <= x < D and 0 <= y < D and grid[x][y] != "🟫" and grid[x][y] != grid[x_fire][y_fire]
    # if index == 2 then for Bot 2
    if index == 2:
        return 0 <= x < D and 0 <= y < D and grid[x][y] != "🟫" and not ((x, y) in pathF)
    # if index == 2 then for Bot 3
    if index == 3:
        return 0 <= x < D and 0 <= y < D and grid[x][y] != "🟫" and not ((x, y) in pathF) and not ((x, y) in neighborFP)


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

# Fire Cell Takes an Input of the Current Grid at the given Time Index
# NOTE: Every Bot have a SAME FIRE environment - To get the Better Comparison among All Bots
def fire(OriginalGrid, index):
    # 1) Creating a Temporary Grid from the Original Grid
    temp_grid = [row.copy() for row in OriginalGrid]

    # 2) Storing the neighbor Co-ordinates and which are the valid neighbors
    neighbor_coordinates = []
    valid_neighbor = []

    # 3) Get the Fire Cells from the original Grid..
    fire_cell = [(x, y) for x in range(D) for y in range(D) if OriginalGrid[x][y] == "🔥"]

    # 4) Get the Fire Neighbors from the fire_cell list
    for x, y in fire_cell:
        neighbor_coordinates.extend(get_neighbors(x, y))

    # 5) Check if they are validation of the neighbors and filter out
    # are neighbor out of the grid ? and are the neighbor fire cell ?
    # is Valid method will filter out the neighbor of outside grid as well as fire cell
    # only neighbor will pass which are open cells
    for x, y in neighbor_coordinates:
        if is_valid_move(OriginalGrid, x, y):
            valid_neighbor.append((x, y))
            if index not in neighbors_for_fire:
                neighbors_for_fire[index] = []
            neighbors_for_fire[index].append((x, y))

    # 6) Remove repeated Cells on the valid neighbor cell.
    valid_neighbor = list(set(valid_neighbor))

    # 7) iterate in neighbor and get the fire neighbor to see the count of burning neighbor cell
    # Counting how many fire cells to the OPEN neighbor
    # The probability of each neighbor is being calculated and stored into the dictionary
    # Based on the counted neighbor, finding the fire spread probability using the given formulae 1 - (1 - q) ** K
    for x, y in valid_neighbor:
        count = find_fire_neighbors(OriginalGrid, x, y)
        probability = calculate_fire_spread_probability(q, count)
        if index not in probility_for_bot4:
            probility_for_bot4[index] = []
        probility_for_bot4[index].append(probability)
        # Taking a random value from the 0 to 1. Based on the random Value -- It will Pick Fire cells
        # For example: what is the probability of getting 1 on dice is 1/6
        ran = random.random()
        if ran < probability:
            if OriginalGrid[x][y] != "🟩":
                temp_grid[x][y] = "🔥"
                if index not in path_for_fire:
                    path_for_fire[index] = []
                path_for_fire[index].append((x, y))
            else:
                return None

    # Testing Purpose Printing Grid
    # for x in temp_grid:
    #     print(' '.join(x))
    # print()
    return temp_grid


# Starting Fire until Fire reach to Button.
def start_fire():
    time = 1
    tempGrid = [row.copy() for row in grid]
    while True:
        # print(time)
        tempGrid = fire(tempGrid, time)
        if tempGrid is None:
            break
        time += 1


# Ignition to Fire
start_fire()


# Helper Method for OutFire
def is_outer_fire(grid, x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for nx, ny in neighbors:
        if 0 <= nx < D and 0 <= ny < D and (grid[nx][ny] != "🔥" and grid[nx][ny] != "🟫"):
            return True
    return False

# Method for Outer Fire
def outer_fire_cells(originalGrid):
    outer_fire_cells = []
    #1) Get all the fire cells of the originalGrid
    fire_cells = [(i, j) for i in range(D) for j in range(D) if originalGrid[i][j] == "🔥"]
    for x,y in fire_cells:
        if is_outer_fire(originalGrid, x, y):
            outer_fire_cells.append((x, y))
    return outer_fire_cells


###############################################################
'''                 BFS Implementation                      '''
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
            for nx, ny in get_neighbors(x, y):
                if is_valid_move_bot(original_grid, index, fireP, neighborP, nx, ny):
                    queue.append(((nx, ny), path + [(nx, ny)]))
            visited_dfs.remove((x, y))
    return None

def astar(grid, start, goal):
    fire_cells = outer_fire_cells(grid)
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    def calculate_cost(cell):
        m = D
        n = int(q / D)
        min_distance_FP = min(manhattan_distance(cell, fire) for fire in fire_cells)
        min_distance_BP = manhattan_distance(cell, goal)
        if min_distance_FP < 1:
            return 0
        if min_distance_BP < 1:
            return 0
        #cost = (10 * q) + (1 / min_distance_BP) * (50 / (1 + (1 / min_distance_FP)))
        cost = (min_distance_BP) * (50 / (1 + min_distance_FP)) ** (1/q)
        return int(cost)

    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def get_neighbors(node):
        neighbors = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = node[0] + dx, node[1] + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '🟫' and grid[x][y] != '🔥':
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
            tentative_g_score = g_score[current[0]][current[1]]  + 1 # calculate_cost(neighbor)
            # print("TGS",tentative_g_score)
            if tentative_g_score < g_score[neighbor[0]][neighbor[1]]:
                came_from[neighbor] = current
                g_score[neighbor[0]][neighbor[1]] = tentative_g_score
                f_score[neighbor[0]][neighbor[1]] = g_score[neighbor[0]][neighbor[1]] + heuristic(neighbor)
                if neighbor not in [node[1] for node in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor[0]][neighbor[1]], neighbor))
    return None

def get_neighbors_bot4(grid, x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < D and 0 <= ny < D and (grid[nx][ny] != "🟫" and grid[nx][ny] != "🔥")]

def astar__(grid, start, goal):
    parent = [[(-1, -1) for _ in range(len(grid))] for _ in range(len(grid))]

    def reconstruct_path(node):
        path = []
        while not (node[0] == start[0] and node[1] == start[1]):
            path.append(node)
            node = parent[node[0]][node[1]]
        return list(reversed(path))

    fire_cells = outer_fire_cells(grid)

    # print("Fire_Cells", fire_cells)
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def calculate_cost(start, end):
        m = D
        n = 1
        min_distance_FS = min(manhattan_distance(start, fire) for fire in fire_cells)
        min_distance_SE = manhattan_distance(start, end)
        #if ((start[0] == 1 and start[1] == 9) or (start[0] == 3 and start[1] == 9)):
            # print("min_distance_FS", min_distance_FS)
            # print("min_distance_SE", min_distance_SE)
        cost = m * (min_distance_SE) - n * (min_distance_FS)
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

            if (not any((y[0] == neighbor[0] and y[1] == neighbor[1]) for x, y in open_set)) or tentative_reach_cost < \
                    reach_cost[neighbor[0]][neighbor[1]]:
                reach_cost[neighbor[0]][neighbor[1]] = tentative_reach_cost
                cost[neighbor[0]][neighbor[1]] = reach_cost[neighbor[0]][neighbor[1]] + calculate_cost(neighbor, goal)
                parent[neighbor[0]][neighbor[1]] = current

                if (not any((y[0] == neighbor[0] and y[1] == neighbor[1]) for x, y in open_set)):
                    heapq.heappush(open_set, (cost[neighbor[0]][neighbor[1]], neighbor))
            # if (current[0] == 2 and current[1] == 9):
            #     print("ReachCost at", neighbor, reach_cost[neighbor[0]][neighbor[1]])
            #     print("TotalCost at", neighbor, cost[neighbor[0]][neighbor[1]])
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
    # print("Main Path", path)
    p1 = bot_pos
    # For Bot 1

    while True:
        # for x in bot_1_grid:
        #     print(' '.join(x))
        # print()
        if time > 0:
            if path is None or path == []:
                print("No path exist for bot 1")
                break
            else:
                p1 = path[0]
            path.pop(0)

        bot_pos = p1
        t, k = bot_pos
        bot_1_grid[t][k] = "🤖"
        if (x_button, y_button) == p1:
            print("Bot reached Button. Bot 1 Won")
            break
        if len(FirePath) == 0:
            print("Fire reached to Button. Bot 1 Loss")
            break

        next_fire_cell = FirePath[0]

        for i, j in next_fire_cell:
            bot_1_grid[i][j] = "🔥"
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

    time = 0
    FirePath = list(path_for_fire.values())
    current_fire_cell = [(x_fire, y_fire)]
    p2 = (x_bot, y_bot)
    while True:

        if time > 0:
            path2 = find_shortest_path(bot_2_grid, 2, current_fire_cell, neighborP, bot_pos, button_pos)
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
        bot_2_grid[t][k] = "🤖"

        if len(FirePath) == 0:
            print("Fire reached to Button. Bot 2 Loss")
            break
        f2 = FirePath[0]
        next_fire_cell = f2

        for i, j in next_fire_cell:
            bot_2_grid[i][j] = "🔥"
            current_fire_cell.append((i, j))
        if p2 in current_fire_cell:
            print("Fire Caught Bot 2 ")
            break
        FirePath.pop(0)
        time += 1
    print(time)
    for x in bot_2_grid:
        print(' '.join(x))
    print()

    print("***********************************************************")
    print("Bot 3")
    print("***********************************************************")
    # For Bot 3
    time = 0
    FirePath = list(path_for_fire.values())
    neighborP = list(neighbors_for_fire.values())
    neighbor = neighborP[0]
    current_fire_cell = [(x_fire, y_fire)]

    p3 = (x_bot, y_bot)
    bot_pos = p3

    while True:

        if time > 0:
            path3 = find_shortest_path(bot_3_grid, 3, current_fire_cell, neighbor, bot_pos, button_pos)
            if path3 is None or path3 == []:
                path3 = find_shortest_path(bot_3_grid, 2, current_fire_cell, neighbor, bot_pos, button_pos)
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
        bot_3_grid[t][k] = "🤖"

        f3 = FirePath[0]
        next_fire_cell = f3

        for i, j in next_fire_cell:
            bot_3_grid[i][j] = "🔥"
            current_fire_cell.append((i, j))
            list(set(current_fire_cell))
        if p3 in current_fire_cell:
            print("Fire Caught Bot 3 ")
            break

        FirePath.pop(0)
        if len(FirePath) == 0:
            print("Fire reached to Button. Bot 3 Loss")
            break
        if len(neighborP) != 0:
            neighbor = neighborP.pop(0)
        else:
            break
        time += 1
    print(time)
    for x in bot_3_grid:
        print(' '.join(x))
    print()

def task_4():
    print("***********************************************************")
    print("Bot 4")
    print("***********************************************************")
    bot_4_grid = [row.copy() for row in grid]
    FirePath = list(path_for_fire.values())
    time = 0
    bot_pos = (x_bot,y_bot)
    while True:
        # for x in bot_4_grid:
        #     print(' '.join(x))
        # print()
        path = astar(bot_4_grid, bot_pos, button_pos)
        if path:
            bot_pos = path[1]
            (x,y) = path[1]
            bot_4_grid[x][y] = "🤖"
            if bot_pos == button_pos:
                print("win")
                break
        else:
            print("loose")
            break

        if len(FirePath) == 0:
            print("Fire reached to Button. Bot 4 Loss")
            break
        f4 = FirePath[0]
        for i,j in f4:
            bot_4_grid[i][j] = "🔥"
        if bot_pos in f4:
            print("Losse fire caught bot")
            break
        FirePath.pop(0)
        time += 1
    print(time)
    for x in bot_4_grid:
        print(' '.join(x))
    print()

task()
task_4()