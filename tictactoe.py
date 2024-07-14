#tic-tac-toe
print("PLEASE DO NOT ENTER SAME DIGIT AGAIN AND AGAIN!")
import os
from msvcrt import getch
def tictactoe():
    board=[0,1,2,3,4,5,6,7,8]
    def end():
        print("Thank you")
        input()
    def draw():
        os.system('cls')
        print("************")
        print()
        print(board[0],"|",board[1],"|",board[2])
        print("_________")
        print(board[3],"|",board[4],"|",board[5])
        print("_________")
        print(board[6],"|",board[7],"|",board[8])
        print()
        print("************")

    draw()
    def winning(player):
        if (
        board[0]==board[1]==board[2] or
        board[3]==board[4]==board[5] or
        board[6]==board[7]==board[8] or
        board[0]==board[3]==board[6] or
        board[1]==board[4]==board[7] or
        board[2]==board[5]==board[8] or
        board[0]==board[4]==board[8] or
        board[2]==board[4]==board[6]
        ):
            print(player+" Won the Game!!")
            ask()
    def ask():
        print("Do you want to play again? (y/n):")
        playagain=getch().decode("ascii")
        if playagain=="y":
            print("\n"*10)
            tictactoe()
        else:
            end()
        print("\n"*10)



    def chances(): #main #CHECK THIS PART
        n=0
        empty=True
        while n<=8:
            if n%2==0:
                player="Player 2"
                playernot="Player 1"
                winning(player)
                while empty is True:
                    choice=int(input("Player 1's Choice(0,8):"))
                    if board[choice]=="X" or board[choice]=="O":
                        print("try again!")

                    else:
                        empty=False
                        board[choice]="X"
                empty=True
            else:
                player="Player 1"
                playernot="Player 2"
                winning(player)
                while empty is True:
                    choice=int(input("Player 2's Choice(0,8):"))
                    if board[choice]=="X" or board[choice]=="O":
                        print("try again!")

                    else:
                        empty=False
                        board[choice]="O"
                empty=True

            draw()
            n+=1
        if n==9:
            winning(playernot)
            print("Tie Game!")
            ask()



    chances()
tictactoe()



