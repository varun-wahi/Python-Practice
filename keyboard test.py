import random

choice_lst = ["Stone","Paper","Scissors"]
print("""\n	Options\n
	1.Rock
	2.Paper
	3.Scissors\n\n""")
choice = int(input("Enter Your Choice:"))

if choice >=4:
	pass

else:
	computer_choice = random.choice(choice_lst)
	if choice==1:
		print("You Chose Rock")
		
	elif choice ==2:
		print("You Chose Paper")
	
	else:
		print("You Chose Scissors")
	
	print("Computer Chose",computer_choice,"\n\n")

	if choice == 1 and computer_choice == "Paper":



