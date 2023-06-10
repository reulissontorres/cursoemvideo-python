name = input('What is your full name? ').strip()

has_silva = 'silva' in name.lower()

print('Does your name have Silva? {}'.format(has_silva))
