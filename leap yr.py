yr = int(input("enter the yr"))
if(yr%400==0)and(yr%100==0):
    print("leapyr")
elif(yr%4==0)and(yr%100!=0):
    print("leap yr")
else:
        print("not a leap yr")
