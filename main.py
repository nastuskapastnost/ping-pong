from tkinter import*
import random
# Переменные
width = 1200
height =700
background = 'LemonChiffon'
width_desk = 25
height_desk = 100
fill_left_desk= 'DodgerBlue'
fill_right_desk= 'Red'
fill_ball = '#FFD700'
fill_line = '#000000'
radius = 30
speed_left_desk = 0
speed_right_desk = 0
speed_desks = 20
speed_ball_plus = 1.05
ball_start_x=20
ball_start_y=20
ball_finish_speed = 40
ball_x=20
ball_y=0
# Само окошко
tk = Tk()
tk.title("Игра " + "Пин Понг")
canvas = Canvas(tk, width=width, height=height, background=background)
canvas.pack()
tk.update()

# Рисуем игровые элементы
left_desk = canvas.create_line(width_desk/2,0,width_desk/2,height_desk,width=width_desk,fill=fill_left_desk)

right_desk = canvas.create_line(width-width_desk/2,0,width-width_desk/2,height_desk,width=width_desk,fill=fill_right_desk)

central_line = canvas.create_line(width/2,0,width/2,height,fill=fill_line)

ball = canvas.create_oval(width/2-radius,height/2-radius,width/2+radius,height/2+radius,fill= fill_ball)

# Функции
# Функция ракеток
def desk ():
    # Cловарь
    desks ={left_desk: speed_left_desk, right_desk: speed_right_desk}
    for i in desks:
        canvas.move(i,0,desks[i])
        if canvas.coords(i)[1]<0:
            canvas.move (i,0,-canvas.coords(i)[1])
        elif canvas.coords(i)[3]>height:
            canvas.move (i,0,height - canvas.coords(i)[3])

canvas.focus_set()
def W_S (event):
    global speed_left_desk
    global speed_right_desk
    if event.keysym=="w":
        speed_left_desk=-speed_desks
    elif event.keysym=="s":
        speed_left_desk=speed_desks
    elif event.keysym=="Up":
        speed_right_desk=-speed_desks
    elif event.keysym=="Down":
        speed_right_desk=speed_desks

def bound(a):
    global ball_x
    global ball_y
    if a=="desk":
        ball_y=random.randrange(-10,10)
        if abs(ball_x)<ball_finish_speed:
            ball_x=ball_x * (-speed_ball_plus)
        else:
            ball_x= -ball_x
    else:
        ball_y=-ball_y
def ball_2():
    left, up,right,down = canvas.coords(ball)
    center = (down + up)/2
    if right +ball_start_x<width-width_desk and left+ball_start_x>width_desk:
        canvas.move(ball,-ball_x,ball_y)
    elif left == width_desk or right == width-width_desk:
        if right > width/2:
            if canvas.coords(right_desk)[1] < center < canvas.coords(right_desk)[3]:
                bound("desk")
            else:
                pass
        else:
            if canvas.coords(left_desk)[1] < center < canvas.coords(left_desk)[3]:
                bound("desk")
            else:
                pass

    else:
        if right > width/2:
            canvas.move(ball,width-width_desk-right,ball_y)
        else:
            canvas.move(ball,width_desk-left,ball_y)

    if up + ball_y < 0 or down + ball_y > height:
        bound("go to else")


canvas.bind("<KeyPress>",W_S)

def stop_W_S (event):
    global speed_left_desk
    global speed_right_desk
    if event.keysym in "ws":
        speed_left_desk=0
    elif event.keysym in ("Up","Down"):
        speed_right_desk=0

canvas.bind("<KeyRelease>",stop_W_S)

# Мячик


# Бесконечный цыкл

while True:
    desk()
    ball_2()
    tk.update()