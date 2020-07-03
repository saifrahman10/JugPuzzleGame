from JugClass import Jug
from JugGameClass import Jug_Game

def main():
    jug1 = Jug(3)
    jug2 = Jug(5)
    juggame = Jug_Game(jug1, jug2)
    while not juggame.is_win():
        options = "1: Empty jug 1\n2: Empty jug 2\n3: Fill Jug 1\n4: Fill Jug 2\n5: Pour jug 1 into jug 2\n6: Pour jug 2 into jug 1"
        juggame.status()
        move = input("What move would you like to make: ")
        if move == 's':
            juggame.status()
        if move == 'o':
            print(options)
        if move == '1':
            jug1.empty()
        if move == '2':
            jug2.empty()
        if move == '3':
            jug1.fill()
        if move == '4':
            jug2.fill()
        if move == '5':
            juggame.transfer(jug1, jug2)
        if move == '6':
            juggame.transfer(jug2, jug1)
    print("Congratulations you've won!")
main()

# Winning moves:
# 3
# 5
# 3
# 5
# 2
# 5
# 3
# 5