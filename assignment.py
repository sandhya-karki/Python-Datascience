print('======Dell======')
print('======Mac=======')
print('======Toshiba===')
product = input('choose a product')

if product == 'dell':
    price = 30000
elif product == 'mac':
    price = 50000
elif product =='Toshiba':
    price = 20000
else:
    'ERROR WHILE CHOOSING PRODUCT'

packing = input('choose packing type')
if packing == 'normal':
    packcost=1000
elif packing == 'laptopbags':
    packcost=5000
elif packing == 'giftwrap':
    packcost=10000
else:
    'ERROR WITH PACKING'

    total = price+packcost
    print(f'total is :{total}')
