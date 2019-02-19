# letters = 'abcdefghijklmnopqrstuvwxyz'
# secret = [1, 0, 3]

# def translate(index, master):
#     return master[index]

# def decode(number_list, master_list):
#     return map_over(number_list, master_list, translate)
    # configuration came in as arguments
    # result = ''
    
    # do translation
    # for each item in number_list
    # find that index in master_list...
    # put that character in result
    # for item in number_list:
        # find that index in master_list...
        # letter = master_list[item]

        # put thar character in result
        # result += letter

        # result += master_list[item]
        # result += translate(item, master_list)
    # return the result
    # return result

# decoded_message = decode(secret, letters)
# print(decoded_message)    


# def map_over(collection, master_list, how):
#     result = ''
#     for item in collection:
#         result += how(item, master_list)
#     return result

# print(map_over(secret, letters, translate))

letters = 'abcdefghijklmnopqrstuvwxyz'
secret = [1, 0, 3] # "bad"
message = 'encode' #[4, 13, 2, 14, 3, 4]
# encoded = 


def translate(index, master):
    return master[index]

def map_over(collection, master, how):
    result = ''
    for item in collection:
        result += how(item, master)

    return result

# give your functions "verb" names
def decode(number_list, master_list):
    return map_over(number_list, master_list, translate)
    # # configuration came in as arguments
    # result = ''
    # # count = 0

    # # do the translation
    # # for each item in number_list...
    # for item in number_list:
    #     # find that index in master_list...
    #     # letter = master_list[item]

    #     # put that character in result
    #     # result = result + letter
    #     # result += letter
        
    #     # result += master_list[item]
    #     result += translate(item, master_list)

    # # return the result
    # return result

# decoded_message = decode(secret, letters)
# print(decoded_message)
print(decode(secret, letters))

def decode_while(number_list, master_list):
    # configuration came in as arguments
    result = ''
    count = 0
    max_length = len(number_list)

    # do the translation
    # for each item in number_list...
    # for item in number_list:
    while count < max_length:
        # find that index in master_list...
        # item = number_list[count]
        # letter = master_list[item]

        # put that character in result
        # result = result + letter
        # result += letter
        
        # result += master_list[item]
        result += master_list[number_list[count]]
        count += 1

    # return the result
    return result

print(decode_while(secret, letters))


print(map_over(secret, letters, translate))



