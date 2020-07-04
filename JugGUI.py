from tkinter import *
from PIL import ImageTk, Image
from JugClass import Jug
from JugGameClass import Jug_Game
import tkinter.messagebox

# Create main window
tk = Tk()
tk.geometry('370x360')
# Set window title
tk.title("Jug Puzzle Game")
action, fromJug = 'None', None

# Setup Game
jug1, jug2 = Jug(3), Jug(5)
jug_game = Jug_Game(jug1, jug2)

def updateJugGraphic():
    jug1text = 'JugImages/Jug1Fill' + str(jug1.amount) + '.png'
    jug2text = 'JugImages/Jug2Fill' + str(jug2.amount) + '.png'

    jug1img = ImageTk.PhotoImage(Image.open(jug1text))
    jug1_button.configure(image=jug1img)
    jug1_button.image = jug1img

    jug2img = ImageTk.PhotoImage(Image.open(jug2text))
    jug2_button.configure(image=jug2img)
    jug2_button.image = jug2img

    jug1_text.set('Amount: ' + str(jug1.amount))
    jug2_text.set('Amount: ' + str(jug2.amount))
# Function to complete game moves and updated button text as required
def jugClick(button,jug):
    global action, fromJug
    if action == 'Fill':
        jug.fill()
    elif action == 'Empty':
        jug.empty()
    elif 1:
        if fromJug == None:
            feedback_var.set('Select which jug to transfer to')
            fromJug = jug
        else:
            jug_game.transfer(fromJug,jug)
            feedback_var.set('Move your move.')
            fromJug=None
    updateJugGraphic()
    checkForWin()
    if action == 'Fill' or action == 'Empty':
        feedback_var.set('Move your move.')
    action = 'None'

def buttonClick(buttons):
    global action
    if buttons['text'] == 'Fill':
        action = 'Fill'
        feedback_var.set('Select a jug to fill.')
    if buttons['text'] == 'Empty':
        action = 'Empty'
        feedback_var.set('Select a jug to empty.')
    if buttons['text'] == 'Reset Game':
        jug_game.reset()
        updateJugGraphic()

# Function to check WIN condition
def checkForWin():
    if jug_game.is_win():
        tkinter.messagebox.showinfo("The Game is Over", 'Congrats, you\'ve won!')
        tk.quit()

# Game Feedback Label
feedback_var = StringVar()
feedback_var.set('Welcome to Jug Puzzle')
feedback_label = Label(textvariable=feedback_var)
feedback_label.grid(row=0, column=0, columnspan=2)

# Jug Text Amount

jug1_text = StringVar()
jug1_text.set('Amount: 0')
jug1_amount_label = Label(textvariable=jug1_text)
jug1_amount_label.grid(row=1,column=0)


jug2_text = StringVar()
jug2_text.set('Amount: 0')
jug2_amount_label = Label(textvariable=jug2_text)
jug2_amount_label.grid(row=1,column=1)

# Jug Graphics

jug1_img = ImageTk.PhotoImage(Image.open('JugImages/Jug1Fill0.png'))
jug1_button = Button(tk, image=jug1_img, command=lambda: jugClick(jug1_button, jug1))
jug1_button.grid(row=2,column=0)

jug2_img = ImageTk.PhotoImage(Image.open('JugImages/Jug2Fill0.png'))
jug2_button = Button(tk, image=jug2_img, command=lambda: jugClick(jug2_button, jug2))
jug2_button.grid(row=2,column=1)

# Fill Button Moves
B1 = Button(tk, text='Fill', height=2, width=20, command=lambda: buttonClick(B1))
B1.grid(row=3, column=0)

B2 = Button(tk, text='Empty', height=2, width=20, command=lambda: buttonClick(B2))
B2.grid(row=3, column=1)

B3 = Button(tk, text='Reset Game', fg='red', height=1, width=40,  command=lambda: buttonClick(B3))
B3.grid(row=4, column=0, columnspan=2)

tk.mainloop()
