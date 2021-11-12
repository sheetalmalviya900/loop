i=1
while(i<=5):
    num=int(input("enter the guessing number"))
    if(num==5):
        print("Wow you guessed the correct number")
        break;
    elif(num<5):
        print("Number entered by you entered is small, try one more time ")
    else:
        print("Number entered by you entered is greater, try one more time")
    i+=1