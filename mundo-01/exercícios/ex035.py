print('-=' * 20)
print('Triangle Analyzer')
print('-=' * 20)
side1 = float(input('First segment: '))
side2 = float(input('Second segment: '))
side3 = float(input('Third segment: '))

if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print('The segments above CAN FORM a triangle!')
else:
    print('The segments above CANNOT FORM a triangle.')
