# Create 2d lists for minesweeper games
game_1 = [["#", "-"],
          ["-", "-"]]
game_2 = [["-", "#", "-"],
          ["#", "-", "-"],
          ["-", "-", "#"]]
game_3 = [["#", "-", "#", "-"],
          ["#", "-", "-", "-"],
          ["-", "-", "#", "#"],
          ["-", "#", "-", "-"]]
game_4 = [["#", "-", "-", "#", "-"],
          ["-", "#", "-", "-", "#"],
          ["-", "-", "#", "-", "-"],
          ["#", "-", "-", "#", "-"],
          ["-", "-", "-", "-", "-"]]
game_5 = [["#", "-", "-", "-", "#", "-"],
          ["-", "#", "-", "#", "-", "-"],
          ["-", "-", "-", "#", "-", "-"],
          ["-", "#", "-", "#", "-", "-"],
          ["-", "-", "-", "-", "#", "-"],
          ["-", "-", "-", "-", "#", "-"]]

# Request user input to choose game, with quick loop to make sure that a valid game is selected
game_number = input("Please enter the number of the game you would like to play (1-5) ")
valid_selection = False
if game_number == "1" or game_number == "2" or game_number == "3" or game_number == "4" or game_number == "5":
    valid_selection = True
while not valid_selection:
    game_number = input("Selection not recognised, please try again ")
    if game_number == "1" or game_number == "2" or game_number == "3" or game_number == "4" or game_number == "5":
        valid_selection = True

# Generate game grid based on user selection
if game_number == "1":
    grid = game_1[:]
elif game_number == "2":
    grid = game_2[:]
elif game_number == "3":
    grid = game_3[:]
elif game_number == "4":
    grid = game_4[:]
elif game_number == "5":
    grid = game_5[:]

# Use loop to determine number of columns in the game grid, then generate an equivalent grid with zeros for every item
rows = len(grid)
cols = 0
for i in range(rows):
    cols = len(grid[i])
output = [[0] * cols for _ in range(rows)]

# The big loop that does everything else:
for i in range(rows):
    for j in range(cols):
        # If the list entry is "#" then the value in its position on the output grid will be increased by 1000, and each
        # entry around it will be increased by 1 (with some conditions)
        if grid[i][j] == "#":
            # First scenario is that neither i nor j equal 0
            if i != 0 and j != 0:
                output[i-1][j-1] += 1
                output[i][j-1] += 1
                output[i - 1][j] += 1
                output[i][j] += 1000
                # Secondary scenarios within this is are that either i or j can equal rows-1 or cols-1 respectively
                # the conditions below deal with each of these situations
                if i == (rows - 1) and j == (cols - 1):
                    pass
                elif i == (rows - 1) and j != (cols - 1):
                    output[i - 1][j + 1] += 1
                    output[i][j + 1] += 1
                elif i != (rows - 1) and j == (cols - 1):
                    output[i + 1][j - 1] += 1
                    output[i + 1][j] += 1
                else:
                    output[i + 1][j + 1] += 1
                    output[i - 1][j + 1] += 1
                    output[i][j + 1] += 1
                    output[i + 1][j - 1] += 1
                    output[i + 1][j] += 1
            # Second scenario is that i = 0, but j does not
            elif i == 0 and j != 0:
                output[i][j] += 1000
                output[i][j - 1] += 1
                # Again with secondary scenarios within this for when either i or j equal rows-1 or cols-1
                # respectively, and the conditions below deal with each of these situations
                if i == (rows - 1) and j == (cols - 1):
                    pass
                elif i == (rows - 1) and j != (cols - 1):
                    output[i][j + 1] += 1
                elif i != (rows - 1) and j == (cols - 1):
                    pass
                else:
                    output[i + 1][j - 1] += 1
                    output[i + 1][j] += 1
                    output[i + 1][j + 1] += 1
                    output[i][j + 1] += 1
            # Third scenario is that j = 0, but i does not
            elif i != 0 and j == 0:
                output[i - 1][j] += 1
                output[i][j] += 1000
                # Again with secondary scenarios within this for when either i or j equal rows-1 or cols-1
                # respectively, and the conditions below deal with each of these situations
                if i == (rows - 1) and j == (cols - 1):
                    pass
                elif i == (rows - 1) and j != (cols - 1):
                    output[i - 1][j + 1] += 1
                    output[i][j + 1] += 1
                elif i != (rows - 1) and j == (cols - 1):
                    output[i + 1][j] += 1
                else:
                    output[i + 1][j + 1] += 1
                    output[i - 1][j + 1] += 1
                    output[i][j + 1] += 1
                    output[i + 1][j] += 1
            # Last scenario is that both i and j are 0
            elif i == 0 and j == 0:
                output[i][j] += 1000
                # Again with secondary scenarios within this for when either i or j equal rows-1 or cols-1
                # respectively, and the conditions below deal with each of these situations
                if i == (rows - 1) and j == (cols - 1):
                    pass
                elif i == (rows - 1) and j != (cols - 1):
                    output[i][j + 1] += 1
                elif i != (rows - 1) and j == (cols - 1):
                    output[i + 1][j] += 1
                else:
                    output[i + 1][j + 1] += 1
                    output[i][j + 1] += 1
                    output[i + 1][j] += 1

# Quick loop to convert values greater than or equal ot 1000 in output to "#"
for i in range(rows):
    for j in range(cols):
        if output[i][j] >= 1000:
            output[i][j] = "#"

# Print game grid and output grid - printed using loops to display over multiple lines
for line in grid:
    print(line)
for line in output:
    print(line)
