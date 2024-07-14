import time
import os
print("\n"*5)
y="|"
per=1
for i in range(25):
    print(y)
    print("         ",per,"%")
    time.sleep(0.05)
    y=y+"|"
    per=per+4
    os.system("cls")
print(y)
print("         ",per-1,"%")
input()




