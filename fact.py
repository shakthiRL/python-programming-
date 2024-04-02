num=7
fact=1
if num<0 :
 print("not fact")
elif num==0 :
 print("0")
else :
    for i in range(1,num+1):
        fact=fact*i
    print("it is fact",num,"is",fact)
