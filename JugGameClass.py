from JugClass import Jug


class Jug_Game:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2
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

    def status(self):
        print("Jug 1 is {} units filled and Jug 2 is {} units filled.".format(self.jug1.amount, self.jug2.amount))