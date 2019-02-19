letters = 'abcdefghijklmnopqrstuvwxyz'
secret = [1, 0, 3] # "bad"
secret = 'encode' 

def convert_letters_to_numbers(a_letter, master):
    # find a_letter in master
    master.index(a_letter)
    # save the index
    # then return it
    return master.index(a_letter)

print(convert_letters_to_numbers('b', letters))
print(convert_letters_to_numbers('a', letters))
print(convert_letters_to_numbers('d', letters))

def map_over(collection, master, do_translation):
    result = []
    for letter in collection:
        result.append(do_translation(letter, master))
    return result

def encode(message, master):
    return map_over(message, master, convert_letters_to_numbers)


print(encode(secret, letters))