# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

#
# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo)
canvas.grid(column=1, row=1)

window.mainloop()