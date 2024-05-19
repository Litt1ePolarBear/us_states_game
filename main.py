import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guessed_state = []
state_list = data["state"].to_list()

while len(guessed_state) <50:
    answer_state = screen.textinput(title=f"{len(guessed_state)} / 50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in state_list:
        guessed_state.append(answer_state)
        state_list.remove(answer_state)
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        xcor = int(data[data.state == answer_state].x)
        ycor = int(data[data.state == answer_state].y)
        state_data = data[data.state == answer_state]
        state_name.goto(x=xcor, y=ycor)
        state_name.write(answer_state)


learning_file = {
    "states you missed": [state_list],
    "states you saved": [guessed_state]
}

states_to_learn = pandas.DataFrame(learning_file)
states_to_learn.to_csv("learning_file")