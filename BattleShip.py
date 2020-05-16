import random
from Ship import Ship
from Bot_Logic import Bot_Logic

letters = ['a','b','c','d','e','f','g','h','i','j']
numbers = "0 1 2 3 4 5 6 7 8 9 10"
lengths=[5,4,3,3,2]
directions = ["up","down","left","right"]

bot_ships=[]
my_ships=[]

bot_logic = Bot_Logic()

def play_game():
    place_ships()
    place_bot_ships()
    print("You start.")
    while(not game_lose() and not game_win()):
        print_bot_board(bot_board) 
        take_turn()
        bot_turn()
        print("Your turn.")


def test_game(bot_ships):
    place_bot_ships()
    
    for ship in bot_ships:
        my_ships.append(Ship(ship.get_coords()))
    bot_ships = []
    for i in range(0,len(bot_board)):
        for j in range(0,len(bot_board[i])):
            for k in range(0,len(bot_board[i][j])):
                my_board[i][j][k]=bot_board[i][j][k]
    place_bot_ships()

    print("You start.")
    while(not game_lose() and not game_win()):
        print_bot_board(bot_board) 
        take_turn()
        bot_turn()
        print("Your turn.")

def print_my_board(board):
    grid=[]
    grid.append(numbers)
    num = 0
    for line in board:
        a = letters[num]
        for spot in line:
            if spot[0] and spot[1]:
                a += " " + "X"
            elif spot[0]:
                a += " " + "&" 
            elif spot[1]:
                a += " " + "O"     
            else:
                a += " " + "_"             
        grid.append(a)
        num = num + 1
    for t in grid:
        print(t)


def print_bot_board(board):
    grid=[]
    grid.append(numbers)
    num = 0
    for line in board:
        a = letters[num]
        for spot in line:
            if spot[0] and spot[1]:
                a += " " + "X"
            elif spot[1]:
                a += " " + "O"     
            else:
                a += " " + "_"   
        grid.append(a)
        num += 1
    for t in grid:
        print(t)


def blank_board():
    board = []
    for _ in range(0,10):
        line = []
        for _ in range(0,10):
            line.append([False,False])
        board.append(line)
    return board  

my_board = blank_board()
bot_board = blank_board()    


def place_bot_ships():
    for ship in lengths:
        place_bot_ship(random.randint(0,9),random.randint(0,9),ship,bot_board)   


def place_bot_ship(let,num,length,board):
    direction = directions[random.randint(0,3)]
    count = 0
    while ship_block_error(let,num,direction,length,board) and count < 5:
        direction = directions[random.randint(0,3)]
        count += 1
    if ship_block_error(let,num,direction,length,board) and count > 4: 
        place_bot_ship(random.randint(0,9),random.randint(0,9),length,board)    
    else:
        put_ship_on_board(let,num,direction,length,board,True)  
  

def place_ships():
    for ship_length in lengths:
        place_ship(ship_length,my_board)
        print_my_board(my_board)    
        

def place_ship(ship_length,ship_board):
    ship_length_str = str(ship_length)
    ship_coord = input("Enter the coordinate for your " +ship_length_str+ " long ship: ").lower()
    num = 0
    for letter in letters:
        if ship_coord[0:1] == letter:
            coord_let = num
        num += 1   
    coord_num = int(ship_coord[1:]) - 1
    if ship_board[coord_let][coord_num][0]:
        print("There is already a ship in this location.")
        place_ship(ship_length,ship_board)
    else: 
        ship_dir = input("Your coordinates are " + ship_coord + ". Enter the direction of your " +ship_length_str+ " long ship: ").lower()     
        while ship_dir != "down" and ship_dir != "up" and ship_dir != "left" and ship_dir != "right": 
            ship_dir = input("Your entry is invalid. Please enter either up, down, left, or right for you ship orientation: ").lower()
        if ship_block_error(coord_let,coord_num,ship_dir,ship_length,ship_board):
            print("There is either already a ship in this location, or this location is out of bounds.")
            print("Please choose a new ship location.")
            place_ship(ship_length,ship_board)
        else:
            put_ship_on_board(coord_let,coord_num,ship_dir,ship_length,ship_board,False)


def put_ship_on_board(let,num,dir,length,board,bot):
    coordinates = ship_coordinates(let,num,dir,length)
    for coord in coordinates:    
        board[coord[0]][coord[1]][0]  = True 
    if bot:
        bot_ships.append(Ship(coordinates)) 
    else:
        my_ships.append(Ship(coordinates))            


def ship_block_error(let,num,dir,length,board):
    coordinates = ship_coordinates(let,num,dir,length)
    for coord in coordinates:
        if coord[0] not in range(0,10) or coord[1] not in range(0,10):
            return True
        elif board[coord[0]][coord[1]][0]:
            return True    
    return False    


def ship_coordinates(let,num,dir,len):
    coordinates = []
    let_coord = input_dir(dir)[0]
    num_coord = input_dir(dir)[1]
    for _ in range (0,len):    
        coordinates.append([let,num])
        let += let_coord
        num += num_coord  
    return coordinates

def input_dir(dir):   
    num_coord = 0 
    let_coord = 0
    if dir == "up":
        let_coord = -1
    elif dir == "down":
        let_coord = 1 
    elif dir == "left":
        num_coord = -1   
    elif dir == "right":
        num_coord = 1  
    return [let_coord,num_coord]    

def take_turn():
    shot = input("Enter the coordinates of your shot: ")
    num = 0
    for letter in letters:
        if shot[0:1] == letter:
            let = num
        num += 1   
    num = int(shot[1:]) - 1
    bot_board[let][num][1]=True
    print_bot_board(bot_board)  
    if bot_board[let][num][0]:
        if hit_check_sunk(let,num,False):
            print("Hit and sunk!")
        else:
            print("That's a hit!")   
    else:    
        print("That's a miss.")
    print("Your opponent is taking their turn.")

def hit_check_sunk(let,num,bot):    
    c = [let,num]
    if bot:
        for ship in my_ships:
            if c in ship.get_coords():
                ship.hit()
                if ship.check_sunk():
                    return True
                else:
                    return False    
    else:
         for ship in bot_ships:
            if c in ship.get_coords():
                ship.hit()
                if ship.check_sunk():
                    return True
                else:
                    return False          

        
def bot_turn():
    if not bot_logic.get_bot_turn_counter():
        let = random.randint(0,9)
        num = random.randint(0,9)
        if my_board[let][num][1]:
            bot_turn()
        else:    
            my_board[let][num][1]=True  
            print_my_board(my_board)  
            if my_board[let][num][0]:     
                hit_check_sunk(let,num,True)
                bot_logic.set_first_bot_hit([let,num])
                bot_logic.set_last_bot_hit([let,num])
                bot_logic.set_bot_turn_counter(True)
                print("Your ship was hit!")
            else:
                print("They missed.")    
    else:
        smart_bot_hit()
     

def smart_bot_hit():
    if bot_logic.get_bot_dir() == "":
        dir = directions[random.randint(0,3)]
    else:
        dir = bot_logic.get_bot_dir()

    let_dir = input_dir(dir)[0]
    num_dir = input_dir(dir)[1]
    if bot_logic.get_last_bot_hit()[0]+let_dir not in range(0,10) or bot_logic.get_last_bot_hit()[1]+num_dir not in range(0,10) or my_board[bot_logic.get_last_bot_hit()[0]+let_dir][bot_logic.get_last_bot_hit()[1]+num_dir][1]:
        if bot_logic.get_last_bot_hit() == bot_logic.get_first_bot_hit():
            smart_bot_hit()
        elif bot_logic.get_turn_around_count() == 1:   
            bot_logic.reset()
            bot_turn() 
        else:    
            turn_around() 
            smart_bot_hit()
    else:             
        my_board[bot_logic.get_last_bot_hit()[0]+let_dir][bot_logic.get_last_bot_hit()[1]+num_dir][1] = True 
        print_my_board(my_board)   
        if my_board[bot_logic.get_last_bot_hit()[0]+let_dir][bot_logic.get_last_bot_hit()[1]+num_dir][0]:
            if hit_check_sunk(bot_logic.get_last_bot_hit()[0]+let_dir,bot_logic.get_last_bot_hit()[1]+num_dir,True):
                bot_logic.reset()
                print("Your ship was sunk!")
            else:
                bot_logic.set_last_bot_hit([bot_logic.get_last_bot_hit()[0]+let_dir,bot_logic.get_last_bot_hit()[1]+num_dir])
                bot_logic.set_bot_dir(dir)
                print("Your ship was hit!")   
                print(dir)
        else:
            if bot_logic.get_bot_dir() != "":
                if bot_logic.get_turn_around_count() == 1:
                    bot_logic.reset()   
                else:
                    turn_around() 
            print("They missed")    
        

def turn_around():
    if bot_logic.get_bot_dir() == "up":
        bot_logic.set_bot_dir("down")
    elif bot_logic.get_bot_dir() == "down":
        bot_logic.set_bot_dir("up")
    elif bot_logic.get_bot_dir() == "left":
        bot_logic.set_bot_dir("right")
    elif bot_logic.get_bot_dir() == "right":
        bot_logic.set_bot_dir("left")
    bot_logic.set_last_bot_hit(bot_logic.get_first_bot_hit())
    bot_logic.set_turn_around_count(1)

def game_win():
    for ship in bot_ships:
        if not ship.check_sunk():
            return False
    print("You win!")
    return True        

def game_lose():
    for ship in my_ships:
        if not ship.check_sunk():
            return False
    print("You lose.")
    return True         


#test_game(bot_ships)
play_game()





    
  










