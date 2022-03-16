from os import system,name
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2=[1,2]

#turn is a function
def turn(z):
    while True:
        if z.isdigit():
            z=int(z)
            if z in list2:
                if z==2:
                    can_play = False
                    for i in range(20):
                        if list1[i] != '_' and list1[i+1] != '_':
                            can_play = True
                            if can_play:
                                break
                    if can_play:
                        break
                else:
                    break
        z=input("please enter a valid num: ")
    return z


def clear():
    if name=='nt':
        _=system('cls')


def underscore(y):
    counter=0
    for j in y:
        if (j == '_'):
            counter += 1
            if (counter == 20):
                return True
    return False


def get_input(x, t):
    while True:
        if x.isdigit(): # 1
            x=int(x)
            if x in list1 :
                if t == 2: # x-1 +1
                    if list1[x-2] != '_' or list1[x] != '_':
                        break
                else:
                    break
        print(list1)
        x=input("please enter a valid num: ")
    return x


for i in range (0,20,+1):
    print(list1)
    turn1=input("if you want to play one time choose 1 and if you want to play twice choose 2: ")
    turn1=turn(turn1)
    if(turn1==1):
        player1=input("player1: ")
        player1=get_input(player1,1)
        list1[player1 - 1] = '_'
        if(underscore(list1)):
            print("player1 wins")
            break
        clear()
        print(list1)

    elif(turn1==2):
        player1=input("player1: ")
        player1 = get_input(player1,2)
        x=player1
        player1 = input("player1: ")
        player1 = get_input(player1,2)
        while(abs(x-player1)!=1):
            player1 = input("please enter an adjacent number to the first one :")
            player1 = get_input(player1,2)
        list1[player1 - 1] = '_'
        list1[x - 1] = '_'
        if (underscore(list1)):
            print("player1 wins")
            break
        clear()
        print(list1)

    turn2 = input("if you want to play one time choose 1 and if you want to play twice choose 2: ")
    turn2=turn(turn2)
    if (turn2 == 1):
        player2 = input("player2: ")
        player2=get_input(player2,1)
        list1[player2 - 1] = '_'
        if (underscore(list1)):
            print("player2 wins")
            break
        clear()
    elif(turn2==2):
        player2 = input("player2: ")
        player2 = get_input(player2,2)
        y=player2
        player2 = input("player2: ")
        player2 = get_input(player2,2)
        while (abs(y - player2) != 1):
            print("please enter an adjacent number to the first one :")
            player2 = input("player2: ")
            player2 = get_input(player2,2)
        list1[player2 - 1] = '_'
        list1[y - 1] = '_'
        if (underscore(list1)):
            print(list1)
            print("player2 wins")
