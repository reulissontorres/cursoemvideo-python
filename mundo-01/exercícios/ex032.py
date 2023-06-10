from datetime import date

year = int(input('Which year do you want to analyze? Enter 0 to analyze the current year: '))

if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('The year {} is a LEAP year'.format(year))
else:
    print('The year {} is NOT a LEAP year'.format(year))
