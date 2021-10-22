import turtle
import datetime

class Clock:

    def __init__(self, hour = 0.00, minute = 0.00, second = 0, radius = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.radius = radius

    def set_second(self):
        dt = datetime.datetime.now()
        return dt.second

    def set_minute(self):
        dt = datetime.datetime.now()
        return dt.minute + self.set_second() / 60

    def set_hour(self):
        dt = datetime.datetime.now()
        return dt.hour + self.minute / 60 if dt.hour < 12 else dt.hour + self.minute / 60 - 12

    def draw_clock(self, pen):
        pen.Screen().setup(800, 800)
        pen.speed(0)
        pen.Screen().tracer(0)
        pen.hideturtle()
        # chọn màu nền là cyan
        pen.bgcolor("cyan")
        # vẽ đường tròn và tô màu trắng
        pen.fillcolor("white")
        pen.begin_fill()
        pen.pensize(5)
        pen.penup()
        pen.goto(0, self.radius * (-1))
        pen.pendown()
        pen.circle(self.radius)
        pen.end_fill()
        # vẽ các vạch chia đồng hồ
        pen.penup()
        pen.home()
        for i in range(60):
            pen.right(i * 6)
            pen.penup()
            if i % 15 == 0:
                pen.pensize(5)
                pen.forward(0.75 * self.radius)
                pen.pendown()
                pen.forward(0.15 * self.radius)
                pen.penup()
                pen.home()
            elif i % 5 == 0:
                pen.pensize(3)
                pen.forward(0.8 * self.radius)
                pen.pendown()
                pen.forward(0.1 * self.radius)
                pen.penup()
                pen.home()
            else:
                pen.pensize(1)
                pen.forward(0.85 * self.radius)
                pen.pendown()
                pen.forward(0.05 * self.radius)
                pen.penup()
                pen.home()
        pen.update()

    def draw_hands(self, pen):

        pen.speed(10)
        pen.hideturtle()
        pen.pendown()

        # Vẽ kim giờ
        pen.home()
        pen.left(90)
        pen.pensize(7)
        pen.right(self.hour * 30)
        pen.forward(0.5 * self.radius)

        # Vẽ kim phút
        pen.home()
        pen.left(90)
        pen.pensize(5)
        pen.right(self.minute * 6)
        pen.forward(0.68 * self.radius)

        # Vẽ kim giây
        pen.home()
        pen.left(90)
        pen.pensize(3)
        pen.pencolor("red")
        pen.right(self.second * 6)
        pen.forward(0.68 * self.radius)

        # Vẽ tâm đồng hồ
        pen.home()
        pen.pencolor("black")
        pen.dot(20)
        pen.penup()

        # Trả con trỏ về vị trí (0,0)
        pen.home()

        turtle.Screen().update()
        pen.clear()

    def draw_motion_clock(self, pen):
        while True:
            self.second = self.set_second()
            self.minute = self.set_minute()
            self.hour = self.set_hour()
            self.draw_hands(pen)