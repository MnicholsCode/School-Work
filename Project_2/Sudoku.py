#*****************************************************************
#Name: load_puzzle()
#Purpose: To read in a text file and parse the data from that file
#*****************************************************************
def load_puzzle(path):
    #Opens the file from the path specified by the user, path is in same directory
    with open(path) as fin:
        contents = fin.read()
    lines = contents.split('\n')
    sudoku = []
    #Loop to read in the elements in lines then split and convert them before appending to list
    for row in lines:
        row_string = row.split()
        row_int = [int(n) for n in row_string]
        sudoku.append(row_int)
    print("Sudoku loaded from", path,"\n")
    return sudoku

#*****************************************************************
#Name: display_puzzle()
#Purpose: takes the information from the matrix and pretty prints
#         an output of the sudoku box
#*****************************************************************
def display_puzzle(puzzle):
    #loop for printing top and medium portions of the board
    for i in range(len(puzzle)):
        if i % 3 == 0:
            print("+" + "-------+"*3)
       #Loop to process and print the values in the text files into the board
        for j in range(len(puzzle[0])):
            char = puzzle[i][j]
            if char == 0:
                char = "."
                
            if j % 3 == 0:
                print("| ", end="")
                
            if j == 8:
                print(char, "|")
            else:
                print(str(char) + " ", end = "")
    #final line of the board
    print("+" + "-------+"*3)

#*****************************************************************
#Name: get_next()
#Purpose: To show what the next available cell is to populate or
#         not
#*****************************************************************
def get_next(row, col):
    if col < 8:
        return row,col+1
    elif col == 8 and row < 8:
        return row+1,0
    elif col == 8 and row == 8:
        return None,None

#*****************************************************************
#Name: get_options()
#Purpose: By checking the row, col and box. this function returns
#         a list of ints, which are our options for placing in that
#         cell.
#*****************************************************************
def get_options(puzzle, row, col):
    if puzzle[row][col] > 0:
        return None
    
    used = []
    #check row
    for i in range(0,9):
        if puzzle[row][i] > 0:
            used.append(puzzle[row][i])
    
    #Check col
    for i in range(0,9):
        if puzzle[i][col] > 0:
            used.append(puzzle[i][col])
    
    #check 3x3 box
    box_x = row // 3                                           #integer division to avoid float
    box_y = col // 3
        
    for i in range(box_x * 3, box_x * 3 + 3):                  #traverse through box elements
        for j in range(box_y * 3, box_y * 3 + 3):
            if puzzle[i][j] > 0:
                used.append(puzzle[i][j])
    options = []
    for i in range(1,10):
        if i not in used:
            options.append(i)
    return options

#*****************************************************************
#Name: copy_puzzle()
#Purpose: Makes a copy of the current puzzle
#*****************************************************************
def copy_puzzle(puzzle):
    new_puzzles = []
    for i in range(0,len(puzzle)):
        new_copy = puzzle[i].copy()
        new_puzzles.append(new_copy)
    return new_puzzles

#*****************************************************************
#Name: solve()
#Purpose: to solve the sudoku, it takes in the current cell and if
#         that cell is blank (0) then it will get the options and
#         start to solve. This is done through recursion. The idea
#         is to backtrack and find a solution by trying out the options
#         and seeing what works.
#*****************************************************************
def solve(puzzle, row = 0, col = 0):
    #Checking if current cell is not 0, meaning if it already has a value in it
    #if that is the case, we cycle through cells to find a blank (0) value
    if puzzle[row][col] != 0:
        next_row, next_col = get_next(row,col)
        if next_row is None:
            return puzzle
        else:
            return solve(puzzle, next_row, next_col)
            
    #When a blank value is found, we want to know the options available to us
    options = get_options(puzzle, row, col)
    
    if options == []:
        return None

    for cur_opt in options:
        new_puzzle = copy_puzzle(puzzle)
        new_puzzle[row][col] = cur_opt               
        result = solve(new_puzzle, row, col)
            
        if result is not None:
            return result
