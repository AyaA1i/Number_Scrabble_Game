list = [1,2,3,4,5,6,7,8,9]
player1=[]
player2=[]
counter1 = counter2 = 0

#function checks if the output is a number and in our list and if it is not it will ask for another input.
def get_input(x):
    while True:
        if x.isdigit():
            x=int(x)
            if x in list :
                break
        print(list)
        x=input("please enter a valid num: ")
    return x


print("choose a number ")
#for loop takes 3 inputs from each player and checks if sum of any of them equals 15 or not.
for i in range (0,3,+1):
    print(list)
    print("player1 : ", end='')
    number1 = input()
    number1=get_input(number1)
    player1.append(number1)
    list.remove(number1)
    if (i == 2):
        if (player1[0] + player1[1] + player1[2] == 15):
            counter1 = counter1 + 1
            print("player1 wins")
            break
    print(list)
    print("player2 : ",end='')
    number2 = input()
    number2=get_input(number2)
    player2.append(number2)
    list.remove(number2)
    if (i == 2):
        if (player2[0] + player2[1] + player2[2] == 15):
            counter2 = counter2 + 1
            print("player2 wins")
#condition checks if the sum of the 3 iutputs of each player are not equal to 15.
if (counter1 == 0 and counter2 == 0):
    print(list)
    print("player1 : ",end='')
    number1 = input()
    number1=get_input(number1)
    player1.append(number1)
    list.remove(number1)
    #three loops loop on the four elements on player1 list.
    for i in range(0,2):
        for j in range(i+1,3):
            for k in range(j+1,4):
                #condition checks if the sum of any 3 numbers in player1 list is equal to 15.
                if player1[i]+player1[j]+player1[k]==15:
                    counter1=counter1+1
                    print("player1 wins")
                    break
    #condition checks if player1 didn't enter 3 numbers the sum of them is 15.
    if(counter1==0):
        print(list)
        print("player2 : ", end='')
        number2 = input()
        number2=get_input(number2)
        player2.append(number2)
        list.remove(number2)
        # three loops loop on the four elements on player2 list.
        for i in range(0, 2):
            for j in range(i + 1, 3):
                for k in range(j + 1, 4):
                    # condition checks if the sum of any 3 numbers in player2 list is equal to 15.
                    if player2[i] + player2[j] + player2[k] == 15:
                        counter2=counter2+1
                        print("player2 wins")
                        break
#condition checks if the two players didn't enter 3 numbers the sum of them is 15.
if (counter1 == 0 and counter2 == 0):
    print("draw")

