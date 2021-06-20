from pprint import pprint
# Creating data for the dictionary
engToFra = {
    'courir': 'run',
    'remercier': 'thank',
    'prendre': 'take',
    'réveiller': 'wake',
    'rencontrer': 'meet'
}
pprint(engToFra)

# adding a new word

engToFra['donner'] = 'give'
print('With a new word:', engToFra)

# remove

del engToFra['courir']
pprint(engToFra)

#search

print(engToFra.get('prendre'))

# Replacing data

print(engToFra['donner'])
engToFra['donner'] = 'peas'
print(engToFra)
