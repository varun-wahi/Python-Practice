import mysql.connector
from datetime import date,datetime
import os 

db = mysql.connector.connect(host = "localhost", user = "root", passwd = "root",database = "teacher_data")
cursor = db.cursor()
today = date.today()


def menu():
	
	today=date.today()
	now=datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("Date: ",today.strftime("%b-%d-%Y"),"  Time :", current_time)
	print("*"*50)

	print("               MENU                 ")
	print("""
	1. Create Database
	2. Create Table
	3. Add Teacher
	4. Remove Teacher
	5. Show Data
	6. Exit
		
		""")
	choice = int(input("Enter Choice: "))

	if choice == 1:
		create_db()

	elif choice == 2:

		cursor.execute("""CREATE TABLE IF NOT EXISTS teachers (id INT AUTO_INCREMENT PRIMARY KEY, 
			name VARCHAR(255), 
			gender VARCHAR(1),
			subject VARCHAR(255),
			phone BIGINT,
			joining_date VARCHAR(255),
			salary INT)""")
		print("TABLE CREATED!\n\n")

	elif choice == 3:
		add_teacher()

	elif choice == 4:
		remove_teacher()

	elif choice == 5:
		show_data()

	elif choice == 6:
		exit()



def create_db():
	db = mysql.connector.connect(host = "localhost", user = "root", passwd = "root")
	cursor = db.cursor()

	#creating a database, if it doesn't already exist.
	cursor.execute("CREATE DATABASE IF NOT EXISTS Teacher_Data")
	print("DATABASE CREATED! \n")



def add_teacher():

	name = input("Enter Name: ")
	gender = input("Gender (M/F): ")
	sub = input("Enter Subject: ")
	phone = int(input("Enter Mobile No: "))
	joining_date = today.strftime("%b-%d-%Y")
	salary = int(input("Enter Salary: "))
	print("\n")

	command = "insert into teachers(name, gender, subject, phone, joining_date, salary) values(%s, %s, %s, %s, %s, %s)"
	values = (name,gender,sub,phone,joining_date,salary)
	cursor.execute(command,values)
	db.commit()
	print(name+"'s data was inserted.")

def remove_teacher():
	name = input("Teacher's Name: ")
	name = ("'"+name+"'")

	sub = input("Teacher's Subject: ")
	sub = ("'"+sub+"'")

	cursor.execute("DELETE FROM teachers WHERE name =%s AND subject = %s"%(name,sub))
	db.commit()
	input("\nPress Enter to Confirm.\n")
	print(name,"was removed from the table!")


def show_data(): ##############################
	cursor.execute("SELECT * from teachers")
	data = cursor.fetchall()

	head=("     S.NO        |       Name       |      Gender      |     Subject     |     Mobile No     |    joining_date   |    Salary       |")
	print("-"*len(head))
	print(head)
	print("-"*len(head))

	for i in data:
		print("\n")
		for j in i:
			j=str(j)
			print(j," "*(16-len(j))+"|",end=" ")

	print("\n")


while True:
	print("*"*50)	
	menu()
	print("\n\n")