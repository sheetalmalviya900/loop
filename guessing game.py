# num=int(input("enter the guessing number"))
i=1
while(i<=5):
    num=int(input("enter the guessing number"))
    if(num==5):
        print("guessing is true")
        break;
    else:
        print("wrong guess")
    i+=1