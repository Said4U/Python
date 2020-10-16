from tkinter import *

width = 800
height = 800

root = Tk()
c = Canvas(root, width = width, height = height, bg="white")

scal1 = Scale(root, orient = HORIZONTAL, length = 300, from_= 10, to = 100, tickinterval = 10, resolution = 5) # Анимация
scal1.place(x = 0, y = 0)

scal2 = Scale(root, orient = HORIZONTAL, length = 300, from_= 10, to = 20, tickinterval = 1, resolution = 1) # а
scal2.place(x = 0, y = 100)

scal3 = Scale(root, orient = HORIZONTAL, length = 300, from_= 28, to = 40, tickinterval = 2, resolution = 2) # r
scal3.place(x = 0, y = 200)

scal4 = Scale(root, orient = HORIZONTAL, length = 300, from_= 8/3, to = 8, tickinterval = 1, resolution = 1/30) # b
scal4.place(x = 0, y = 300)

c.pack()

x_center = width // 2
y_center = height // 2

a = 10 # наши параметры
r = 28
b = 8/3
x, y, z = 0, 0.1, 0


def calculation_pos(a, r, b, radius = 0.1): # Вычисление координат объекта
    global x
    global y
    global z
    x2 = x + (a * (y - x)) / 100
    y2 = y + (x * (r - z) - y) / 100
    z2 = z + (x * y - b * z) / 100

    x = x2
    y = y2
    z = z2

    x1 = x - radius
    y1 = z - radius
    x2 = x + radius
    y2 = z + radius

    return x1*5, y1*5, x2*5, y2*5

def animation(): #Перемещение точки
     

    x1, y1, x2, y2 = calculation_pos(getA(), getR(), getB())
    d = c.create_oval(x1 +  x_center, y1 + y_center  - 200, x2 +  x_center, y2 + y_center - 200, fill = 'black')

    root.after(1 + getSpeed(), animation)


def getSpeed():
    return scal1.get()

def getA():
    return scal2.get()

def getR():
    return scal3.get()

def getB():
    return scal4.get()
    
animation()

root.mainloop()
