# def add(z):
#     c=20
#     return z+c
# sum=add(20)
# print(sum)

# def abc(x,y):
#     c=x/y
#     d=x*y
#     return c,d
# div,mul=abc(10,20)
# print(div)
# print(mul)


# def mul():#function with no argument and no return value
#     x=20
#     y=40
#     c=x+y
#     print(c)
# mul()

# def abc(x,y):
#     z=x+y
#     return z
# keh=abc(5,2)
# print(keh)

# def gfx(a,b):#argument with no return value
#     l=a+b
#     print(l)
# gfx(1,2)




# def gfx():
#     a=int(input("Enter a number"))
#     b=int(input("Enter a number"))
#     c=int(input("Enter a number"))
#     if a>b and a>c:
#         return(a,"is grater")
#     elif b>c and b>a:
#         return(b,"is grater")
#     else:
#         return(c,"is grater")
# print(gfx())



# def disp():
#     def show():
#         print("Show Function")
#     show()
# disp()
# print("Disp Function")


# def disp():
#     def show():
#         return "show function"
#     result=



# def add():
#     print("add")
# print("python")
# add()
# print("Hello")

# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         print(x)
#         print("inside the function y ",y)
#     inner()
#     print("z:",z)
# outer()

# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         global y
#         z=z+1
#         print(x)
#         print("inside the function y",y)
#     inner()
#     print("Z:",z)
# outer()


# y=10 
# def inner():
#     x=4
#     global y
#     print(x)
#     print("inside the function y",y)
# print("y:",y)
# inner()

# y=10
# def inner():
#     x=4
#     global y
#     y=y+1
#     print(x)
#     print("inside the function y",y)
# print("y:",y)
# inner()
    


# y=50
# def outer():
#     y=5
#     def inner():
#         y=9
#         print(y)
#     inner()
# outer()


# def outer():
#     x="local"
#     def inner():
#         nonlocal x
#         x="nonlocal"
#         print("inner:",x)
#     inner()
#     print("outer:",x)
# outer( )

# result=lambda n1,n2,n3:( n1 + n2 + n3, n1-n2-n3,n1*n2*n3,n1/n2/n3)
# print("math of three value:", result(10,20,25))

# li=[2,3,4,5,6,7]
# square_list=list(map(lambda x: x**2,li))
# print(square_list)

# a=[1,2,3]
# b=[3,4,5]
# abc=list(map(lambda x,y:x+y,a,b))
# print(abc)

# data=[1,2,3,4,5,5,6,6,7,9,10]
# var=list(filter(lambda x:x%3==0,data))
# print(var)

for i in range(4):
    print(i)