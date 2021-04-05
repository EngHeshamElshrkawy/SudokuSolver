

board = [[0,9,0,0,0,6,1,0,0],
 [7,1,0,0,9,0,0,2,8],
 [0,0,8,0,0,0,0,4,9],
 [0,6,0,2,5,0,0,0,1],
 [0,0,0,0,0,0,0,0,0],
 [5,0,0,0,6,9,0,7,0],
 [1,2,0,0,0,0,8,0,0],
 [9,8,0,0,4,0,0,5,2],
 [0,0,5,6,0,0,0,1,0]]





#Prints the board in a more convenient  form instead of line by line.
def prettyPrint():
    global board
    for i in range(9):
        print(*board[i])

#Tests if the given number can be added into the given position
def test(x, y, n):
    global board
    #Tests the row
    for i in range(9):
        if board[i][x] == n:
            return False
    #Tests the column
    for i in range(9):
        if board[y][i] == n:
            return False
    new_x = (x//3)*3 
    new_y = (y//3)*3
    #Tests the square
    for i in range(3):
        for j in range(3):
            if board[new_y + j][new_x + i] == n:
                return False
    return True

#Solves the board
def fill():
    global board
    visited = []
    #Iterates through the board to find all the empty positions
    for i in range(9):
        for j in range(9):
            if board[j][i] == 0:
                visited.append([j, i, 0])
    lst = 0
    #Loops through all the empty positions
    while lst < len(visited):
        x = visited[lst][1]
        y = visited[lst][0]
        n = visited[lst][2]
        if n < 9:
            #Finds a number that can be put in that position
            for i in range(1, 10 - n):
                if test(x, y, n+i):
                    visited[lst][2] = n+i
                    board[y][x] = n+i
                    break
                else:
                    #If no number can be added in that position backtrack to a previous position
                    if n+i == 9:
                        visited[lst][2] = 0
                        board[y][x] = 0
                        lst -= 2
        else:
            visited[lst][2] = 0
            board[y][x] = 0
            lst -= 2
        
        lst += 1
   


fill()
prettyPrint()

