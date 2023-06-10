days = int(input('How many days rented? '))
km = float(input('How many kilometers driven? '))
total_payment = (days * 60) + (km * 0.15)
print('The total amount to be paid is R${:.2f}'.format(total_payment))
