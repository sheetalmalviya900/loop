i=int(input("enter the number"))
tem=i
rev=1
while(i>0):
    tem=i*0+tem
    i//=10
print(tem)
if(tem==i):
    print("palindrom")
else:
    print("not a palindrom")
