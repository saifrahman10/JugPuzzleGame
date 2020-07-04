from JugClass import Jug


class Jug_Game:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2
        self.instructions = 'Welcome to jug puzzle.\n\nThe objective of this game is to get 4 units into Jug #2.\n\n' \
                            'Your only moves are to fill either jug, empty either jug, or transfer the maximum amount of units possible from one jug to the other\n' \
                            'Good luck!'

    def reset(self):
        self.jug1.amount = 0
        self.jug2.amount = 0
    def is_win(self):
        return self.jug2.amount == 4
    def transfer(self, fromjug, tojug):
        if tojug.amount != tojug.capacity:
            space = tojug.capacity - tojug.amount
            if space >= fromjug.amount:
                tojug.amount += fromjug.amount
                fromjug.empty()
            else:
                tojug.amount += space
                fromjug.amount -= space
        else:
            print("Jug is at full capacity.")