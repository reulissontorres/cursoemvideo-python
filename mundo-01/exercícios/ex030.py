number = int(input('\033[35mTell me any number: '))
remainder = number % 2
if remainder == 0:
    print('\033[37mThe number {} is \033[34mEVEN'.format(number))
else:
    print('\033[37mThe number {} is \033[34mODD'.format(number))
