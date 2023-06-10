a = int(input('First value: '))
b = int(input('Second value: '))
c = int(input('Third value: '))

# Checking which is the smallest
smallest = a
if b < a and b < c:
    smallest = b
if c < a and c < b:
    smallest = c

# Checking which is the largest
largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c

print('The smallest value entered was {}'.format(smallest))
print('The largest value entered was {}'.format(largest))
