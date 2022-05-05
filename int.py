# MUST KNOW BASIC PYTHON

# Init Method
class Sample1:
    def __init__(self, first, last, interest, phone):
        self.first = first
        self.last = last
        self.interest = interest
        self.phone = phone

g1 = Sample1("First Name", "Last Name", "Interest", 1234)
print("Guest last name: " + g1.last)

# Dictionary
price_list = {"jeans": 255, "trousers": 149, "t-shirt": 69} # dict syntax
price_list.update = ({"boots": 50, "sneakers": 370}) # add new item in dict
price_list2 = {"Someting": 55}
combined_price_list = zip(price_list, price_list2) # combines two dict

# Using Dictionary
quiz_score = {"Rex": 98, "Ian": 83, "Bob":72, "Lin": 87}
print(quiz_score.get("Bob")) # retrieve information from key
print(quiz_score.pop("Bob")) # removes bob from dict. if no params -> removes last item
print(quiz_score.keys()) # returns all keys in the dict
print(quiz_score.values()) # returns all values in the dict
print(quiz_score.items()) # returns a tuple of key value pairs

# Nested Dictionaries
characters = {1:{"name": "something", "Element":"Ice"}, 2:{"name": "something"}}

# Creating, Writing, and Appending Files 
f = open("new file.txt", "w") # write - writes a file or create it if doesn't exist.
f = open("new file.txt", "x") # create - create the specified file, returns error if it exist.
f = open("new file.txt", "a") # append - appending files or create it if doesn't exist.

# Reading files
