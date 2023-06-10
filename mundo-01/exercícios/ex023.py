number = int(input('Enter a number: '))

unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10

print('Analyzing the number {}'.format(number))
print('Unit: {}'.format(unit))
print('Ten: {}'.format(ten))
print('Hundred: {}'.format(hundred))
print('Thousand: {}'.format(thousand))
