name = input('Enter your full name: ').strip()

print('Analyzing your name...')
print('Your name in uppercase is {}'.format(name.upper()))
print('Your name in lowercase is {}'.format(name.lower()))

name_length = len(name.replace(' ', ''))
print('Your name has a total of {} letters'.format(name_length))

name_parts = name.split()
first_name = name_parts[0]
print('Your first name is {} and it has {} letters'.format(first_name, len(first_name)))
