print('''                                     MULTIPLICATION TABLE GENERATOR''')
num = 3
while num != 0:
    num = int(input('''
    please enter your number: '''))
    pro = int(input('''    till what multiple do you want: '''))
    print('''''')
    for i in range(1, pro + 1):
        product = num * i
        print(f'{num} X {i} = {product}')
