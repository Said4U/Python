import math
import matplotlib.pyplot as plt
import numpy as np

def g2 (x, y, koeficent, funcion = lambda x: x):
    """
    Расчет коэффициента детерминации R^2
    """
    if len(koeficent) == 2:

        a, b = koeficent
        n = len(y)
        y_mid = sum(y) / n
        upper = sum([(y - funcion(x, a, b))**2 for y, x in zip(y, x)])
        lower = sum([(y - y_mid)**2 for y in y])
        R = upper / lower

    elif len(koeficent) == 3:

        a, b, c = koeficent
        n = len(y)
        y_mid = sum(y) / n
        upper = sum([(y - funcion(x, a, b, c))**2 for y, x in zip(y, x)])
        lower = sum([(y - y_mid)**2 for y in y])
        R = upper / lower

    return 1 - R

def koeficent1 (x, y, x_funcion = lambda x: x, y_funcion = lambda y: y):
    """
    Получение коэфициетов a и b для уравнений типа a + bx
    """
    n = len(x)
    sum_x = sum([x_funcion(x) for x in x])
    sum_y = sum([y_funcion(y) for y in y])
    sum_x2 = sum([x_funcion(x)**2 for x in x])
    sum_xy = sum([x_funcion(x)*y_funcion(y) for x, y in zip(x, y)])
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    a = (sum_y - b * sum_x) / (n)
    
    return a, b


def koeficent2 (x, y):
    """
    Получение коэфициетов a и b для уравнений типа ax^2 + bx + c
    """
    n = len(x)
    sum_x = sum([x for x in x])
    sum_y = sum([y for y in y])
    sum_x2 = sum([x ** 2 for x in x])
    sum_xy = sum([x * y for x, y in zip(x, y)])
    sum_x3 = sum([x ** 3 for x in x])
    sum_x4 = sum([x ** 4 for x in x])
    sum_x2y = sum([(x ** 2) * y for x, y in zip(x, y)])
    M1 = np.array([[n, sum_x, sum_x2],[sum_x, sum_x2, sum_x3],[sum_x2, sum_x3, sum_x4]])
    V1 = np.array([sum_y, sum_xy, sum_x2y])
    a, b, c = np.linalg.solve(M1, V1)

    return c, b, a



def sr_get(x, y, x_funcion = lambda x: x, y_funcion = lambda y: y):
    """
    Вычисление величины среднего квадратичного отклонения S(x) и S(y)
    """
    n = len(x)
    sum_x = sum([x_funcion(x) for x in x][::5])
    sum_y = sum([y_funcion(y) for y in y][::5])
    otkl_x = (sum([(x - sum_x) ** 2 for x in x]) / n) ** 0.5
    otkl_y = (sum([(y - sum_y) ** 2 for y in y]) / n) ** 0.5
    return otkl_x, otkl_y


xmin = -8                                                                 #Инициализация констант
xmax = 16                                                                
x1 = 5                                                                    
x2 = 9
H = 0.25
func1 = lambda x: 2*math.sin(0.8*x - 2)
func1_integ = lambda x: -5*(math.cos(4*x/5 - 2))/2
func2 = lambda x: x**2 - 8
func2_integ = lambda x: (x ** 3)/3 - 8*x
func3 = lambda x: 2 * ((abs(2*x)) ** 0.5)
func3_integ = lambda x: (2 ** (5/2) * x * (abs(x) ** 0.5)) / 3
linear_funciontion = lambda x, a, b: a + b * x
polim_funciontion = lambda x, a, b, c: a * x ** 2 + b * x + c
funcionTION_LIST = [func1, func2, func3]
INTEGRATED_funcionTION_LIST = [func1_integ, func2_integ, func3_integ]
X_INTERVALS_LIST = [xmin, x1, x2, xmax]
x = [(x/100) for index in range(3) for x in range(X_INTERVALS_LIST[index]*100, int(X_INTERVALS_LIST[index+1]*100), int(H*100))]
y = [funcionTION_LIST[index](x/100) for index in range(3) for x in range(X_INTERVALS_LIST[index]*100, int(X_INTERVALS_LIST[index+1]*100), int(H*100))]
N = len(x)

print('Количество узловых точек:', N)


#Основная программа

fig, (ax1, ax2, ax3) = plt.subplots(
    nrows=3, ncols=1,                   #объявление обекта Figure (переменная fig)
    figsize=(12, 30)                    #и nparray из обьектов Axes (переменные ax1, ax2, ax3)
)

#Вычисляем математическое ожидание для частично непрерывной функции T-T
mat_o = 0    

for index in range(3):
    opr_integ = INTEGRATED_funcionTION_LIST[index](X_INTERVALS_LIST[index + 1]) - funcionTION_LIST[index](X_INTERVALS_LIST[index])
    mat_o += opr_integ
 
ax1.plot (x, y, 'r')                                              #работа с первым графиком(ax1)
ax1.set_title(f'M(x) = {mat_o}')                                            #изображен просто график кастомной функции
lgnd1 = ax1.legend(['Custom funciontion'], loc='upper center', shadow=True)    #как в варианте
lgnd1.get_frame().set_facecolor('#ffb19a')

               
X_INTERVALS_LIST[3] = xmax + 2
new_x = [(x/100) for index in range(3) for x in range(X_INTERVALS_LIST[index]*100, int(X_INTERVALS_LIST[index+1]*100), int(H*100))]
new_y = [funcionTION_LIST[index](x/100) for index in range(3) for x in range(X_INTERVALS_LIST[index]*100, int(X_INTERVALS_LIST[index+1]*100), int(H*100))]
               

a1, b1 = koeficent1(x, y)                                          
y_trend = [linear_funciontion(x, a1, b1) for x in new_x]                      
R_1 = g2(x, y, [a1, b1], funcion = linear_funciontion)               
otkl_x1, otkl_y1 = sr_get(x, y_trend)
ax2.plot(x, y, 'r', new_x, y_trend, 'b', linestyle='solid')      
ax2.set_title(f'R^2 = {R_1}\nS(x) = {otkl_x1}\nS(y) = {otkl_y1}')           
lgnd2 = ax2.legend(['Custom funciontion', f'y = {a1} + {b1}x'], loc='upper center', shadow=True)
lgnd2.get_frame().set_facecolor('#ffb19a')


a2, b2, c2 = koeficent2(x, y)                                          
y_trend2 = [polim_funciontion(x, a2, b2, c2) for x in new_x]                       
R_2 = g2(x, y, [a2, b2, c2], funcion = polim_funciontion)                 
otkl_x2, otkl_y2 = sr_get(x, y_trend2)
ax3.plot(x, y, 'r', new_x, y_trend2, 'b', linestyle='solid')
ax3.set_title(f'R^2 = {R_2}\nS(x) = {otkl_x2}\nS(y) = {otkl_y2}')
lgnd3 = ax3.legend(['Custom funciontion', f'y = {a2}x^2 + {b2}x + {c2}'], loc='upper center', shadow=True)
lgnd3.get_frame().set_facecolor('#ffb19a')                

