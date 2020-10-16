#3адание 1
import random
import copy
from decimal import Decimal
global suma_det
suma_det = []
s = []
s2 = []
count1 = 0
count2 = 0
count5 = 0
matrix1 = [[random.randint(0,9) for i in range(3)] for j in range(3)]
matrix2 = [[random.randint(0,9) for i in range(3)] for j in range(3)]

print("Сгенерированная матрица 1:")
for elem in matrix1:
    print(elem)
print()
print("Сгенерированная матрица 2:")
for elem in matrix2:
    print(elem)

for elem in matrix1:
    count1 += 1
    for i in range(len(elem)):
        count2 = 0
        for elem2 in matrix2:
            count2 += 1
            for j in range(len(elem2)):
                if i == j and count1 == count2:
                    s.append(elem[i] + elem2[j])
                    s2.append(elem[i] - elem2[j])

matrix_sum = [s[i:i + 3] for i in range(0, 9, 3)]
matrix_raz = [s2[i:i + 3] for i in range(0, 9, 3)]

print()
print("Cуммма двух матриц: ")
for elem in matrix_sum:
    print(elem)

print()
print("Разность двух матриц: ")
for elem in matrix_raz:
    print(elem)

def determin(matrix, digit):
    det_sum = matrix[0][0]*matrix[1][1]*matrix[2][2] + matrix[0][1]*matrix[1][2]*matrix[2][0] + matrix[1][0]*matrix[2][1]*matrix[0][2]
    det_raz = matrix[0][2]*matrix[1][1]*matrix[2][0] + matrix[0][1]*matrix[1][0]*matrix[2][2] + matrix[0][0]*matrix[1][2]*matrix[2][1]
    det_com = det_sum - det_raz
    if digit == 1:
        suma_det.append(det_com)
        return 'Определитель матрицы 3*3 для матрицы 4*4 = ' +  str(det_com)
    if digit == 2:
        suma_det.append(det_com)
        return 'Определитель матрицы 3*3 по неизвестной = ' +  str(det_com)
        det_com = det_sum - det_raz
    if digit == 3:
        suma_det.append(det_com)
        return 'Минор матрицы 4*4 = ' +  str(det_com)
    else:
        return det_com

print()
print("Определитель 1 матрицы = ", determin(matrix1, 0))

print("Определитель 2 матрицы = ", determin(matrix2, 0))

matrix_trans = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]
print()
print("Транспонированная 1 матрица:  ")
for elem in matrix_trans:
    print(elem)

matrix_trans = [[matrix2[j][i] for j in range(len(matrix2))] for i in range(len(matrix2[0]))]
print()
print("Транспонированная 2 матрица:  ")
for elem in matrix_trans:
    print(elem)

def rever(matrix, determ):
    count3 = -1
    count4 = -1
    s_minor = []
    s_det = []
    for elem in matrix: #столбцы
        count3 += 1
        for i in range(len(elem)): #строки
            matrix_det = copy.deepcopy(matrix)

            matrix_det.pop(count3)

            matrix_det[0].pop(i)
            matrix_det[1].pop(i)

            s_minor.append(matrix_det[0][0]*matrix_det[1][1] - matrix_det[0][1]*matrix_det[1][0])

    s_minor = [s_minor[i:i + 3] for i in range(0, 9, 3)] #матрица миноров

    s_minor[0][1] *= -1
    s_minor[1][0] *= -1
    s_minor[1][2] *= -1
    s_minor[2][1] *= -1 # матрица алгебраических дополнений


    s_minor = [[s_minor[j][i] for j in range(len(s_minor))] for i in range(len(s_minor[0]))]


    for elem in s_minor:
        count4 += 1
        for i in range(len(elem)):
            s_det.append(round(s_minor[count4][i] / determ, 2))


    if len(matrix) == 4:
        s_det = [s_det[i:i + 4] for i in range(0, 12, 4)]
        print(s_det)
        return s_det
    else:
        s_det = [s_det[i:i + 3] for i in range(0, 9, 3)]
        for elem in s_det:
            print(elem)
        return ''

print()
print("Обратная 1 матрица:")
print(rever(matrix1, determin(matrix1, 0)))
print("Обратная 2 матрица:")
print(rever(matrix2, determin(matrix2, 0)))


A = [[random.randint(1,10) for i in range(2)] for j in range(2)]
B = [[random.randint(1,10) for i in range(3)] for j in range(2)]
C = [[random.randint(1,10) for i in range(2)] for j in range(3)]
D = [[random.randint(1,10) for i in range(1)] for j in range(2)]

print()
print("Матрица А: ")
for elem in A:
    print(elem)
print()

print("Матрица B: ")
for elem in B:
    print(elem)
print()

print("Матрица C: ")
for elem in C:
    print(elem)
print()

print("Матрица D: ")
for elem in D:
    print(elem)
print()

def matrix_multiplicatio(matrix_one, matrix_two):
    matrix_last = []
    value = 0
    value3 = 0
    value2 = []
    for n in range(len(matrix_two[1])):
        for i in range(len(matrix_one)): 
            for j in range(len(matrix_one[i])):
                value += matrix_one[i][j] * matrix_two[j][n] 
            value2.append(value)
            value = 0
        value3 = value2.copy()
        value2.clear()
        matrix_last.append(value3)

    matrix_last = [[matrix_last[j][i] for j in range(len(matrix_last))] for i in range(len(matrix_last[0]))]
    print()
    if len(matrix_one) == 4:
        print("Решение системы методом обратной матрицы: ")
        for elem in matrix_last:
            elem[0] = round(elem[0], 2)
            print(elem)
    else:
        for elem in matrix_last:
            print(elem)
    return ''

print("A*B:")
print(matrix_multiplicatio(A, B))
print("C*D:")
print(matrix_multiplicatio(C, D))
print("B*C:")
print(matrix_multiplicatio(B, C))
print("C*B:")
print(matrix_multiplicatio(C, B))
 

A_matr = [[3, -3, 1, -2],
          [0, -9, -5, 8], 
          [-1, -3, -3, -6], 
          [0, -3, -9, -4]]
 
B_matr = [[-2], [-14], [-6], [-12]]


#3адание 2 
print("Метод Крамера:")

print()
for i in range(len(A_matr)): #столбцы
    matrix_det = copy.deepcopy(A_matr)

    matrix_det.pop(0)

    matrix_det[0].pop(i)
    matrix_det[1].pop(i)
    matrix_det[2].pop(i)
    print(determin(matrix_det, 1))

suma_det[0] *= 3
suma_det[1] *= 3
suma_det[3] *= 2
suma_det_com = sum(suma_det) # Определитель матрицы 4*4
suma_det.clear()


for i in range(len(A_matr[1])):   
    count5 += 1
    A_matr_copy = copy.deepcopy(A_matr)
    A_matr_copy[0][i] = B_matr[0][0]
    A_matr_copy[1][i] = B_matr[1][0]
    A_matr_copy[2][i] = B_matr[2][0]
    A_matr_copy[3][i] = B_matr[3][0]
    for i in range(len(A_matr)): #столбцы
        matrix_det = copy.deepcopy(A_matr_copy)

        matrix_det.pop(0)

        matrix_det[0].pop(i)
        matrix_det[1].pop(i)
        matrix_det[2].pop(i)
        print(determin(matrix_det, 2))

    if count5 == 1:
        suma_det[0] *= -2
        suma_det[1] *= 3
        suma_det[3] *= 2
        suma_det_1 = sum(suma_det)
        suma_det.clear()

    if count5 == 2:
        suma_det[0] *= 3
        suma_det[1] *= 2
        suma_det[3] *= 2
        suma_det_2 = sum(suma_det)
        suma_det.clear()

    if count5 == 3:
        suma_det[0] *= 3
        suma_det[1] *= 3
        suma_det[2] *= -2
        suma_det[3] *= 2
        suma_det_3 = sum(suma_det)
        suma_det.clear()

    if count5 == 4:
        suma_det[0] *= 3
        suma_det[1] *= 3
        suma_det[3] *= 2
        suma_det_4 = sum(suma_det)
        suma_det.clear()


print()
print("x1 = " , suma_det_1 / suma_det_com)
print("x2 = " ,suma_det_2 / suma_det_com)
print("x3 = " ,suma_det_3 / suma_det_com)
print("x4 = " ,suma_det_4 / suma_det_com)

print()
print("Метод обратной матрицы:")
print()

count3 = -1
count4 = -1
s_minor = []
s_det = []
for elem in A_matr: #строки
    count3 += 1
    for i in range(len(elem)): #столбцы
        matrix_det = copy.deepcopy(A_matr)

        matrix_det.pop(count3)

        matrix_det[0].pop(i)
        matrix_det[1].pop(i)
        matrix_det[2].pop(i)

        print(determin(matrix_det, 3))


suma_det = [suma_det[i:i + 4] for i in range(0, 16, 4)] #матрица миноров

suma_det[0][1] *= -1
suma_det[0][3] *= -1
suma_det[1][0] *= -1
suma_det[1][2] *= -1
suma_det[2][1] *= -1
suma_det[2][3] *= -1
suma_det[3][0] *= -1
suma_det[3][2] *= -1 # матрица алгебраических дополнений


suma_det = [[suma_det[j][i] for j in range(len(suma_det))] for i in range(len(suma_det[0]))]


for elem in suma_det:
    count4 += 1
    for i in range(len(elem)):
        s_det.append(suma_det[count4][i] / suma_det_com)


s_det = [s_det[i:i + 4] for i in range(0, 16, 4)]

print()

B_matr = [-2, -14, -6, -12]
value = 0
vector_last = []

for i in range(len(s_det)): 
    for j in range(len(s_det[1])):
        value += s_det[i][j] * B_matr[j]
    vector_last.append(int(value))
    value = 0 

print("X = " , vector_last)


