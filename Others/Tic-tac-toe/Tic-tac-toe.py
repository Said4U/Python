args1 = [i for i in input()]
args2 = [i for i in input()]
args3 = [i for i in input()]

answer = None

if set(args1) == {"X"} or set(args2) == {"X"} or set(args3) == {"X"}:
    answer = True
else:
    for i in range(3):
        if set([args1[i], args2[i], args3[i]]) == {'X'}:
            answer = True

    if set([args1[0], args2[1], args3[2]]) == {'X'} or set([args1[2], args2[1], args3[0]]) == {'X'}:
        answer = True

    if answer == None:
        if set(args1) == {"O"} or set(args2) == {"O"} or set(args3) == {"O"}:
            answer = False
        else:
            for i in range(3):
                if set([args1[i], args2[i], args3[i]]) == {'O'}:
                    answer = False

            if set([args1[0], args2[1], args3[2]]) == {'O'} or set([args1[2], args2[1], args3[0]]) == {'O'}:
                answer = False

if answer == True:
    print('Win')
elif answer == False:
    print('Lose')
elif answer == None:
    print('Draw')

