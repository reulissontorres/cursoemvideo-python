distance = float(input('What is the distance of your trip? '))
print('You are about to start a trip of {}Km.'.format(distance))
price = distance * 0.50 if distance <= 200 else distance * 0.45
print('And the price of your ticket will be R${:.2f}'.format(price))
