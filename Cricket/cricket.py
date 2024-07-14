import random
import os
import time
import matplotlib.pyplot as p

runs=0
ball=0
score=0
wickets=0
score_over=0
Scores=[]
ball_list=[]


def main():
	intro()
	input()




def intro():
	print("*"*55)
	print("                       Cricket")
	print("*"*55)
	team1=input("First Team-")
	team2=input("Second Team-")
	ko=open("Lineup.txt","r")
	#String
	team1_lineup_str=ko.readline()
	team2_lineup_str=ko.readline()
	ko.close()
	#list
	team1_lineup_lst=team1_lineup_str.split(",")
	team2_lineup_lst=team2_lineup_str.split(",")
	Overs=int(input("No of Overs:"))
	Balls=6*Overs
	lpo=12
	#Lineup
	print("")
	print("					Lineup")
	print("					======")
	print("  Team",team1)
	print("*"*20)
	for o in team1_lineup_lst:
		print("~ "+o)
		time.sleep(0.13)
	print("  Team",team2)
	print("*"*20)
	for o in team2_lineup_lst:
		print("~ "+o)
		time.sleep(0.13)
	input()
	os.system("cls")
	toss(team1,team2)
	Menu(Balls)


def toss(team1,team2): #################
	teams_list=[team1,team2]
	toss_choice=random.choice(teams_list)
	print("Team ",toss_choice," Captain")
	print("-"*20)
	print("1.Heads")
	print("2.Tails")
	toss_options=["Heads","Tails"]
	try:
		User_toss=int(input( "Choose Your Option:"))
	except:
		os.system("cls")
		toss(team1,team2)

	Toss_Result=random.choice(toss_options)
	if toss_options[User_toss-1]==Toss_Result:

		print("You Won!")
		print("\nTeam ",toss_choice," Captain Choose\n1.Bat \n2.Ball")
		choice_2=int(input("->"))


	elif User_toss!=Toss_Result:
		print("You Lost!")
		print("\nTeam ",toss_choice," Captain Choose\n1.Bat \n2.Ball")
		choice_2=int(input("->"))

	elif User_toss!=1 or User_toss!=2:
		toss(team1,team2)

	Bat_Ball(toss_choice,choice_2)

	print("\n")


def Bat_Ball(toss_choice,choice_2):##########
	pass
	if choice_2==1: #BAT
		input()

	elif choice_2==2: #BALL
		input()


def Menu(Balls): #Add Player
	for i in range(Balls):
		print("*"*55)
		print("                       Menu")
		print("*"*55)
		print("1.One Run")
		print("2.Two Runs")
		print("3.Three Runs")
		print("4.Four")
		print("5.Six")
		print("6.Out!")
		print("7.Wide")
		print("8.No Ball")
		Choice=int(input("Enter Your Choice:"))
		Add_Score(Choice,Balls)
		os.system("cls")
		ScoreCard(Balls)
	Stats_graph()


def Add_Score(Choice,Balls):
	#import Global Variables
	global score
	global wickets
	global ball
	global Scores
	global score_over

	if Choice==1:
		score+=1
		ball+=1

	elif Choice==2:
		score+=2
		ball+=1

	elif Choice==3:
		score+=3
		ball+=1

	elif Choice==4: #FOUR
		print()
		print("FOUR!")
		score+=4
		ball+=1

	elif Choice==5: #SIX
		print()
		print("SIX!")
		score+=6
		ball+=1

	elif Choice==6: #OUT
		print()
		print("OUT!")
		print("Next Batsman is :")
		wickets+=1
		ball+=1

	elif Choice==7: #WIDE
		print()
		print("WIDE!")
		score+=1

	elif Choice==8:
		score+=1
		print()
		print("Free Hit!")
		Menu(Balls)

	else:
		Menu(Balls)

	if ball%6==0:
		print("\nOver Up!\n")
		if ball==6:
			score_over=score
		else:
			score_over=score-score_over
		input()
		ball_list.append(int(ball/6))
		Scores.append(int(score_over))
		score_over=score

def ScoreCard(Balls):
	global score
	global ball

	if ball==Balls:
		Result()
	else:
		print("="*100)
		print("Current Score: ",score)
		print("Wickets: ",wickets)
		print("Overs: ",int(ball/6)+(ball%6)/10)
		print("\n")

def Strike(team1_lineup_lst,team2_lineup_lst):
	pass


def Result():
	global ball
	print("="*100)
	print("Total Score: ",score)
	print("Wickets: ",wickets)
	print("Overs: ",int(ball/6)+(ball%6)/10)
	Total_Score=score
	print("\n")

def Stats_graph():###########
	global Scores
	global ball
	p.title("Runs Per Over")
	p.xlabel("Overs")
	p.ylabel("Runs")
	x=ball_list
	y=Scores
	p.bar(x,y,width=0.5,color=("red","blue","green","cyan","pink","purple"))
	p.show()




main()

