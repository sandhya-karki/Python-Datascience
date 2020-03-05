# x = 10
# y = 20
# z = 50

# # if x > y and x > z:
# #     print('x is large')
# # elif y > x and y > z:
# #     print('y is large')
# # else:
# #     print('z is large')

# if x > y:
#     if x > z:
#         print('x')

#     else:
#         print('z')
# else:
#     if y > z:
#         print('y')
#     else:
#         print('z')

p = 150000
t = 2.5
r = 2.5

i = (p * t * r)/100

print(f'simple interest is {i}')

p = (100*i)/(t*r)

print(f'principle is {p}')