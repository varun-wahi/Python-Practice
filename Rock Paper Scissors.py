import random
import os
lst=["Rock","Paper","Scissors"]
def main():
    os.system("cls")
    print("*******************")
    menu()
    print("*******************")
def menu():
    print("     Menu")
    print("*******************\n")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors\n")
    player()
def player():
    choice=int(input("Choice:"))
    if choice==1:
        plr="Rock"
    elif choice==2:
        plr="Paper"
    elif choice==3:
        plr="Scissors"
    else:
        print("**********\n")
        main()
    plr2=random.choice(lst)
    print("Player Chose",plr)
    print("Computer Chose",plr2)
    winner(plr,plr2)
def winner(plr,plr2):
    print("\n")
    if plr==plr2:
        print("Tie!")
    elif (plr=="Paper" and plr2=="Rock"):
        print("Computer Wins!")
    elif (plr=="Scissors" and plr2=="Paper"):
        print("Player Wins!")
    elif plr=="Rock" and plr2=="Scissors":
        print("Player Wins!")
    else:
        print("Computer Wins :(")
    input("\n Press Enter to Play Again\n")
    main()


main()

