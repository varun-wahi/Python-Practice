c=1
while c<=10:
    print("****************************************************************************")
    size=int(input("Enter size :")) #problem with size =2
    line=1
    length=(size*2)+1
    mid=(length+1)/2
    print("length:",length)
    print("mid:",mid)
    print("'*' in mid :",mid*2-4)
    print()
    #top part
    while line<=length:
        if line==1 or line==length:
            print("+"+"--"*size+"+")
            line+=1
        else:
            while line>=2 and line<=mid-1:
                if line==2:
                    print("|"," "*int(mid-line-1)+"/\\"," "*int(mid-line-2),"|")
                elif line>=3 and line<=length-1:
                    if line%2==0 :
                          print("|"+" "*int(mid-line)+"/"+"="*(int(line*2)-4)+"\\"+" "*int(mid-line)+'|')
                    else:
                        print("|"+" "*int(mid-line)+"/"+"-"*(int(line*2)-4)+"\\"+" "*int(mid-line)+'|')
                line+=1
        #middle line
            while line==mid:
                if line%2==0:
                    print("|<","="*int(mid*2-4),">|",sep='')
                else:
                    print("|<","-"*int(mid*2-4),">|",sep='')
                count=int(mid*2-4)
                
                line+=1
        #lower part
            x=1
            while line>=mid+1 and line<=length-1:
                if line==length-1:
                    print("|"+" "*int(line-mid)+"\\/"+" "*int(line-mid-1),"|")
                if line>=mid+1 and line<=length-2:
                    if line%2==0 :
                        print("|"+" "*int(line-mid)+"\\"+"="*int((2*line)-4*(line-mid+1)) +"/"+" "*int(line-mid)+'|')
                    else:
                        print("|"+" "*int(line-mid)+"\\"+"-"*int((2*line)-4*(line-mid+1))+"/"+" "*int(line-mid)+'|')
                line+=1
                x+=1
    c+=1
print("Thank You!")
input()
    
    
            
            
         
            
