from JugClass import Jug
from JugGameClass import Jug_Game
from JugGUI import *

def start_game():
    jug1 = Jug(3)
    jug2 = Jug(5)
    juggame = Jug_Game(jug1, jug2)
    while not juggame.is_win():
        options = "1: Empty jug 1\n2: Empty jug 2\n3: Fill Jug 1\n4: Fill Jug 2\n5: Pour jug 1 into jug 2\n6: Pour jug 2 into jug 1"
        juggame.status()
        move = input("What move would you like to make: ")
        options_dict = {
            's': juggame.status,
            'o': lambda: print(options),
            '1': jug1.empty,
            '2': jug2.empty,
            '3': jug1.fill,
            '4': jug2.fill,
            '5': lambda: juggame.transfer(jug1, jug2),
            '6': lambda: juggame.transfer(jug2, jug1)
        }
        
        if move in options_dict:
            options_dict[move]()
    print("Congratulations you've won!")
start_game()

# Winning moves:
# 3
# 5
# 3
# 5
# 2
# 5
# 3
# 5
