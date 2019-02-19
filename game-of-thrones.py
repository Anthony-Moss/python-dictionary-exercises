from characters import characters
import requests # makes API requests (this is a third-party module)
import json # convert the API data into python dictionaries and arrays
import time # module for working with timestamps
# print(len(characters))
# jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

# # print out the key names individually
# # for k in jon_snow:
# #     print(k)

# # print out just the values
# # for k in jon_snow:
# #     print(jon_snow[k])

# # print both the key and the value
# for k in jon_snow:
#     print("%s: %s" % (k, jon_snow[k]))

# all characters
# for k in characters:
#     print(k['name'])

# characters starting with 'A'
def find_char_names_start_a():
    a_names = []
    for k in characters:
        if k['name'][0] == 'A':
            a_names.append(k['name'])
    print(len(a_names))

# character names starting with 'z'
def find_char_names_start_z():
    z_names = []
    for k in characters:
        if k['name'][0] == 'Z':
            z_names.append(k['name'])
    print(len(z_names))

# all dead characters
def find_dead_chars():
    dead_chars = []
    for k in characters:
        if k['died'] != '':
            dead_chars.append(k)
    print(len(dead_chars))

# char most titles
def find_char_most_titles():
    titles = []
    for k in characters:
        titles.append(len(k['titles']))
        if max(titles) == len(k['titles']):
            print(k['name'])

# how many are Valyrian?
def find_Valyrian():
    valyrian_people = []
    for k in characters:
        if k['culture'] == 'Valyrian':
            valyrian_people.append(k['name'])
    print(len(valyrian_people))

# who plays 'hot pie'
def who_plays_hot_pie():
    for k in characters:
        if k['name'] == 'Hot Pie':
            print(k['playedBy'])

# how many characters are not in the show
def find_char_not_in_show():
    not_in_show = []
    for k in characters:
        if k['tvSeries'] == ['']:
            not_in_show.append(k['name'])
    print(len(not_in_show))

# list of characters with last name Targaryen
def create_list_of_targaryens():
    targaryens = []
    for k in characters:
        if 'Targaryen' in k['name']:
            targaryens.append(k['name'])
    print(targaryens)


# from characters import characters

# def houses(characters):
#     house = ""
#     counter = 0
#     for k in characters:
#         if k['allegiances'] != []:
#             while counter < len(k['allegiances']):
#                 house += (k['allegiances'][counter] + " ")
#                 counter += 1
#             counter = 0
#     house_list = house.rstrip(" ").split()
#     return house_list

# house = houses(characters)
# print(house)

# def house_number(house):
#     allegiance_dict = {}
#     for i in house:
#         if i in allegiance_dict.keys():
#             allegiance_dict[i] += 1
#         else:
#             allegiance_dict[i] = 1
#     return allegiance_dict

# print(house_number(house))

# count the number of people who are part of a house
def make_house_histogram(character_list):
    histogram = {}

    #do things
    for person in character_list:

        # what do i check for each person
        allegiances = person['allegiances']
        # allegiances is a list of urls
        # it looks like this:
        # ["https://anapioficeandfire.com/api/houses/378"]
        for house in allegiances:
            # do something with that
            # histogram[house] = 1
            if house in histogram:
                histogram[house] += 1
            else:
                histogram[house] = 1
            (histogram[house])

    return histogram


def pretty_print_histogram(histogram):
    for house in histogram:
        print("%s has %d members" % (house, histogram[house]))

def translate_address_to_house_name(URL):
    house_name = ''
    r = requests.get(URL)
    house_info = r.json()
    house_name = house_info['name']
    return house_name

def convert_to_nice_names(histogram):
    nice_histogram = {}

    for url in histogram:
        house_name = translate_address_to_house_name(url)
        nice_histogram[house_name] = histogram[url]
    return nice_histogram

ugly_histogram = make_house_histogram(characters)
pretty_histogram = convert_to_nice_names(ugly_histogram)
pretty_print_histogram(pretty_histogram)

# print(translate_address_to_house_name("https://www.anapioficeandfire.com/api/characters?page=%d&pageSize=100"))
# pretty_print_histogram(make_house_histogram(characters))
# print(make_house_histogram(characters))
# {
# "https://anapioficeandfire.com/api/houses/378": 45,
# https://anapioficeandfire.com/api/houses/377": 49,
# "https://anapioficeandfire.com/api/houses/378: 100,
# }