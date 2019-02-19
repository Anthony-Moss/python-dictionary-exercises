from characters import characters

# who are the top 10 title holders?
top_10_characters_title_num = []
top_10_characters_names = []
# how do i sort a list of dictionaries based on length of list
for k in characters:
    top_10_characters_title_num.append([len(k['titles'])] + [k['name']])
    top_10_characters_title_num_sorted = top_10_characters_title_num.sort()
go_to = len(top_10_characters_title_num)-11
# for every item in top 10 (so 10), we print the name followed by their titles
print(top_10_characters_title_num) # this is not top 10 but all titles and names in order by title
print(top_10_characters_title_num[:go_to:-1]) # this should print top ten if it works save to variable so we can iterate through
print(top_10_characters_title_num[:go_to:-1][0][1]) #prints name of person with most titles if i change last [] to 0 it gets title number
top_10_list = top_10_characters_title_num[:go_to:-1]


# what do i expect/hope-for?
# [
# {
    # name: "Baylon Greyjoy", titles: ['....7 things here']
# },    
# {
    # name: "somebody else...", title: ['....titles here']
# }


