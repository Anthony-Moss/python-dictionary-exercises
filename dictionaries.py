meal = {
    'breakfast' : 'waffles',
    'lunch' : 'tacos',
    'dessert' : 'cupcakes',
    'drink' : 'beer'
}
user = {
    'first_name' : 'Sean',
    'last_name' : 'Reid'
}

# print(appropriateMeal['dessert'])
# print(house['kitchen'])
print(user['first_name'])

# if 'cigar' in meal:
#     print('Cuba, we have a cigar.')
# else:
#     print('No cigars, womp womp')

meal['water'] = 'tap'
meal['bread'] = True
meal['drink'] = 'Guinness'
print(meal)

del meal['water']
print(meal)

