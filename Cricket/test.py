import random
import matplotlib.pyplot as p
teams_list=["1","2"]
toss_choice=random.choice(teams_list)
print("Team ",toss_choice," Captain")
print("\n")
print("1.Heads")
print("2.Tails")
toss_options=["Heads","Tails"]
User_toss=int(input( "Enter Your Choice:"))
Toss_Result=random.choice(toss_options)
if toss_options[User_toss-1]==Toss_Result:
    print("You Won!")
elif User_toss!=Toss_Result:
    print("You Lost!")
################
x=[1,2,8,4,5,6,7]
y=["a","b","c","d","e","f","g"]
p.title("First")
p.xlabel("idk")
p.ylabel("idk_2")
p.plot(y,x,linewidth=2)
p.show()
x=[2,5,8,8,45,6,7]
y=["a","b","c","d","e","f","g"]
p.title("First2")
p.xlabel("idk2")
p.ylabel("idk_23")
p.plot(y,x,linewidth=2)
p.show()
input()
