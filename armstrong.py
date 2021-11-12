num=int(input("enter the number"))
b=num
sum=0
while(num>0):
    a=num%10
    num=num//10
    product=a**3
    sum+=product
if(b==sum):
    print(b,"armstrong number")
else:
    print(b,"not a armstrong number")
