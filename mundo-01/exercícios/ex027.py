full_name = input('Enter your full name: ').strip()
name_parts = full_name.split()

print('Nice to meet you!')
print('Your first name is {}'.format(name_parts[0]))
print('Your last name is {}'.format(name_parts[-1]))
