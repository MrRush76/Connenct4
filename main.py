Board = [["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["A", "B", "C", "D", "E"]]

def Show_Board():
    global Board
    for row in range(0, 6):
        for column in range(0, 5):
            print(Board[row][column], "    ", end='')
        print("\n")

def Update_Board(symbol, column):
    global Board
    for row in range(4, -1, -1):
        if Board[row][column] == "0":
            Board[row][column] = symbol
            break

def IsWinner():
    global Board
    for row in range(5):
        for col in range(2):
            if Board[row][col] == Board[row][col+1] == Board[row][col+2] == Board[row][col+3] != "0":
                return True
    for col in range(5):
        for row in range(2):
            if Board[row][col] == Board[row+1][col] == Board[row+2][col] == Board[row+3][col] != "0":
                return True
    for row in range(2):
        for col in range(2):
            if Board[row][col] == Board[row+1][col+1] == Board[row+2][col+2] == Board[row+3][col+3] != "0":
                return True
    for row in range(3, 5):
        for col in range(2):
            if Board[row][col] == Board[row-1][col+1] == Board[row-2][col+2] == Board[row-3][col+3] != "0":
                return True
    return False

def play():
    Show_Board()
    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")
    print(f"{player1} will be Y and {player2} will be R")
    winner = False
    attempt = 0
    while not winner:
        if attempt % 2 == 0:
            symbol = "Y"
            player = player1
        else:
            symbol = "R"
            player = player2
        column = input(f"{player}, choose a column (A, B, C, D, E): ").upper()
        column_index = ord(column) - ord('A')
        Update_Board(symbol, column_index)
        Show_Board()
        winner = IsWinner()
        if winner:
            print(f"Congratulations {player}, you have won!")
        attempt += 1

play()
