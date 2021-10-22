# Tham khao bai cua Tien Dao


import turtle as t
import random

small = 1
normal = 3


def ran_color():
    color = ["red", "green", "blue", "grey", "black", "pink", "yellow", "purple", "orange", "brown"]
    return color[random.randint(0, len(color) - 1)]


def move_turtle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def rectangle(height, width):
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)


def roof(roof_height, roof_width):
    t.pensize(normal)
    side = roof_height * (2 ** (1 / 2))
    t.forward(roof_width)
    t.left(135)
    t.forward(side)
    t.left(45)
    t.forward(roof_width - 2 * roof_height)
    t.left(45)
    t.forward(side)


def banisters(height_door, width):
    t.pensize(small)
    n = 7
    w_1 = width / n
    w_2 = w_1 / n
    for i in range(n):
        rectangle(height_door * 3 / 7, w_1)
        if i != n - 1:
            t.forward(w_1 - w_2)
            rectangle(height_door * 3 / 7, w_2)
            t.forward(w_2)
        else:
            t.forward(w_1)


def rounddoor(height_door, width_door):
    t.pensize(normal)
    x, y = t.position()
    t.forward(width_door)
    t.left(90)
    t.forward(height_door / 2)
    t.circle(width_door / 2, extent=180)
    t.forward(height_door / 2)
    t.left(90)
    t.forward(width_door / 2)
    t.left(90)
    t.forward(height_door / 2 + width_door / 2)
    t.right(90)
    # door knob
    t.pensize(small)
    move_turtle(t.xcor() + width_door / 6, t.ycor() - height_door * 3 / 4)
    t.circle(width_door / 26)
    move_turtle(t.xcor() - 2 * width_door / 6, t.ycor())
    t.circle(width_door / 26)
    move_turtle(x, y)


def room(height, width, door, doorknob):
    t.pensize(normal)
    x, y = t.position()
    rectangle(height, width)
    # door
    width_door = width / 3
    height_door = height * 3 / 5
    t.forward(width_door)
    if door == 1:
        rectangle(height_door, width_door)
    else:
        rounddoor(height_door, width_door)
    # doorknob
    if doorknob == 1:
        move_turtle(t.xcor() + 3 * width_door / 4, t.ycor() + height_door * 4 / 7)
        t.pensize(small)
        t.circle(width_door / 13)
    move_turtle(x, y)


height_flat = float(input("Chieu cao phong: "))
floor = int(input("So tang ban muon ve: "))
flat = int(input("So phong (theo chieu ngang) ban muon ve: "))
roof_avai = input("Ban co muon co mai nha khong (0: khong - 1: co): ")

width_flat = height_flat * 7 / 5
door_height = height_flat / 3 * 2
door_width = door_height / 3

width = width_flat * flat
roof_height = door_height * 2 / 3
roof_width = width
if roof_avai != "1":
    if roof_avai != "0":
        print("Cau tra loi khong phu hop. He thong tu chon cau tra loi la 0.")
    height = height_flat * (floor + 1)
else:
    height = height_flat * (floor + 1) + roof_height

x_start = -width / 2
y_start = -height / 2

t.pencolor(ran_color())

t.hideturtle()
move_turtle(x_start, y_start)
room(height_flat, width, 0, 0)

for i in range(1, floor + 1):
    move_turtle(x_start, y_start + height_flat * i)
    for j in range(flat):
        room(height_flat, width_flat, 1, 1)
        banisters(door_height, width_flat)
if roof_avai == "1":
    t.pensize(3)
    move_turtle(x_start, y_start + height - roof_height)
    roof(roof_height, roof_width)

t.done()