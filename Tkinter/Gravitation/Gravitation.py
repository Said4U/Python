from tkinter import * 
import math

width = 600
height = 600

root = Tk()
c = Canvas(root, width = width, height = height, bg="white")
c.pack()

x_center = width // 2
y_center = height // 2

angle1 = 0
angle_speed1 = 0.02
angle2 = 0
angle_speed2 = 0.02
angle3 = 0
angle_speed3 = 0.02
angle4 = 0
angle_speed4 = 0.02
angle5 = 0
angle_speed5 = 0.02
angle6 = 0
angle_speed6 = 0.02
angle7 = 0
angle_speed7 = 0.02
angle8 = 0
angle_speed8 = 0.02
angle9 = 0
angle_speed9 = 0.02

speed_lst = [angle_speed1, angle_speed2, angle_speed3, angle_speed4, angle_speed5, angle_speed5, angle_speed6, angle_speed7, angle_speed8]

radius_lst = [10, 10, 10, 15, 15, 15, 10, 15, 15, 15]

centers_lst = [[] for i in range(9)]
difference = [[0 for i in range(9)] for i in range(9)]

way_object = []

def calculation_pos(radius, dis_radius, angle, k_sin = 0, k_cos = 0, swap = None): # Вычисление координат объекта

    x = x_center - dis_radius * math.sin(angle) + math.sin(angle) * k_sin
    y = y_center - dis_radius * math.cos(angle) + math.cos(angle) * k_cos

    if swap != None:   #меняем старые ккординаты на новые
        centers_lst[swap] = [x,y]

    if len(centers_lst[8]) != 0:  #находим расстояние от каждого объекта до каждого
        for i in range(len(centers_lst)):
            difference[swap][i] = int(((centers_lst[swap][0] - centers_lst[i][0])**2 + (centers_lst[swap][1] - centers_lst[i][1])**2)**0.5)



    for i in range(len(difference)):
        for j in range(len(difference)):
            if difference[i][j] > 0 and difference[i][j] < radius_lst[i] + radius_lst[j] and {i, j} not in way_object:
                #меняем траектории 
                way_object.append({i, j})
                speed_lst[i] *= -1
                speed_lst[j] *= -1

                speed_lst[i] -= speed_lst[i]*0.001 * radius_lst[j]
                speed_lst[j] -= speed_lst[j]*0.001 * radius_lst[i]

            if difference[i][j] > radius_lst[i] + radius_lst[j] + 6 and {i,j} in way_object:
                way_object.remove({i,j})

    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2

def animation_planet(planet, radius, dis_radius, angle, k_sin = 0, k_cos = 0, swap = None):#перемещение планет
    x1, y1, x2, y2 = calculation_pos(radius, dis_radius, angle, k_sin, k_cos, swap = swap)
    c.coords(planet, x1, y1, x2, y2)


def animation(): #Перемещение объектов
    
    global angle1
    angle1 += speed_lst[0]
    global angle2
    angle2 += speed_lst[1]
    global angle3
    angle3 += speed_lst[2]
    global angle4
    angle4 += speed_lst[3]
    global angle5
    angle5 += speed_lst[4]
    global angle6
    angle6 += speed_lst[5]
    global angle7
    angle7 += speed_lst[6]
    global angle8
    angle8 += speed_lst[7]
    global angle9
    angle9 += speed_lst[8]

    animation_planet(planet_2, 10, 250, angle1, 150, 30, swap = 0)
    animation_planet(planet_3, 10, 170, angle2 + 5, 350, 200, swap = 1)
    animation_planet(planet_4, 15, 200, angle3 + 10, 390, 175, swap = 2)
    animation_planet(planet_5, 15, 230, angle4 + 15, 350, 200, swap = 3)
    animation_planet(planet_6, 15, 260, angle5 + 20, swap = 4) 
    animation_planet(planet_7, 10, 260, angle6 + 25, 600, 120, swap = 5)
    animation_planet(planet_8, 15, 200, angle7 + 30, 105, 305, swap = 6)
    animation_planet(planet_9, 15, 220, angle8 + 35, 270, 85, swap = 7)
    animation_planet(planet_10, 15, 190, angle9 + 40, 280, 640, swap = 8) 

    root.after(5, animation)

def planet_creation(radius, dis_radius, color, swap = None):#создание планет
    
    x1, y1, x2, y2 = calculation_pos(radius, dis_radius, 0, swap = swap)
    planet = c.create_oval(x1, y1, x2, y2, fill = color) 
    return planet


planet_1 = planet_creation(20, 0, "red")
planet_2 = planet_creation(10, 50, "yellow", 0)
planet_3 = planet_creation(10, 120, "white", 1)
planet_4 = planet_creation(15, 180, "orange", 2)
planet_5 = planet_creation(15, 240, "red", 3)
planet_6 = planet_creation(15, 300, "grey", 4)
planet_7 = planet_creation(10, 260, "green", 5)
planet_8 = planet_creation(15, 200, "blue", 6)
planet_9 = planet_creation(15, 220, "pink", 7)
planet_10 = planet_creation(15, 190, "black", 8)


animation()

root.mainloop()
