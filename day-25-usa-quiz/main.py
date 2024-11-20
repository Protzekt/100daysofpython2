import turtle
import pandas
from states import state_namer
correct_guesses = []
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer_state = screen.textinput(title=f"{len(correct_guesses)}", prompt="What's another states name ?").title()

data = pandas.read_csv("50_states.csv")
while len(correct_guesses) < 50:
    for state in data["state"]:
        if answer_state == state:
            print("Your guess is among the 50 States!")
            posx = int(data[data.state == answer_state].x)
            posy = int(data[data.state == answer_state].y)
            state_namer(posx, posy, answer_state)
            correct_guesses.append(answer_state)
screen.exitonclick()
