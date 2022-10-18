from tkinter import *
import random

# Переменные
width = 1200
height = 700
background = 'LemonChiffon'
width_desk = 25
height_desk = 100
fill_left_desk = 'DodgerBlue'
fill_right_desk = 'Red'
fill_ball = '#FFD700'
fill_line = '#000000'
radius = 30
speed_left_desk = 0
speed_right_desk = 0
speed_desks = 20
speed_ball_plus = 1.05
ball_start_x = 12
ball_start_y = 12
ball_finish_speed = 30
ball_x = 12
ball_y = 0
R = width - width_desk
red = 0
blue = 0
boll = "start"
napravlenie = 20
width_repeat = 125
fill_repeat = 'Yellow'

# Само окошко
tk = Tk()
tk.title("Игра " + "Пин Понг")
canvas = Canvas(tk, width=width, height=height, background=background)
canvas.pack()
tk.update()

# Рисуем игровые элементы
left_desk = canvas.create_line(
    width_desk / 2,
    0,
    width_desk / 2,
    height_desk,
    width=width_desk,
    fill=fill_left_desk
)
right_desk = canvas.create_line(
    width - width_desk / 2,
    0,
    width - width_desk / 2,
    height_desk,
    width=width_desk,
    fill=fill_right_desk
)

repeat = canvas.create_line(
    width / 2.65,
    height / 1.4,
    width / 1.6,
    height / 1.4,
    width= width_repeat,
    fill= background
)

repeat_text = canvas.create_text(
    width/2,
    height/1.4,
    text= "repeat",
    font= 'Arial 55',
    fill= background
)

central_line = canvas.create_line(
    width / 2,
    0,
    width / 2,
    height,
    fill=fill_line
)
ball = canvas.create_oval(
    width / 2 - radius,
    height / 2 - radius,
    width / 2 + radius,
    height / 2 + radius,
    fill=fill_ball
)


count_text = canvas.create_text(
    width / 2,
    15,
    # ?????
    text=(blue, red),
    font='Arial 30',
    fill='black'
)
win_text = canvas.create_text(
    width / 2,
    height / 2,
    text="",
    font='Arial 100',
    fill='black'
)

# Функции

# Функция ракеток
def desk():
    # Cловарь
    desks = {left_desk: speed_left_desk, right_desk: speed_right_desk}
    for i in desks:
        canvas.move(i, 0, desks[i])
        if canvas.coords(i)[1] < 0:
            canvas.move(i, 0, -canvas.coords(i)[1])
        elif canvas.coords(i)[3] > height:
            canvas.move(i, 0, height - canvas.coords(i)[3])


canvas.focus_set()


def W_S(event):
    global speed_left_desk
    global speed_right_desk
    if event.keysym == "w":
        speed_left_desk = -speed_desks
    elif event.keysym == "s":
        speed_left_desk = speed_desks
    elif event.keysym == "Up":
        speed_right_desk = -speed_desks
    elif event.keysym == "Down":
        speed_right_desk = speed_desks


canvas.bind("<KeyPress>", W_S)


def stop_W_S(event):
    global speed_left_desk
    global speed_right_desk
    if event.keysym in "ws":
        speed_left_desk = 0
    elif event.keysym in ("Up", "Down"):
        speed_right_desk = 0


canvas.bind("<KeyRelease>", stop_W_S)


def bound(a):
    global ball_start_x
    global ball_start_y
    if a == "desk":
        ball_start_y = random.randrange(-10, 10)
        if abs(ball_start_x) < ball_finish_speed:
            ball_start_x = ball_start_x * (-speed_ball_plus)
        else:
            ball_start_x = -ball_start_x
    else:
        ball_start_y = -ball_start_y


def ball_2():
    left, up, right, down = canvas.coords(ball)
    center = (down + up) / 2
    if right + ball_start_x < R and left + ball_start_x > width_desk:
        canvas.move(ball, ball_start_x, ball_start_y)
    elif left == width_desk or right == R:
        if right > width / 2:
            if canvas.coords(right_desk)[1] < center < canvas.coords(right_desk)[3]:
                bound("desk")
            else:
                count_score("right")
                one()
        else:
            if canvas.coords(left_desk)[1] < center < canvas.coords(left_desk)[3]:
                bound("desk")
            else:
                count_score("left")
                one()

    else:
        if right > width / 2:
            canvas.move(ball, R - right, ball_start_y)
        else:
            canvas.move(ball, width_desk - left, ball_start_y)

    if up + ball_start_y < 0 or down + ball_start_y > height:
        bound("go to else")


def count_score(a):
    global blue, red
    if a == "right":
        blue = blue + 1
        canvas.itemconfigure(count_text, text=(blue, red))
    else:
        red = red + 1
        canvas.itemconfigure(count_text, text=(blue, red))


def one():
    global ball_start_x
    canvas.coords(ball, width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius)
    ball_start_x = -(ball_start_x * napravlenie) / abs(ball_start_x)


# Бесконечный цuкл
def win():
    global boll
    if red == 20:
        canvas.itemconfigure(win_text, text="red win", fill='red')
        canvas.itemconfigure(repeat_text, fill='black')
        canvas.itemconfigure(repeat, fill=fill_repeat)
        boll = "stop"
    if blue == 20:
        canvas.itemconfigure(win_text, text="blue win", fill='blue')
        canvas.itemconfigure(repeat_text, fill='black')
        canvas.itemconfigure(repeat, fill=fill_repeat)
        boll = "stop"


##################
while True:
    desk()
    if boll == "start":
        ball_2()
    win()
    tk.after(30)
    tk.update()
