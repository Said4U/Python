import random
class Data:

    def __init__(self, matrix = 0):

        self.matrix = ([[' ', " a", '  b', '  c', '  d', '  e', '  f', '  g', '  h', '  '], 
        ['1','|+|', '| |', '|+|', '| |', '|+|', '| |', '|+|', '| |', '1'], ['2','| |', '|+|', '| |', '|+|', '| |', '|+|', '| |', '|+|', '2'],
        ['3','|+|', '| |', '|+|', '| |', '|+|', '| |', '|+|', '| |', '3'], ['4','| |', '|+|', '| |', '|+|', '| |', '|+|', '| |', '|+|', '4'], 
        ['5','|+|', '| |', '|+|', '| |', '|+|', '| |', '|+|', '| |', '5'], ['6','| |', '|+|', '| |', '|+|', '| |', '|+|', '| |', '|+|', '6'],
        ['7','|+|', '| |', '|+|', '| |', '|+|', '| |', '|+|', '| |', '7'], ['8','| |', '|+|', '| |', '|+|', '| |', '|+|', '| |', '|+|', '8'],
        [' ', " a", '  b', '  c', '  d', '  e', '  f', '  g', '  h', '  ']])

    def out_white(self):

        l = ''
        print()
        for i in self.matrix[::-1]:
            for j in i:
                l += j
        for i in range(10):
                print(l[0 + 26*i:26 + 26*i]) 

    def out_black(self):

        l = ''
        print()
        for i in self.matrix:
            for j in i:
                l += j
        for i in range(10):
                print(l[0 + 26*i:26 + 26*i]) 

    def positions(self):
        global alpha
        alpha = ["a", "b", 'c', "d", 'e', 'f', 'g', "h"]
        global coordinates
        coordinates = []
        global alpha_dict
        alpha_dict = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8}
        s = []
        count = 0
        print()
        print("Введите координаты, где будут распологаться ваши шашки: ")
        while count < 6:
            pos = input()
            s = [j for j in pos]
            if int(s[1]) < 9 and int(s[1]) > 0 and s[0] in alpha and len(s) == 2:
                if self.matrix[int(s[1])][alpha_dict.get(s[0])] == '|+|':
                    if choice == 1:
                        if int(s[1]) < 4:
                            self.matrix[int(s[1])].pop(alpha_dict.get(s[0]))
                            self.matrix[int(s[1])].insert(alpha_dict.get(s[0]), '|Б|')
                            count += 1
                        else:
                            print("Нельзя расставлять на вражеской половине поля")
                    else:
                        if int(s[1]) > 5:
                            self.matrix[int(s[1])].pop(alpha_dict.get(s[0]))
                            self.matrix[int(s[1])].insert(alpha_dict.get(s[0]), "|Ч|")
                            count += 1
                        else:
                            print("Нельзя расставлять на вражеской половине поля")
                else:
                    print("Вы попали на белую клетку, расстановка не засчитана ")
            else:
                print("Ошибка расстановки")

        for i in range(1, 7):
            if i % 2 == 1:
                if choice == 1:
                    self.matrix[7].pop(i)
                    self.matrix[7].insert(i, "|Ч|")
                    s = [7, i]
                else:
                    self.matrix[1].pop(i)
                    self.matrix[1].insert(i, "|Б|")
                    s = [1, i]
                coordinates.append(s)
            else:
                if choice == 1:
                    self.matrix[8].pop(i)
                    self.matrix[8].insert(i, "|Ч|")
                    s = [8, i]
                else:
                    self.matrix[2].pop(i)
                    self.matrix[2].insert(i, "|Б|")
                    s = [2, i]
                coordinates.append(s)


    def move(self):
        global note_step
        global step
        global win
        win = 0
        key_next_place = self.matrix[int(next_place[1])][alpha_dict.get(next_place[0])]
        key_place = self.matrix[int(place[1])][alpha_dict.get(place[0])]


        if choice == 1:
            if key_place == "|Б|" and key_next_place == "|+|":

                self.matrix[int(next_place[1])][alpha_dict.get(next_place[0])] = '|Б|'

                self.matrix[int(place[1])][alpha_dict.get(place[0])] = "|+|"

        else:
            if key_place == "|Ч|" and key_next_place == "|+|":

                self.matrix[int(next_place[1])][alpha_dict.get(next_place[0])] = '|Ч|'

                self.matrix[int(place[1])][alpha_dict.get(place[0])] = "|+|"

        if variant == 1:
            note_step += ' ' + step

        if choice == 1:
            for i in self.matrix[8]:
                if i == "|Б|":
                    win = 1
            for i in self.matrix[1]:
                if i == "|Ч|":
                    win = 2
        else:
            for i in self.matrix[1]:
                if i == "|Ч|":
                    win = 1
            for i in self.matrix[8]:
                if i == "|Б|":
                    win = 2



    def move_for_men(self):
        global step
        global del_coor
        del_coor = []
        global variant
        variant = 0
        global place
        global next_place
        global note_step 

        print("Введите координаты хода: ")
        step = input()
        for i in step:
            if i == "-":
                place = [j for j in step[0:2]]
                next_place = [j for j in step[3:5]]
                if choice == 1: 
                    if int(next_place[1]) - int(place[1]) == 1 and abs(alpha_dict.get(next_place[0]) - alpha_dict.get(place[0])) == 1:
                        variant = 1
                else:
                    if int(next_place[1]) - int(place[1]) == -1 and abs(alpha_dict.get(next_place[0]) - alpha_dict.get(place[0])) == 1:
                        variant = 1

        for i in step:
            if i == ":":
                place = [j for j in step[0:2]]
                next_place = [j for j in step[3:5]]

                if abs(int(next_place[1]) - int(place[1])) == 2 and abs(alpha_dict.get(next_place[0]) - alpha_dict.get(place[0])) == 2:
                    if choice == 1:
                        if (alpha_dict.get(next_place[0]) - alpha_dict.get(place[0])) > 0:
                            if self.matrix[int(place[1]) + 1][alpha_dict.get(place[0]) + 1] == "|Ч|":
                                self.matrix[int(place[1]) + 1][alpha_dict.get(place[0]) + 1] = "|+|"
                                del_coor = [int(place[1]) + 1, alpha_dict.get(place[0]) + 1]
                                variant = 1
                        else:
                            if self.matrix[int(place[1]) + 1][alpha_dict.get(place[0]) - 1] == "|Ч|":
                                self.matrix[int(place[1]) + 1][alpha_dict.get(place[0]) - 1] = "|+|"
                                del_coor = [int(place[1]) + 1, alpha_dict.get(place[0]) - 1]
                                variant = 1
                    else:
                        if (alpha_dict.get(next_place[0]) - alpha_dict.get(place[0])) < 0:
                            if self.matrix[int(place[1]) - 1][alpha_dict.get(place[0]) - 1] == "|Б|":
                                self.matrix[int(place[1]) - 1][alpha_dict.get(place[0]) - 1] = "|+|"
                                del_coor = [int(place[1]) - 1, alpha_dict.get(place[0]) - 1]
                                variant = 1
                                
                        else:
                            if self.matrix[int(place[1]) - 1][alpha_dict.get(place[0]) + 1] == "|Б|":
                                self.matrix[int(place[1]) - 1][alpha_dict.get(place[0]) + 1] = "|+|"
                                del_coor = [int(place[1]) - 1, alpha_dict.get(place[0]) + 1]
                                variant = 1

                for i in coordinates:
                    if i == del_coor:
                        coordinates.remove(del_coor)



    def move_for_PC(self):
        global note_step
        global count1
        global win 
        count1 = 0
        access = 0
        possible = 0
        coor_lst = []
        or_1 = [-1, 1]
        for elem in range(10):
            for i in range(10):
                if choice == 1:
                    if self.matrix[elem][i] == "|Ч|" and (self.matrix[elem - 1][i - 1] == "|Б|" or self.matrix[elem - 1][i + 1] == "|Б|"):
                        if self.matrix[elem - 1][i - 1] == "|Б|" and self.matrix[elem - 2][i - 2] == "|+|":
                            self.matrix[elem][i] = "|+|"
                            self.matrix[elem - 1][i - 1] = "|+|"
                            self.matrix[elem - 2][i - 2] = "|Ч|"
                            possible = 1
                            old_coor = [elem, i]
                            new_coor = [elem - 2, i - 2]

                        if self.matrix[elem - 1][i + 1] == "|Б|" and self.matrix[elem - 2][i + 2] == "|+|":
                            self.matrix[elem][i] = "|+|"
                            self.matrix[elem - 1][i + 1] = "|+|"
                            self.matrix[elem - 2][i + 2] = "|Ч|"
                            possible = 1
                            old_coor = [elem, i]
                            new_coor = [elem - 2, i + 2]

                else:
                    if self.matrix[elem][i] == "|Б|" and (self.matrix[elem + 1][i - 1] == "|Ч|" or self.matrix[elem + 1][i + 1] == "|Ч|"):
                        if self.matrix[elem + 1][i - 1] == "|Ч|" and self.matrix[elem + 2][i - 2] == "|+|":
                            self.matrix[elem][i] = "|+|"
                            self.matrix[elem + 1][i - 1] = "|+|"
                            self.matrix[elem + 2][i - 2] = "|Б|"
                            possible = 1
                            old_coor = [elem, i]
                            new_coor = [elem + 2, i - 2]
                            

                    if i <= 8 and elem <= 8 and self.matrix[elem][i] == "|Б|" and (self.matrix[elem + 1][i - 1] == "|Ч|" or self.matrix[elem + 1][i + 1] == "|Ч|"):  
                        if self.matrix[elem + 1][i + 1] == "|Ч|" and self.matrix[elem + 2][i + 2] == "|+|":
                            self.matrix[elem][i] = "|+|"
                            self.matrix[elem + 1][i + 1] = "|+|"
                            self.matrix[elem + 2][i + 2] = "|Б|"
                            possible = 1
                            old_coor = [elem, i]
                            new_coor = [elem + 2, i + 2]

   

        if possible == 1:
            note_step += " " + str(alpha[old_coor[1] - 1]) + str(old_coor[0]) + ":" + str(alpha[new_coor[1] - 1]) + str(new_coor[0])
            coordinates.remove(old_coor)
            coordinates.append(new_coor)
        if possible == 0:
            ran = random.randint(0, len(coordinates) - 1)
            ran_for_1 = random.choice(or_1)
            if choice == 1:
                while self.matrix[coordinates[ran][0] - 1][coordinates[ran][1] - ran_for_1] != "|+|":
                    ran_for_1 = random.choice(or_1)
                    ran = random.randint(0, len(coordinates) - 1)
                    count1 += 1
                    if count1 == 100:
                        access = 1
                        break
            else:
                while self.matrix[coordinates[ran][0] + 1][coordinates[ran][1] + ran_for_1] != "|+|":
                    ran_for_1 = random.choice(or_1)
                    ran = random.randint(0, len(coordinates) - 1)
                    count1 += 1
                    if count1 == 100:
                        access = 1
                        break

            if  access == 0:      
                self.matrix[coordinates[ran][0]][coordinates[ran][1]] = "|+|"
                if choice == 1:
                    self.matrix[coordinates[ran][0] - 1][coordinates[ran][1] - ran_for_1] = "|Ч|"
                    note_step += ' ' + str(alpha[coordinates[ran][1] - 1]) + str(coordinates[ran][0]) + "-" + str(alpha[coordinates[ran][1] - ran_for_1 - 1]) + str(coordinates[ran][0] - 1)
                    coordinates[ran] = [coordinates[ran][0] - 1, coordinates[ran][1] - ran_for_1]
                else:
                    self.matrix[coordinates[ran][0] + 1][coordinates[ran][1] + ran_for_1] = "|Б|"
                    note_step += ' ' + str(alpha[coordinates[ran][1] - 1]) + str(coordinates[ran][0]) + "-" + str(alpha[coordinates[ran][1] + ran_for_1 - 1]) + str(coordinates[ran][0] + 1)
                    coordinates[ran] = [coordinates[ran][0] + 1, coordinates[ran][1] + ran_for_1]

        if choice == 1:
            for i in self.matrix[8]:
                if i == "|Б|":
                    win = 1
            for i in self.matrix[1]:
                if i == "|Ч|":
                    win = 2
        else:
            for i in self.matrix[1]:
                if i == "|Ч|":
                    win = 1
            for i in self.matrix[8]:
                if i == "|Б|":
                    win = 2





data = Data()
print("Выберите цвет, за который будете играть:\n1. Белые\n2. Черные")
global choice
choice = int(input())

def info():
    if choice == 1:
        data.out_white()
    elif choice == 2:
        data.out_black()
    else:
        raise ValueError("Ну сказано же, ввести только 1 или 2")
    return ''

print(info())

data.positions()

print("\nПоле с шашками")
print(info())

variant = 0
win = 0
count1 = 0
count_step = 0
note_step_lst = []
note_step = ""

while len(coordinates) != 0 and win == 0 and count1 != 100:

    if win != 0:
        break
    if choice == 1:
        data.move_for_men()
        if variant == 1:
            count_step += 1
            note_step = str(count_step) + "."
            data.move()
            if len(coordinates) == 0:
                break
            data.move_for_PC()
        else:
            print('Ошибка хода')
        print(info())
    else:
        count_step += 1
        note_step = str(count_step) + "."
        print("Ход ПК")
        data.move_for_PC()
        print(info())
        if win != 0:
            break
        data.move_for_men()
        if variant == 1:
            data.move()
            print(info())
        else:
            while variant != 1:
                print('Ошибка хода')
                data.move_for_men()
                data.move()
                print(info())

    note_step_lst.append(note_step)
note_step_lst.append(note_step)

if win == 1:
    print("Поздавляем! Вы победили.\n")
elif win == 2:
    print("Вы проиграли")

note_step_lst[-1]+= "Х"

for i in note_step_lst:
    print(i)

