import os
import sys
import random

os.system('cls' if os.name == 'nt' else 'clear')
board = [" "," "," "," "," "," "," "," "," "]
red_x = "\033[31mx\033[37m"
blue_o = "\033[34mo\033[37m"
def update_board ():
    print(" -----------")
    print("|" , board[0], "|" , board[1] , "|", board[2] , "|")
    print(" -----------")
    print("|" , board[3], "|" , board[4] , "|" , board[5] ,"|")
    print(" -----------")
    print("|" , board[6], "|" , board[7] , "|" , board[8] ,"|")
    print(" -----------")

def free_space():
    free_space = False
for y in board:
    value = y
    if value == red_x :
        free_space = False
        break
    elif value == blue_o: 
        free_space = False
        break
    elif value == " ": 
        free_space= True
        break
    else :
        free_space= True
        break


def choose_move():
    while free_space == True :
        user_choice = input("Where do you want to put \033[31mx\033[37m?(between 1-9) ")
        user_choice = int(user_choice)-1
        if ( int(user_choice) < 0 or int(user_choice) > 8 ) :
            print("between 1-9")
        elif board[int(user_choice)] == red_x or board[int(user_choice)] == blue_o  :
            print("Not an empty space!")
        else :
            board[int(user_choice)] = red_x
            os.system('cls' if os.name == 'nt' else 'clear')
            return

def ai_move():
    while free_space == True :
        a = random.randint(0, 8) 
        if board[int(a)] == red_x or board[int(a)] == blue_o  :
            a = random.randint(0, 8)
        else :
            board[int(a)] = blue_o
            os.system('cls' if os.name == 'nt' else 'clear')
            break

"""def ai_hard_move(): #work in progress :(
    while free_space == True :
        for i in range(len(board)):
            if board[int(i)] == red_x and board[int(i + 1)] == red_x and i <= 5 :
                board[int(i+3)] = blue_o
            elif board[int(i)] == red_x and board[int(i + 3)] == red_x and i <= 2 :
                board[int(i+6)] = blue_o
            elif board[int(i)] == red_x and board[int(i + 4)] == red_x and i == 0 :
                board[int(i+8)] = blue_o
            elif board[int(i+2)] == red_x and board[int(i + 4)] == red_x and i <= 2 :
                board[int(i+6)] = blue_o 
            elif board[int(i)] == red_x and board[int(i + 4)] == red_x and i == 0 :
                board[int(i+8)] = blue_o  
            elif board[int(i)] == blue_o and board[int(i + 1)] == blue_o and i <= 5  :
                board[int(i+3)] = blue_o
            elif board[int(i)] == blue_o and board[int(i + 3)] == blue_o and i == 0 :
                board[int(i+6)] = blue_o
            elif board[int(i)] == blue_o and board[int(i + 4)] == blue_o and i == 0 :
                board[int(i+8)] = blue_o
            elif board[int(i+2)] == blue_o and board[int(i + 4)] == blue_o and i <= 2 :
                board[int(i+6)] = blue_o 
            elif board[int(i)] == blue_o and board[int(i + 4)] == blue_o and i == 0 :
                board[int(i+8)] = blue_o                               
            else :
                board[int(random.randint(0, 8))] = blue_o
                os.system('cls' if os.name == 'nt' else 'clear')
                break"""           

def player_win():
    if board[0] == red_x and board[1] == red_x and board[2] == red_x :
        return True
    if board[3] == red_x and board[4] == red_x and board[5] == red_x :
        return True
    if board[6] == red_x and board[7] == red_x and board[8] == red_x :
        return True
    if board[0] == red_x and board[4] == red_x and board[8] == red_x :
        return True
    if board[2] == red_x and board[4] == red_x and board[6] == red_x :
        return True
    if board[0] == red_x and board[3] == red_x and board[6] == red_x :
        return True
    if board[1] == red_x and board[4] == red_x and board[7] == red_x :
        return True
    if board[2] == red_x and board[5] == red_x and board[8] == red_x :
        return True   
    else :
        return False

def player_loose():
    if board[0] == blue_o and board[1] == blue_o and board[2] == blue_o :
        return True
    if board[3] == blue_o and board[4] == blue_o and board[5] == blue_o :
        return True
    if board[6] == blue_o and board[7] == blue_o and board[8] == blue_o :
        return True
    if board[0] == blue_o and board[4] == blue_o and board[8] == blue_o :
        return True
    if board[2] == blue_o and board[4] == blue_o and board[6] == blue_o :
        return True
    if board[0] == blue_o and board[3] == blue_o and board[6] == blue_o :
        return True
    if board[1] == blue_o and board[4] == blue_o and board[7] == blue_o :
        return True
    if board[2] == blue_o and board[5] == blue_o and board[8] == blue_o :
        return True
    else :
        return False



def draw():
    for value in board:
        if value == red_x :
            pass
        elif value == blue_o: 
            pass
        elif value == " ": 
            return False 
    return True
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_screen():
    print('''    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~TICTACTOE~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ~~~~~~~~~~~created by: Lengyel Noemi - Kovacs Adam~~~~~~~~~~~~\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ~~~~~Controls: press 1-9 on your keyboard, then press Enter~~~\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~[1][2][3]~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~[4][5][6]~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~[7][8][9]~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~MAIN MENU~~~~~~~~~~~~~~~~~~~~~~~~~~~\n

                        q ~ Quit the game
                        w ~ Play with the computer
                        e ~ Play with a friend
    ''')
    while True :
        start_option = input("Press the option's letter: ")
        if start_option == "q" :
            sys.exit()
        elif start_option == "w" :
            diff_opt = input("EASY:e or HARD:h ?")
            if diff_opt == "e":
                vs_ai()
            elif diff_opt == "h":
                decision = input("In progress, sorry :c ~~~~~ MAIN MENU:y ~ QUIT:q  :  ")
                if decision == "y" :
                    clear_board()
                    start_screen()
                elif decision == "q" :
                    sys.exit()
                return ()
            else:
                pass
        elif start_option == "e" :
            pvp()

def clear_board():
    global board
    board = [" "," "," "," "," "," "," "," "," "]

def vs_ai(): 
    while True :
        update_board()
        choose_move()
        update_board()
        if player_win() == True :
            print("\n    ~~~~~~~~ \n     <|GG|> \n   \033[31mPlayer 1 WON\033[37m \n    :):):):) \n    ~~~~~~~~\n")
            decision = input("END GAME ~~~~~ MAIN MENU:y ~ QUIT:q  :  ")
            if decision == "y" :
                clear_board()
                start_screen()
            elif decision == "q" :
                sys.exit()
            break
        if draw() == True :
            print("\n    ~~~~~~~~~ \n     <|GG|> \n    ITS A DRAW\n    :|:|:|:|\n    ~~~~~~~~~\n")
            decision = input("END GAME ~~~~~ MAIN MENU:y ~ QUIT:q  :  ")
            if decision == "y" :
                clear_board()
                start_screen()
            elif decision == "q" :
                sys.exit()
            break
            break
        clear_screen()
        ai_move()
        update_board()
        if player_loose() == True :
            print("\n    ~~~~~~~~~ \n     <|GG|> \n    \033[34mSKYNET WON\033[37m\n    :(:(:(:(\n    ~~~~~~~~~\n")
            decision = input("END GAME ~~~~~ MAIN MENU:y ~ QUIT:q  :  ")
            if decision == "y" :
                clear_board()
                start_screen()
            elif decision == "q" :
                sys.exit()
            break
        clear_screen()

def vs_ai_hard(): 
    while True :
        update_board()
        choose_move()
        update_board()
        if player_win() == True :
            print("\n    ~~~~~~~~ \n     <|GG|> \n   \033[31mPlayer 1 WON\033[37m \n    :):):):) \n    ~~~~~~~~\n")
            decision = input("END GAME ~~~~~ MAIN MENU:y ~ QUIT:q  :  ")
            if decision == "y" :
                clear_board()
                start_screen()
            elif decision == "q" :
                sys.exit()
            break
        if draw() == True :
            print("\n    ~~~~~~~~~ \n     <|GG|> \n    ITS A DRAW\n    :|:|:|:|\n    ~~~~~~~~~\n")
            decision = input("END GAME ~~~~~ MAIN MENU:y ~ QUIT:q  :  ")
            if decision == "y" :
                clear_board()
                start_screen()
            elif decision == "q" :
                sys.exit()
            break
            break
        clear_screen()
        ai_hard_move()
        update_board()
        if player_loose() == True :
            print("\n    ~~~~~~~~~ \n     <|GG|> \n    \033[34mSKYNET WON\033[37m\n    :(:(:(:(\n    ~~~~~~~~~\n")
            decision = input("END GAME ~~~~~ MAIN MENU:y ~ QUIT:q  :  ")
            if decision == "y" :
                clear_board()
                start_screen()
            elif decision == "q" :
                sys.exit()
            break
        clear_screen()        

def player_1():
    while free_space == True :
        user_choice = input("Where do you want to put \033[31mx\033[37m?(between 1-9) ")
        user_choice = int(user_choice)-1
        if ( int(user_choice) < 0 or int(user_choice) > 8 ) :
            print("between 1-9")
        elif board[int(user_choice)] == red_x or board[int(user_choice)] == blue_o  :
            print("Not an empty space!")
        else :
            board[int(user_choice)] = red_x
            os.system('cls' if os.name == 'nt' else 'clear')
            return

def player_2():
    while free_space == True :
        user_choice = input("Where do you want to put \033[34mo\033[37m?(between 1-9) ")
        user_choice = int(user_choice)-1
        if ( int(user_choice) < 0 or int(user_choice) > 8 ) :
            print("between 1-9")
        elif board[int(user_choice)] == red_x or board[int(user_choice)] == blue_o  :
            print("Not an empty space!")
        else :
            board[int(user_choice)] = blue_o
            os.system('cls' if os.name == 'nt' else 'clear')
            return

def pvp():
    while True :
        update_board()
        player_1()
        update_board()
        if player_win() == True :
            print("\n    ~~~~~~~~ \n     <|GG|> \n   \033[31mPlayer 1 WON\033[37m \n    :):):):) \n    ~~~~~~~~\n")
            decision = input("END GAME ~~~~~ MAIN MENU:y ~ QUIT:q  :  ")
            if decision == "y" :
                clear_board()
                start_screen()
            elif decision == "q" :
                sys.exit()
            break
        if draw() == True :
            print("\n    ~~~~~~~~~ \n     <|GG|> \n    ITS A TIE\n    :|:|:|:|\n    ~~~~~~~~~\n")
            decision = input("END GAME ~~~~~ MAIN MENU:y ~ QUIT:q  :  ")
            if decision == "y" :
                clear_board()
                start_screen()
            elif decision == "q" :
                sys.exit()
            break
            break
        clear_screen()
        update_board()
        player_2()
        update_board()
        if player_loose() == True :
            print("\n    ~~~~~~~~ \n     <|GG|> \n   \033[34mPlayer 2 WON\033[37m \n    :):):):) \n    ~~~~~~~~\n")
            decision = input("END GAME ~~~~~ MAIN MENU:y ~ QUIT:q  :  ")
            if decision == "y" :
                clear_board()
                start_screen()
            elif decision == "q" :
                sys.exit()
            break
        clear_screen()
start_screen()