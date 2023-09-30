from tkinter import  *

# Creating a list that holds directions
questions = {
    "(1) When was our first date?" : ["September First", "Mars", "Sike", "cant belive u forgot"],
    "(2) How did I win you over?" : ["Dancing", "Cool Dance Moves", "Food", "Baby Emily Did Everything"]
}

answers = ["Mars", "Dancing"]

# Define a Count (question 1,2,3,4 ect)
count = 0




# Creates root window
root = Tk()

#Creating rot window
root.title("Trivia Game LOLOL")

# Setting Dimensions of window
root.geometry("400x400")

# Creating a label
label = Label(root, text = "Welcome to the Trivia Game")
label.pack()

start_label = Label(root, text = "")
start_label.pack()

question_label = Label(root, text = "")
question_label.pack()


# Defines a Function to display when clicked
def clicked():
    start_button.configure(text = "You Clicked Me!")

# Button widget to start game
start_button = Button(root, text = "Click me plslslsls", 
             fg = "blue", command=clicked)
start_button.pack()


# Closes window after 1 second
root.after(20000,lambda:root.destroy())

root.mainloop()











