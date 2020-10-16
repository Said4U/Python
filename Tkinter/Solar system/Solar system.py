from tkinter import *
import math

width = 800
height = 800

root = Tk()
c = Canvas(root, width = width, height = height, bg="white")
c.pack()

x_center = width // 2
y_center = height // 2

angle2 = 0
angle_speed2 = 0.07
angle3 = 0
angle_speed3 = 0.09
angle4 = 0
angle_speed4 = 0.12
angle5 = 0
angle_speed5 = 0.3
angle6 = 0
angle_speed6 = 0.05

angle_meteor = 0
angle_speed_meteor = 0.1

angle_sin = 0
angle_sin_speed = 0.5


def calculation_pos(x_center, y_center, radius, dis_radius, angle, direction = 1, addit_for_comp = 0): # Вычисление координат объекта

    x = x_center - dis_radius * math.sin(angle * direction) - addit_for_comp * math.sin(angle_sin)
    y = y_center - dis_radius * math.cos(angle * direction) - addit_for_comp * math.cos(angle_sin)

    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2

def animation_planet(planet, radius, dis_radius, angle, direction = 1):#перемещение планет
    x1, y1, x2, y2 = calculation_pos(x_center, y_center, radius, dis_radius, angle, direction)
    c.coords(planet, x1, y1, x2, y2)

def animation_meteorit(obj_lst, dis_radius, i, angle, addit_for_comp = 0, direction = 1): #перемещение метеоритов и спутников
    if len(obj_lst) == 200:
        x1, y1, x2, y2 = calculation_pos(x_center, y_center, 2, dis_radius, angle + i*5)
    else:
        x1, y1, x2, y2 = calculation_pos(x_center, y_center, 2, dis_radius, angle, addit_for_comp = addit_for_comp, direction = direction)
    c.coords(obj_lst[i], x1, y1, x2, y2)


def animation(): #Перемещение объектов
    
    global angle2
    angle2 += angle_speed2
    global angle3
    angle3 += angle_speed3
    global angle4
    angle4 += angle_speed4
    global angle5
    angle5 += angle_speed5
    global angle6
    angle6 += angle_speed6

    global angle_meteor
    angle_meteor += angle_speed_meteor

    global angle_sin
    angle_sin += angle_sin_speed


    for i in range(len(obj_lst1)):
        animation_meteorit(obj_lst1, 350, i, angle_meteor)
        animation_meteorit(obj_lst2, 355, i, angle_meteor)
        animation_meteorit(obj_lst3, 360, i, angle_meteor)

    animation_planet(planet_2, 20, 60, angle2)
    animation_planet(planet_3, 15, 120, angle3)
    animation_planet(planet_4, 15, 180, angle4, direction = -1)
    animation_planet(planet_5, 25, 240, angle5)
    animation_planet(planet_6, 25, 300, angle6, direction = -1)

    animation_meteorit(companion1, 60, 0, angle2, addit_for_comp = 25)
    animation_meteorit(companion2, 120, 0, angle3, addit_for_comp =  25)
    animation_meteorit(companion2, 120, 1, angle3, addit_for_comp =  35)
    animation_meteorit(companion3, 180, 0, angle4, addit_for_comp =  25, direction = -1)
    animation_meteorit(companion3, 180, 1, angle4, addit_for_comp =  35, direction = -1)

    root.after(1, animation)

def planet_creation(radius, dis_radius, color):#создание планет
    
    x1, y1, x2, y2 = calculation_pos(x_center, y_center, radius, dis_radius, angle = 0)
    planet = c.create_oval(x1, y1, x2, y2, fill = color) 
    return planet

def object_creation(dis_radius, value = 200):#создание пояса астероидов

    obj_lst = []
    for i in range(value):
        x1, y1, x2, y2 = calculation_pos(x_center, y_center, 2, dis_radius, angle = 0)

        p = c.create_oval(x1, y1, x2, y2, fill = 'black') 

        obj_lst.append(p)

    if value == 1:
        return p
    return obj_lst


planet_1 = planet_creation(30, 0, "yellow")
planet_2 = planet_creation(20, 60, "red")
planet_3 = planet_creation(15, 120, "white")
planet_4 = planet_creation(15, 180, "black")
planet_5 = planet_creation(25, 240, "green")
planet_6 = planet_creation(25, 300, "blue")


obj_lst1 = object_creation(350)
obj_lst2 = object_creation(355)
obj_lst3 = object_creation(360)

companion1 = [object_creation(80, 1)]
companion2 = [object_creation(140, 1), object_creation(100, 1)]
companion3 = [object_creation(160, 1), object_creation(200, 1)]

animation()

root.mainloop()

