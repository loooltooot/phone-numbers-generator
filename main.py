from art import tprint
from decimal import *

PHONE_NUMBER_LENGTH = 11
CONSTRAINS = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999']

def main():
    tprint('PhoneNumbers', 'cybermedium')
    
    codes = input('Enter regional codes here: ').split(' ')
    print(f'[+] Selected codes: {codes}')

    file = open('numbers.txt', 'w')

    for code in codes:
        print(f'[+] Code ({code}) in process...')

        other_nums_length = PHONE_NUMBER_LENGTH - len(code)

        getcontext().prec = other_nums_length
        other_nums_step = Decimal(1 / (10**other_nums_length))

        other_nums = other_nums_step
        while other_nums < 1:
            other_nums_str = (f'%.{other_nums_length}f' % other_nums)[2:]
            is_special = False
            for CONSTRAIN in CONSTRAINS:
                if CONSTRAIN in other_nums_str:
                    is_special = True
                    break
            
            if not is_special:
                file.write(f'+{code}{other_nums_str}\n')
            
            other_nums += other_nums_step
        print(f'[+] Code ({code}) is finished!')
    
    file.close()
    print(f'[+] Finished!')

if __name__ == '__main__':
    main()
