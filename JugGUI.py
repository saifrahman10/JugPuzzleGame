from tkinter import *

import PIL
from PIL import ImageTk, Image
from JugClass import Jug
from JugGameClass import Jug_Game




class JugGameGUI():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title('Jug Puzzle Game')

        self.jug1 = Jug(3)
        self.jug2 = Jug(5)
        self.game = Jug_Game(self.jug1, self.jug2)

        img = Image.open('JugImages/Jug1Fill0.png')
        jug1img = ImageTk.PhotoImage(img)

        self.jug1label = Label(self.root)

        self.jug1label.image = ImageTk.PhotoImage(Image.open('JugImages/Jug1Fill0.png'))
        self.jug1label.pack()
        #self.jug1label = Label(self, image=jug1img)
        #self.jug1label.pack()

gameview = JugGameGUI()
gameview.root.mainloop()