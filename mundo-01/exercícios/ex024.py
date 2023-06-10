city = input('Which city were you born in? ').strip()

starts_with_santo = city[:5].upper() == 'SANTO'

print(starts_with_santo)
