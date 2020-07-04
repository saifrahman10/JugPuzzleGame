from tkinter import *

import PIL
from PIL import ImageTk, Image
from JugClass import Jug
from JugGameClass import Jug_Game
import random
import math


class JugGameGUI():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title('Jug Puzzle Game')

        x = random.randrange(2, 25)
        y = random.randrange(2, 25)
        jug1 = Jug(x)
        jug2 = Jug(y)
        win_num = (max(x, y) // math.gcd(x, y)) * max(x, y)
        self.game = Jug_Game(self.jug1, self.jug2, win_num)

        img = Image.open('JugImages/Jug1Fill0.png')
        jug1img = ImageTk.PhotoImage(img)

        self.jug1label = Label(self.root)

        self.jug1label.image = ImageTk.PhotoImage(Image.open('JugImages/Jug1Fill0.png'))
        self.jug1label.pack()
        #self.jug1label = Label(self, image=jug1img)
        #self.jug1label.pack()

gameview = JugGameGUI()
gameview.root.mainloop()
