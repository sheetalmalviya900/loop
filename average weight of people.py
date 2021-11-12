weight=int(input("enter the number of people"))
i=0
sum=0
while(i<weight):
    num=int(input ("enter the number"))
    sum=sum+num
    i+=1
    average=sum/weight
print("average of the people weight:",average)
if(average %5==0):
    print("divisible by 5")
else:
    print("not divisible by 5")

