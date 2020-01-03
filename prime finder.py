print('''                               FIND ALL PRIME NUMBERS FROM 1 TO n''')
pitbull = 0
number_of_primes = 0
while pitbull == 0:
    print('''''')
    prime_range = int(input('Enter your number(n): '))
    prime_test = 0
    for num in range(1, prime_range + 1):
        for number in range(1, num):
            if num % number == 0:
                prime_test = number
        if prime_test == 1:
            number_of_primes += 1
            print(num)
    print(f'Number of prime numbers are {number_of_primes}')
    number_of_primes = 0




