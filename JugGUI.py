from tkinter import *
from PIL import ImageTk, Image
from JugClass import Jug
from JugGameClass import Jug_Game
import tkinter.messagebox
# Create main window
tk = Tk()
tk.geometry('375x530')
# Set window title
tk.title("Jug Puzzle Game")
button_click = True
flag = 0

# Setup Game
jug1, jug2 = Jug(3), Jug(5)
jug_game = Jug_Game(jug1, jug2)

# Function to disable Buttons
def disableButton():
    B1.configure(state=DISABLED)
    B2.configure(state=DISABLED)
    B3.configure(state=DISABLED)
    B4.configure(state=DISABLED)
    B5.configure(state=DISABLED)
    B6.configure(state=DISABLED)
    B7.configure(state=DISABLED)
    B8.configure(state=DISABLED)

def updateJugGraphic():
    jug1text = 'JugImages/Jug1Fill' + str(jug1.amount) + '.png'
    jug2text = 'JugImages/Jug2Fill' + str(jug2.amount) + '.png'

    jug1img = ImageTk.PhotoImage(Image.open(jug1text))
    jug1_label.configure(image=jug1img)
    jug1_label.image = jug1img

    jug2img = ImageTk.PhotoImage(Image.open(jug2text))
    jug2_label.configure(image=jug2img)
    jug2_label.image = jug2img
# Function to complete game moves and updated button text as required
def buttonClick(buttons):
    if buttons['text'] == 'Fill Jug 1':
        jug1.fill()
        b1_text.set(str(jug1.amount))
    if buttons['text'] == 'Fill Jug 2':
        jug2.fill()
        b2_text.set(str(jug2.amount))
    if buttons['text'] == 'Empty Jug 1':
        jug1.empty()
        b1_text.set(str(jug1.amount))
    if buttons['text'] == 'Empty Jug 2':
        jug2.empty()
        b2_text.set(str(jug2.amount))
    if buttons['text'] == 'Transfer Jug 1 to Jug 2':
        jug_game.transfer(jug1,jug2)
        b1_text.set(str(jug1.amount))
        b2_text.set(str(jug2.amount))
        checkForWin()
    if buttons['text'] == 'Transfer Jug 2 to Jug 1':
        jug_game.transfer(jug2,jug1)
        b1_text.set(str(jug1.amount))
        b2_text.set(str(jug2.amount))
        checkForWin()
    #updateJugGraphic()
# Function to check WIN condition
def checkForWin():
    if jug_game.is_win():
        tkinter.messagebox.showinfo("The Game is Over", 'Congrats, you\'ve won!')
        tk.quit()

# Jug Graphics
# jug1_img = Image.open('JugImages/Jug1Fill0.png')
# jug1_resize = jug1_img.resize((3000,200), Image.ANTIALIAS)
#
# jug1_img = ImageTk.PhotoImage(jug1_resize)
# jug1_label = Label(tk, image=jug1_img, height=10,width=10)
#
# jug1_label.grid(row=1, column=0)
#
# jug2_img = ImageTk.PhotoImage(Image.open('JugImages/Jug2Fill0.png'))
# jug2_label = Label(tk, image=jug2_img)
# jug2_label.grid(row=1, column=1)

# Jug Button Setup
b1_text = StringVar()
b1_text.set('0')
B1 = Button(tk, textvariable=b1_text, height=4, width=20, command=lambda: buttonClick(B1))
B1.grid(row=2, column=0)

b2_text = StringVar()
b2_text.set('0')
B2 = Button(tk, textvariable=b2_text, height=4, width=20, command=lambda: buttonClick(B2))
B2.grid(row=2, column=1)

# Fill Button Moves
B3 = Button(tk, text='Fill Jug 1', height=4, width=20, command=lambda: buttonClick(B3))
B3.grid(row=3, column=0)

B4 = Button(tk, text='Fill Jug 2', height=4, width=20, command=lambda: buttonClick(B4))
B4.grid(row=3, column=1)

# Empty Button Moves
B5 = Button(tk, text='Empty Jug 1', height=4, width=20, command=lambda: buttonClick(B5))
B5.grid(row=4, column=0)

B6 = Button(tk, text='Empty Jug 2', height=4, width=20, command=lambda: buttonClick(B6))
B6.grid(row=4, column=1)

# Transfer Button Moves
B7 = Button(tk, text='Transfer Jug 1 to Jug 2', height=4, width=20, command=lambda: buttonClick(B7))
B7.grid(row=5, column=0)

B8 = Button(tk, text='Transfer Jug 2 to Jug 1', height=4, width=20, command=lambda: buttonClick(B8))
B8.grid(row=5, column=1)

tk.mainloop()


