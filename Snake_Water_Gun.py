'''
1 is snake 
0 is gun
-1 is water
'''
import random

computer = random.choice([-1,0,1])
yourst = input("Enter Your Choice: ")
youDict = {"s":1 ,"g":0, "w":-1}
reverse_dic = {1:"Snake" ,0:"Gun", -1:"Water"}
you = youDict[yourst]

print(f"You chose {reverse_dic[you]}\nComputer chose {reverse_dic[computer]}")

if (computer==you):
    print("Its a DRAW")

else:
    if(computer == -1 and you==1):
        print("You  Win!")
    elif(computer==-1 and you == 0):
        print("You Lose!")
    elif(computer==0 and you == 1):
        print("You Lose!")
    elif(computer==0 and you == -1):
        print("You Win!")
    elif(computer==1 and you == 0):
        print("You Win!")
    elif(computer==1 and you == -1):
        print("You Lose!")
    else:
        print("Something went Wrong")
