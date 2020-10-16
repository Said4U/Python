s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s2 = [1, 1, 1, 2, 1 ,3, 1, 4, 1]
s3 = [5, 1, 6, 1, 7, 1, 8, 1, 9]
print("Приоритет начального ввода у верхней строки")
print (s1)
print (s2)
print (s3)
while (len(s1) + len(s2) + len(s3)) != 0:
    print('Введите координаты первого элемента: ')
    n1 = int(input("Cтрока: ")) 
    m1 = int(input("Cтолбец: ")) 
    print('Введите координаты второго элемента: ')
    n2 = int(input("Cтрока: "))
    m2 = int(input("Cтолбец: "))
    if n1 == n2:
        if n1 == 1:
            if s1[m1-1] == s1[m2-1] or s1[m1-1] + s1[m2-1] == 10:
                s1.pop(m1-1)
                s2.pop(m2-1)
                print (s1)
                print (s2)
                print (s3)
            else:
                print('Ошибка ввода данных')
        if n1 == 2:
            if s2[m1-1] == s2[m2-1] or s2[m1-1] + s2[m2-1] == 10:
                s2.pop(m1-1)
                s2.pop(m2-1)
                print (s1)
                print (s2)
                print (s3) 
            else:
                print('Ошибка ввода данных')
        if n1 == 3:
            if s3[m1-1] == s3[m2-1] or s3[m1-1] + s3[m2-1] == 10:
                s3.pop(m1-1)
                s3.pop(m2-1)
                print (s1)
                print (s2)
                print (s3)
            else:
                print('Ошибка ввода данных')
    elif n1 == 1 and n2 == 2:
        if s1[m1-1] == s2[m2-1] or s1[m1-1] + s2[m2-1] == 10:
            s1.pop(m1-1)
            s2.pop(m2-1)
            print (s1)
            print (s2)
            print (s3)
        else:
            print('Ошибка ввода данных')
    elif n1 == 2 and n2 == 3:
        if s2[m1-1] == s3[m2-1] or s2[m1-1] + s3[m2-1] == 10:
            s2.pop(m1-1)
            s3.pop(m2-1)
            print (s1)
            print (s2)
            print (s3)
        else:
            print('Ошибка ввода данных')
    else:
        print('Ошибка ввода данных')