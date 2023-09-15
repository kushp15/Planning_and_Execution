import random

# Bock - #
# Open - O
# Bot - P
# Button - B
# Fire - F

D = 4
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

# Appending Open Cell to OpenGrid List
for x in range(D):
    for y in range(D):
        if grid[x][y] == "O":
            openGrid.append((x, y))


# Find the Position for The Fire Cell
def fire_open_Startposition():
    position = random.randint(0, len(openGrid) - 1)
    a, b = openGrid[position]
    openGrid.pop(position)
    # print(a, b, position, grid[a][b], len(queue))
    return a, b


# Find the Position for The Button Cell
def button_open_position():
    position = random.randint(0, len(openGrid) - 1)
    a, b = openGrid[position]
    openGrid.pop(position)
    # print(a, b, position, grid[a][b], len(queue))
    return a, b


# Find the Position for the Bot Cell
def bot_open_Startposition():
    position = random.randint(0, len(openGrid) - 1)
    a, b = openGrid[position]
    openGrid.pop(position)
    # print(a, b, position, grid[a][b], len(queue))
    return a, b


def find_side_neighbour(x, y, factor):

    if factor == 1:
        Direction_to_check = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        direction = []
        for a, b in Direction_to_check:
            new_x, new_y = a + x, b + y
            if (D > new_x > -1) and (-1 < new_y < D) and (
                    grid[new_x][new_y] == "O" or grid[new_x][new_y] == "P" or grid[new_x][new_y] == "B"):
                direction.append((new_x, new_y))
        print('dire==', direction)
    elif factor == 2:
        Direction_to_check = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        direction = []
        for a, b in Direction_to_check:
            new_x, new_y = a + x, b + y
            if (D > new_x > -1) and (-1 < new_y < D) and (grid[new_x][new_y] == "O" or grid[new_x][new_y] == "B"):
                direction.append((new_x, new_y))
        print('dire==', direction)

    return direction


def fire(x, y):
    firePath = []
    firePath.extend(find_side_neighbour(x, y, 1))
    q = random.randint(0, len(firePath) - 1)
    #print(firePath[q])
    a,b = firePath[q]
    return a,b

def bot_1(x, y):
    bothPath = []
    bothPath.extend(find_side_neighbour(x, y, 2))
    q = random.randint(0, len(bothPath) - 1)
    #print(firePath[q])
    a,b = bothPath[q]
    return a,b

x_bot, y_bot = bot_open_Startposition()
x_button, y_button = button_open_position()
x_fire, y_fire = button_open_position()

grid[x_bot][y_bot] = "P"
grid[x_button][y_button] = "B"
grid[x_fire][y_fire] = "F"

print(fire(x_fire, y_fire))

print(bot_1(x_bot, y_bot))

for x in grid:
    print(' '.join(x))
print()
