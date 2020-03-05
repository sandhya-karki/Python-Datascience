# # x = 10
# # y = 20
# # z = 50

# # # if x > y and x > z:
# # #     print('x is large')
# # # elif y > x and y > z:
# # #     print('y is large')
# # # else:
# # #     print('z is large')

# # if x > y:
# #     if x > z:
# #         print('x')

# #     else:
# #         print('z')
# # else:
# #     if y > z:
# # #         print('y')
# # #     else:
# # #         print('z')

# # p = 150000
# # t = 2.5
# # r = 2.5

# # i = (p * t * r)/100

# # print(f'simple interest is {i}')

# # p = (100*i)/(t*r)

# # print(f'principle is {p}')

# nepali = int(input('Enter marks of Nepali:'))
# english = int(input('Enter marks of English:'))
# maths = int(input('Enter marks of Maths:'))
# science = int(input('Enter marks of Science:'))
# population = int(input('Enter marks of Population:'))

# total = nepali + english + maths + science + population
# percentage = total/5
# print(f'total is {total}')
# print(f'percentage is: {percentage}')

# if percentage < 35:
#     print('failed')
# elif percentage > 35 or percentage < 45:
#     print('pass')
# elif percentage > 45 or percentage < 60:
#     print('second div')
# elif percentage > 60 or percentage <75:
#     print('first div')
# else:
#     print('Distinction')

# if nepali<35:
#     print(f'you have failed in nepali and your marks is {nepali}')
# elif english<35:
#      print(f'you have failed in english and your marks is {english}')
# elif maths<35:
#      print(f'you have failed in maths and your marks is {maths}')
# elif science<35:
#      print(f'you have failed in science and your marks is {science}')
# elif population<35 :
#      print(f'you have failed in population and your marks is {population}')


sum = 3
call = int(input('Enter call duration:'))
if call<=5:
    print(f'callprice = {sum}')
elif call > 5 or call < 11:
    print(f'callprice = {sum *2}')
elif call > 10 or call < 21:
    print(f'callprice = {sum*3}')
elif call > 20 or call < 46:
    print(f'callprice =  {20}')
elif call > 45 or call < 101:
    print(f'callprice = {10}')
   