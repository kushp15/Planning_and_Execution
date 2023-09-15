import random

D = 100
grid = [["B" for _ in range(D)] for _ in range(D)]
openBlockPosArr = []
deadEndCells = []

randIntX = random.randint(1, D-2)
randIntY = random.randint(1, D-2)
grid[randIntX][randIntY] = "O"
openBlockPosArr.append((randIntX, randIntY))

effX1 = randIntX - 1
effX2 = randIntX + 1
effY1 = randIntY - 1
effY2 = randIntY + 1

# debug info
print("picked: " + "(" + str(randIntX) + ", " + str(randIntY) + ")")

while openBlockPosArr:
    openBlockPosArr = []
    for x in range(effX1, effX2 + 1):
        for y in range(effY1, effY2 + 1):
            openBlockPos = 0
            if grid[x][y] == "B":
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
        print()
        print(openBlockPosArr)
        print()

        randIndex = random.randint(0, len(openBlockPosArr) - 1)
        randIntX, randIntY = openBlockPosArr[randIndex]
        grid[randIntX][randIntY] = "O"

        if 0 < effX1 == randIntX:
            effX1 = randIntX - 1
        if D-1 > effX2 == randIntX:
            effX2 = randIntX + 1
        if 0 < effY1 == randIntY:
            effY1 = randIntY - 1
        if D-1 > effY2 == randIntY:
            effY2 = randIntY + 1

        # debug info
        print()
        for x in grid:
            print(' '.join(x))
        print()

for x in range(D):
    for y in range(D):
        deadEndBlock = 0
        if grid[x][y] == "O":
            a = x + 1
            b = x - 1
            c = y + 1
            d = y - 1
            if 0 <= a <= D - 1 and grid[a][y] == "B":
                deadEndBlock += 1
            if 0 <= b <= D - 1 and grid[b][y] == "B":
                deadEndBlock += 1
            if 0 <= c <= D - 1 and grid[x][c] == "B":
                deadEndBlock += 1
            if 0 <= d <= D - 1 and grid[x][d] == "B":
                deadEndBlock += 1
            if deadEndBlock >= 3:
                deadEndCells.append((x, y))



for x in range(D):
    for y in range(D):
        deadEndBlock = 0
        deadEndBlockArr = []
        if grid[x][y] == "O":
            a = x + 1
            b = x - 1
            c = y + 1
            d = y - 1
            if 0 <= a <= D - 1 and grid[a][y] == "B":
                deadEndBlock += 1
                deadEndBlockArr.append((a, y))
            if 0 <= b <= D - 1 and grid[b][y] == "B":
                deadEndBlock += 1
                deadEndBlockArr.append((b, y))
            if 0 <= c <= D - 1 and grid[x][c] == "B":
                deadEndBlock += 1
                deadEndBlockArr.append((x, c))
            if 0 <= d <= D - 1 and grid[x][d] == "B":
                deadEndBlock += 1
                deadEndBlockArr.append((x, d))
            if deadEndBlock >= 3:
                randIndex = random.randint(0, len(deadEndBlockArr) - 1)
                randIntX, randIntY = deadEndBlockArr[randIndex]
                grid[randIntX][randIntY] = "O"

# debug info
print("Done Opening")
