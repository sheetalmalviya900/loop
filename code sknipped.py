# c = 0
# d = 1

# while c < 3:
#     c = c + 1
#     d = d * c
#     print ("Loop Ke Andar", c, d)
# else:
#     print ("Loop Ke Bahar", c, d)

# n = 6
# s = 0
# i = 1

# while i <= n:
#     s = s + i
#     i = i + 1
#     print(s)

# num=int(input("enter the number"))
# i = 2
# while (i<num):
#     if (num%i == 0):
#         print(num, 'is not a prime number')
#         break
#     i = i + 1
# else:
#     print(num, 'is a prime number')

x = 0
while(x<7):
    if (x == 3 or x==5):
        x = x + 1
        continue
    print(x)
    x = x + 1
