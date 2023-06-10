speed = float(input('What is the current speed of the car? '))
if speed > 80:
    print('\033[31mFINE! You exceeded the speed limit of 80Km/h')
    fine = (speed - 80) * 7
    print('You must pay a fine of \033[33mR${:.2f}!'.format(fine))
print('\033[32mHave a nice day! Drive safely!')
