#Write a function that takes a dictionary and returns a list of all the keys in the dictionary.
def get_items(dictionary):
    return list(dictionary.items())
my_dict = {'name': 'arbish', 'age': 19, 'city': 'karachi'}
items_list = get_items(my_dict)
print(items_list) 
