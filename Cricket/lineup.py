a=["Vaibhav,","Varun,","Chetanya,","Anand,","Akshat\n"]
b=["Parth,","Rahul,","Aryan,","Aaditya,","SoyBoy"]
filee=open("Lineup.txt","w")
filee.writelines(a)
filee.writelines(b)
filee.close()
print("Succesful!")
input()
