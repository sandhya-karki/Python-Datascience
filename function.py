# # # def test(x,y): #define function
# # #     print(x,y)

# # # test(10,20) #calling function

# # # def users(name,age):
# # #     get_name=f'your name is {name}'
# # #     get_age=f'age {age}'
# # #     return [get_name, get_age]

# # # data = users('ram', 20)
# # # print(data[0])
# # # print(data[1])

# # # #lambda, endless, inner fxn

# # def students(name, roll=None):
# #     print(name)
# #     if not roll == None:
# #         print(roll)

# # # students('ram',20)

# def take_value():
#     x = int(input('enter principle'))
#     y = int(input('Enter time'))
#     z = int(input('Enter rate'))
#     return [x,y,z]

# def calculate():
#     data = take_value()
#     p = data[0]
#     t = data[1]
#     r = data[2]
#     return p*t*r/100


# def display():
#     print(calculate())

# display()

# # x = 1
# # evn_num = 0
# # odd_num = 0

# # while x<=50
# #     if x % 2 == 0
    
# nested function:

# def users():
#     def names(name):
#         return f'your name is {name}'

#     return names

# data = users()
# print(data('ram'))


# x = 10

# def test():
#     global x
#     x = x + 20
#     print(x)

# test()

#lambda function

# data = lambda x,y: x + y
# print(data(10, 20))

# def users(x):
#     return lambda y: x + y

# a = users(10)
# print(a(20))

# def users()
#dunder method in documentation string
#function decorator study
#python.org
#annotation

#function decorator

# def get_doc(anyfunction):
#     def inner():
#         return f'{anyfunction.__doc__}'
    
#     return inner

# @get_doc
# def test():
#     """ this is test function"""
#     pass

# @get_doc
# def users():
#     """ hello users function """

# function decorator

# def zero_check(anyfunction):
#     def inner(x,y):
#         if y == 0:
#             return f'y is zero'
#         return anyfunction(x,y)
        
#     return inner

# def add(x,y):
#     if y == 0:
#         print('y is zero')
#     return x+y

# print(add(10,10))

# custom module, fxn wrap and multiple decorator study
# read documentation at python.org

# from functools import wraps

# def test(anyfunction):
#     @wraps(anyfunction)
#     def inner():
#         """ Hello inner function """
#         return "test"

#     return inner

# @test
# def get():
#     """ Hello get function """
#     return "success"

# print(get.__doc__)


#online compiler linux study

import calculator 
print(calculator.add(20,10))
print(calculator.sub(40,30))
