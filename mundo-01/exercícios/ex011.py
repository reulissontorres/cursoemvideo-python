width = float(input('Width of the wall: '))
height = float(input('Height of the wall: '))
area = width * height
print('Your wall has dimensions {}x{} and its area is {}m².'.format(width, height, area))
paint = area / 2
print('To paint this wall, you will need {} liters of paint.'.format(paint))
