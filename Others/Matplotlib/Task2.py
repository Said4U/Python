import math
import matplotlib.pyplot as plt

print("Кол-во разделение = 100\nМетод трапеций\n")
def trapecia_method(func, a, b, nseg):

    dx = (b - a) / nseg
    suma = 0.5 * (func(a) + func(b))
    for i in range(1, nseg):
        suma += func(a + i * dx)

    return suma * dx

f1 = lambda x: math.cos(9*math.acos(x))

print("1 функция")
print(trapecia_method(f1, 0, 0.5, 100))

f2 = lambda x: (math.sin(x) * math.e **(-(1 + x)**2)) / ((1 - x**2)**0.5)

print("\n2 функция")
print(trapecia_method(f2, 0, 0.5, 100))

def simpson(f, a, b, n):
    h = (b-a)/n
    k = 0.0
    x = a + h

    for i in range(1,int(n/2 + 1)):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1,int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a) + f(b) + k)

print("\nМетод Симпсона\n")
print("1 функция")
print(simpson(f1, 0, 0.5, 10))

print("\n2 функция")
print(simpson(f2, 0, 0.5, 10))

def linear(f, x0, x):

    answer = f(x0) + ((f(0.0002) - f(0.0001))/0.0001)*(x-x0)

    return answer 

print("\nЛинеаризация функции в точке 0.25\n")
print(linear(f1, 0.25, 0.5))


s = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

s_mean = [math.cos(9*math.acos(x)) for x in s]

f3 = lambda x: math.atan(x)/x

func = lambda x: f3(0.25) + ((f3(x) - f3(x - 0.0001))/0.0001)*(x - 0.25)

s_mean2 = [func(x) for x in s]

plt.plot(s, s_mean, s, s_mean2)

plt.title('Графики функций 2 задания', fontsize = 17)
plt.show()

s_final = [0, 0.5, 0.75, 1, 1.25, 1.50, 1.75, 2]
func3 = lambda x: ((0.25 * 5 / 2) * 25 + (1 - 0.25 / 2 ))**(x)

s_mean4 = [func3(s_final[x]) for x in range(len(s_final))]

s_125 = [125, 125, 125, 125, 125, 125, 125, 125]
plt.plot(s_final, s_mean4, s_final, s_125)
plt.title('График решения дифф. ур.', fontsize = 17)
plt.show()





