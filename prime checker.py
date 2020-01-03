print('''                                 PRIME NUMBER TEST''')
dingdong = 0
FACTORS = []
num_of_factors = 1
while dingdong == 0:
    num = int(input('''
Please enter your number: '''))
    print(''' ''')
    prime_test = 1
    if num == 1:
        print('unique')
    elif num == 2:
        print('prime')
    else:
        for number in range(1, num):
            if num % number == 0:
                prime_test = number
                factor = num / prime_test
                FACTORS.append(factor)
                num_of_factors += 1
        FACTORS.append(1.0)
        FACTORS.reverse()
        if num < 0:
            print('sorry, only natural numbers accepted!')
        elif num == 0:
            print('zero is nothing')
        elif prime_test == 1:
            print('prime')
        elif prime_test != 1:
            print('composite')
            print(f'It can be written as {prime_test} x {factor} = {num}')
            print(f'The set of all factors of {num} is {FACTORS}')
            print(f'Number of factors are {num_of_factors}')
    FACTORS = []
    num_of_factors = 1

