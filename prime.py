n=4
if(n>1):
    for i in range (2,int(n**0.5)+1):
        if(n%i==0):
            print("it is prime")
            break
        else:
            print("not")
else:
        print("not")
