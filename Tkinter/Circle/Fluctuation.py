from tkinter import *
import math

width = 600
height = 600

root = Tk()
c = Canvas(root, width = width, height = height, bg="white")
c.pack()

x_center = width // 2
y_center = height // 2
angle = 0
angle_speed = 0.03 #Расстояние между колебаниями

def calculation_pos_circle(x_center, y_center, radius, dis_radius): # Вычисление координат окужности и точки

    x = x_center - dis_radius
    y = y_center - dis_radius

    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2


def calculation_pos(x_center, y_center, radius, dis_radius, angle, angle_speed): # Вычисление координат объекта

    x = x_center - dis_radius * math.sin(-angle)
    y = y_center - dis_radius * math.cos(-angle)

    koef = 0.1 #Величина колебаний
    if (int(angle / angle_speed) % 2 == 0):
        koef *= (-1)

    x += (x - x_center) * koef
    y += (y - y_center) * koef

    return x, y

def animation(): #Перемещение точки
    
    global angle
    angle += angle_speed


    x1, y1 = calculation_pos(x_center, y_center, 10, 200, angle, angle_speed)

    c.coords(point, x1 - 10, y1 - 10, x1 + 10, y1 + 10)

    x2, y2 = calculation_pos(x_center, y_center, 10, 200, angle - angle_speed, angle_speed)

    c.create_line(x1, y1, x2, y2)

    root.after(30, animation)
    


x1, y1, x2, y2 = calculation_pos_circle(x_center, y_center, 200, 0)

ball = c.create_oval(x1, y1, x2, y2, outline="red", fill='white')

x1, y1, x2, y2 = calculation_pos_circle(x_center, y_center, 10, 200)

point = c.create_oval(x1, y1, x2, y2, fill = 'black') 

animation()

root.mainloop()


