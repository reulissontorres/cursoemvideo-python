from math import hypot

opposite = float(input('Length of the opposite side: '))
adjacent = float(input('Length of the adjacent side: '))
hypotenuse = hypot(opposite, adjacent)
print('The hypotenuse will measure {:.2f}'.format(hypotenuse))
