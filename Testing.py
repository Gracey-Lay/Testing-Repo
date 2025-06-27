# print(int(203.54))
# print(int(True))
# print(int(False))
# print(int("55"))

# # a = range(0,10)
# # # for i in a: 
# # #     print(i)
# # print(list(a))

# x = "Python\n Programming"
# print(x)

# a = "Python\'s Programming"
# print(a)

# # x = input("Enter x:")
# # y = input("Enter y:")
# # z = (int(x))
# # q = (int(y))
# # print("Concatenation:" , x+y)
# # print("Addition:" , z+q)

# s1,s2 = [int(i) for i in input("Enter 2 input:").split()]
# print("Division:",s1/s2)

# s1,s2,s3 = [float(i) for i in input("Enter 3 input").split()] 

# print("Multiply:" , (s1*s2*s3))

# # # x = '30'
# # y = '20'
# # z = x + y
# # print(z)

# # a,b,c = 100,200,300
# # print(a,b,c ,sep=",")

# # n = "Thida"
# # ids = 35
# # sub = "Python"
# # print("Name- {0} ID- {1} and Sub- {2}".format(n,ids,sub))

# # print("Name- {x} ID- {y} and Sub- {z}".format(x=n,y=ids,z=sub))
# # s = 10
# # print(s)
# # del s
# # print(s)

# x = "30" 
# print(x)
# print(type(x))
# y = int(x)
# print(y)
# print(type(y))

# w = 5
# l = 10
# p = w + w + l + l
# print(p)

# # name = input("Enter your name")
# # age = input("Enter your age")
# # gender = input("Enter gender")
# # print("Username- {0} , Age- {1} , Gender- {2}" .format(name,age,gender) )

# name = input("Enter your name")
# print(name.upper())
# print(name.capitalize())

# a = range (0, 8 , 3)
# for i in a:
#     print(i)


# # a = "Hello"

# # print(int(a))

# x = "Mg Mg" , "Ma Ma", "Su Su"
# y = "Mg Mg" , "MA MA", "Su Su"
# print(id(x))
# print(id(y))
# print(x is y)
# print(x == y)

# s = ("Path ", "is", " a", "good " ,"boy")
# a = "-".join(s)
# print(a)

# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%Y"))
# print(x.strftime("%w"))

# num = 45
# print(f"The price is {num:.4f} dollors")

# name = input("Enter Your Name")

# print(f"Hello {name}")

# import math
# a = int(input("Enter a number"))
# b = math.sqrt(a)
# print(b)

# try:
#     print(10/0)

# except ZeroDivisionError:
    
    
#     a = 10
#     b = 2
#     c = a/b
#     print(c)
# print("Hello")
# try:
#     var1 = int(input("Enter var1"))
#     var2= int(input ("Enter var2"))
#     print(var1/var2)
# except(ZeroDivisionError , ValueError)as msg:
#     print("Invalid"  , msg)
# try:
#     def sum(a,b):
#         return a + b
# except TypeError:
#     sum_value = sum(2,4,3)
#     print(sum_value)
# print("Hello")

# def evenodd(n):
#     if n % 2 ==0:
#         print(f"{n} : This is even number")

#     else:
#         print((f"{n} : This is odd number"))
# num = int(input("Enter a number"))
# evenodd(num)

# def cal(a,b):
#     sum = a + b
#     sub = a - b
#     div = a % b
#     mul = a * b

#     return sum, sub, div, mul
# n1 , n2, n3 , n4 = cal(6,7)
# print(n1)
# print(n2)
# print(n3)
# print(n4)

def n(*number):
    s = 0
    print(number)

    for i in number:
        s = s + i
    print("Addition :" ,s)
n(1, 2, 3, 4, 5)

