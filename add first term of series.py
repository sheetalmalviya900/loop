num=int(input("enter the number"))
i=1
product=1
sum=0
while(i<=num):
    product*=i
    sum+=1/product
    # print(sum)
    i+=1
print(sum)

