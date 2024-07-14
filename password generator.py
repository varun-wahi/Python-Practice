import random
print("E-mail Generator\n\n")
char='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
names=(("adam"),("diva"),("kita"),("ora"),("swagger"))
str=''
emaill=""
kal=""
def password(str):
    for i in range(9):
        n=(random.choice(char))
        str+=n
    print("Password:"+str)
def email(kal):
    k=random.randint(0,4)
    n=names[k]
    for j in range(3):
        h=random.choice(char)
        kal+=h
    print("E-mail:"+n+kal+"@yahoo.com")
email(kal)
password(str)
input()



