# PhoneBook exercises 

# phonebook_dict = {
#     'Alice' : '703-493-1834',
#     'Bob' : '857-384-1234',
#     'Elizabeth' : '484-584-2923'
# }

# print(phonebook_dict['Alice'])

# phonebook_dict['Kareem'] = ('938-489-1234')


# del phonebook_dict['Alice']
    


# phonebook_dict['Bob'] = ('968-345-2354')

# for key in phonebook_dict:
#     print("%s's phone number is %s" % (key, phonebook_dict[key]))

# Exercise 2
# ramit = {
#     'name': 'Ramit',
#     'email': 'ramit@gmail.com',
#     'interests': ['movies', 'tennis'],
#     'friends': [
#     {
#     'name': 'Jasmine',
#     'email': 'jasmine@yahoo.com',
#     'interests': ['photography', 'tennis']
#     },
#     {
#     'name': 'Jan',
#     'email': 'jan@hotmail.com',
#     'interests': ['movies', 'tv']
#     }
#     ]
# }

# print(ramit['email'])

# print(ramit['interests'][0])

# print(ramit['friends'][0]['email'])

# print(ramit['friends'][1]['interests'][1])


# Letter Summary
# user_input = input("Please enter a word: ")
# print(user_input)
# letter_dict = {}
# def letter_histogram(user_input):
#     for letter in user_input:
#         if letter in letter_dict:
#             letter_dict[letter] += 1
#         else:
#             letter_dict[letter] = 1
#     print(letter_dict)
            
# letter_histogram(user_input)

# word summary
def word_summary():
    user_input = str(input('Please enter a sentance: '))
    word_dict = {}
    list1 = user_input.lower().split(' ')
    print(list1)
    for word in list1:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    # print(word_dict)
    # print(list(word_dict.keys())[-1])
    print(word_dict)

    # dict_pairs = word_dict.items()
    # for word in dict_pairs:
    #     word_list = 
# Bonus challenge    
# take in dictionary 
# convery dictionary to a list
# sort list
# return last 3 values of new list 
    items = word_dict.items()
    print(items)
    # create list of lists with values of dictionaries to sort
    words_list=[ [v[1],v[0]] for v in items]
    words_list.sort()
    # print(words_list[::-1])
    # print(words_list[(len(words_list)-2)::1])
    print(words_list)
    # create top_three list to hold top 3 words with their values from sorted list
    counter = 0
    top_three = []
    while counter < 3:
        top_three += words_list.pop()
        counter += 1
    print('The top three words are:\n%s: %s\n%s: %s\n%s: %s' % (top_three[1], top_three[0], top_three[3], top_three[2], top_three[5], top_three[4]))
    # print(str(top_three[0]) +': ' + str(top_three[1]) + '\n' + str(top_three[2]) +': ' + str(top_three[3]))
    # print(str(top_three[4]) +': ' + str(top_three[5]))
    
word_summary()
