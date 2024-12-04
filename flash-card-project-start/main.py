from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    window.after(3000, func=card_flip)


def card_flip():
    canvas.itemconfig(word_text,text=current_card["English"], fill="white")
    canvas.itemconfig(lang_text,text="English", fill="white")
    canvas.itemconfig(canvas_image, image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    print(len(to_learn))
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer =window.after(3000, func=card_flip)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_back)


card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0,row=0,columnspan=2)

rightimg = PhotoImage(file="images/right.png")
right= Button(image=rightimg, highlightthickness=0,command=is_known)
right.grid(column=0,row=1)

wrongimg = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrongimg, highlightthickness=0,command=next_card)
wrong.grid(column=1,row=1)

lang_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

next_card()

window.mainloop()