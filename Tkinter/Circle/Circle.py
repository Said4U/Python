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
angle_speed = 0.005


def calculation_pos(x_center, y_center, radius, dis_radius, angle, angle_speed): # Вычисление координат объекта

    x = x_center - dis_radius * math.sin(-angle)
    y = y_center - dis_radius * math.cos(-angle)

    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2

def animation(): #Перемещение точки
    
    global angle
    angle += angle_speed
    x1, y1, x2, y2 = calculation_pos(x_center, y_center, 10, 200, angle, angle_speed)
    c.coords(point, x1, y1, x2, y2)

    root.after(1, animation)
    


x1, y1, x2, y2 = calculation_pos(x_center, y_center, 200, 0, 0, 0)

ball = c.create_oval(x1, y1, x2, y2, outline="red", fill='white')

x1, y1, x2, y2 = calculation_pos(x_center, y_center, 10, 200, angle, angle_speed)

point = c.create_oval(x1, y1, x2, y2, fill = 'black') 


animation()

root.mainloop()
