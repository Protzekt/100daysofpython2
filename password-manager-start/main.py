from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_letters)]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    passE.insert(0, password)
    pyperclip.copy(password)

# password = ""
    # for char in password_list:
    #   password += char



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = webE.get()
    email = emailE.get()
    password = passE.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0:
        messagebox.showerror(title="Oops", message="The website field has been left empty.")
    elif len(email) == 0:
        messagebox.showerror(title="Oops", message="The email field has been left empty.")
    elif len(password) == 0:
        messagebox.showerror(title="Oops", message="The password field has been left empty.")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            webE.delete(0, END)
            passE.delete(0, END)

def find_password():
    website = webE.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPasswrod: {password}")
        else:
            messagebox.showinfo(title="Error", meesage=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #



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
canvas.grid(column=1, row=0)

# Labels

webL = Label(text="Website:", bg="white")
webL.grid(column=0, row=1)
emaiL = Label(text="Email/Password:", bg="white")
emaiL.grid(column=0, row=2)
passL = Label(text="Password:", bg="white")
passL.grid(column=0, row=3)

# Entries
webE = Entry(bg="white", width=30)
webE.focus()
webE.grid(columnspan=2, column=1, row=1)
emailE = Entry(bg="white", width=30)
emailE.grid(columnspan=2, column=1,row=2)
emailE.insert(0, "kostadiko@gmail.com")
passE = Entry(bg="white", width=25)

passE.grid(column=1, row=3)

# Buttons

genB = Button(text="Generate Password", command=gen_pass)
genB.grid(column=2, row=3)

addB = Button(text="Add", width=30, command=save_data)
addB.grid(columnspan=2, column=1, row=4)

searchB = Button(text="Search",command=find_password)
searchB.grid(column=2,row=1)

window.mainloop()