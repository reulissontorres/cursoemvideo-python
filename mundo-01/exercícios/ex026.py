sentence = input('Enter a sentence: ').upper().strip()

letter_a_count = sentence.count('A')
first_a_position = sentence.find('A') + 1
last_a_position = sentence.rfind('A') + 1

print('The letter A appears {} times in the sentence.'.format(letter_a_count))
print('The first letter A appeared at position {}'.format(first_a_position))
print('The last letter A appeared at position {}'.format(last_a_position))
