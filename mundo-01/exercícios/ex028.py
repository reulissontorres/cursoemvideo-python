from random import randint
from time import sleep

computer_number = randint(0, 5)
print('\033[33m-=-' * 20)
print('\033[34mI will think of a number between 0 and 5. Try to guess...')
print('\033[33m-=-' * 20)

player_number = int(input('\033[mWhat number am I thinking of? '))
print('\033[35mPROCESSING...')
sleep(3)

if player_number == computer_number:
    print('\033[32mCongratulations! You managed to beat me!')
else:
    print('\033[31mI won! I was thinking of the number {} and not {}'.format(computer_number, player_number))
