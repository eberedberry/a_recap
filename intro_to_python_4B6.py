new_black = 10
# print(new_black)
# print(type(new_black))

# float_me = 0.5
# print(float_me)
# print(type(float_me))


stringify = "We had a downpour in Lagos 2 days ago!"
# print(stringify)
# print(type(stringify))

my_verdict = True
# print(my_verdict)
# print(type(my_verdict))

random_stuff = ['music', "sports", True, 99.9]
# print(random_stuff)
# print(type(random_stuff))

new_guy = ("45", False, 101)
# print(new_guy)
# print(type(new_guy))

sports = {"football", "cricket", "basketball", "cricket"}
# print(sports)
# print(type(sports))


my_info = {
    "name" : "Adamu",
    "gender" : "Male",
    "age" : 12
}

# print(my_info)
# print(type(my_info))




###ARITHMETIC OPERATIONS
my_mod = 33 % 4
# print(my_mod)


my_quote = 33 // 4
# print(my_quote)

r_power = 5 ** 4
# print(r_power)


####COMAPRISON OPERATORS
first_num = 67
second_num = 40

# quick_check = first_num != second_num
# print(quick_check)

# feedback = ((first_num % 2 != 0) or (second_num > first_num)) and not((second_num == 40) or (second_num // 2 != 0))
# print(feedback)

career = "She is a model who lives in California"
# output = "She I" in career

# scores = [62, 55, 72, 89]
# check = 62 in scores

# print(check)


###CONTATENATION
# first_phrase = "Hello"
# second_phrase = "there, welcome!"

# full_sent = first_phrase + " " + second_phrase
# print(full_sent)


career = "She is a model who lives in California!"
desired_char = career[-1]
desired_portion = career[ : 10]
# print(desired_portion)


# age_limit = 10
# report_template = "You can't gain access unitl your are {} years old.".format(age_limit)

# report_template = f"You can't gain access unitl your are {age_limit} years old."

# print(report_template)


##ESCAPE CHARACTER
source_of_income = 'The nation\'s crude oil'
# print(source_of_income)

refined_career = career.title()

quick_search = career.startswith("She is")

# another_search = career.index("nigeria")
# print(another_search)

# print(refined_career)

career = "!She is a model who lives in California!"
trans_list = career.split("!")
print(trans_list)

new_career = career.replace("California", "Texas")
# print(new_career)

trimmed = career.lstrip("!")
# print(trimmed)


####LIST
random_stuff = ["pawn", "phone", "pen", "ball", False, 99.69, "pawn", 2021, 4+2j, "water"]
# print(random_stuff)

desired_item = random_stuff[-1]
# print(desired_item)

desired_items = random_stuff[ : : 3]
# print(desired_items)

random_stuff[1] = "water"

random_stuff[3 : 6 : 2] = ["chair", True]


# print(random_stuff)

no_of_occurence = random_stuff.count("water")
# print(no_of_occurence)

# print(random_stuff.index("pawn"))

random_stuff.remove("water")

random_stuff.append("Checkmate")

# print(random_stuff)

backup_list = random_stuff.copy()
# print(backup_list)

random_stuff.insert(0, "awesome")
# print(random_stuff)

scores = [31, 19, 20, 56, 45]
# print(scores)
# print("\n")
scores.sort(reverse = True)
# print(scores)


# print(random_stuff)
# print("\n")
# random_stuff.reverse()
# print(random_stuff)

quick_one = ("Brilliant", "Shy", "Great")
# print(quick_one[1:])

# quick_one[1] = "Bold"
# print(quick_one)





####SETS
grocery_cart1 = {"Bread", "Oranges", "Jam", "Fruit Juice", "Eggs", "Butter", "Cookies"}
grocery_cart2 = {"Eggs", "Yam", "Grapes", "Cookies", "Apple", "Carrot", "Bread", "Ice Cream"}

print(grocery_cart1)
print("\n")
print(grocery_cart2)
print("\n")

grocery_cart2.discard("Yam")
grocery_cart2.add("Youghurt")
# print(grocery_cart2)

merged_carts = grocery_cart1.union(grocery_cart2)
# print(merged_carts)

# grocery_cart1.update(grocery_cart2)
# print(grocery_cart1)

backup_cart1 = grocery_cart1.copy()
backup_cart2 = grocery_cart2.copy()

cart1_only = grocery_cart1.difference(grocery_cart2)
print(cart1_only)

# grocery_cart2.difference_update(grocery_cart1)
# print(grocery_cart2)

common_groceries = grocery_cart1.intersection(grocery_cart2)
# print(common_groceries)

backup_cart1.intersection_update(backup_cart2)
# print(backup_cart1)

taking_out_duplicates = grocery_cart1.symmetric_difference(grocery_cart2)
# print(taking_out_duplicates)
 

#####DICTIONARIES!!!
customer_info = {
    "name" : ["Mike Aubentraut", "Uzo Chuks", "Tom Whiteside", "Mary Jane"],
    "gender" : ["Male", "Male", "Male", "Female"],
    "age" : [22, 29, 34, 18],
    "nationality" : ["American", "Nigerian", "Canadian", "Jamaican"]
}

# print(customer_info)

all_names = customer_info["name"]
# print(all_names)

all_nationalities = customer_info.get("nationality")
# print(all_nationalities)

all_keys = customer_info.keys()
# print(all_keys)

all_values = customer_info.values()
# print(all_values)

all_items = customer_info.items()
# print(all_items)

customer_info.update({"occupation" : ["Actor", "Banker", "Footballer", "Experience Engineer"]})

customer_info.pop("age")

customer_info.clear()
# print(customer_info)



####BUILTIN FUNCTIONS
# # get_data = input("Enter integers here: ")
# #to have access to the integers
# con_list = get_data.split(" ")
# #to convert/change the entries to proper integers
# con_list[0] = int(con_list[0])
# con_list[1] = int(con_list[1])
# con_list[2] = int(con_list[2])
# con_list[3] = int(con_list[3])
# con_list[4] = int(con_list[4])


# # smallest_integer = min(con_list)
# # print(smallest_integer)
# new_list = list(set(con_list))
# new_list.sort()

# output = new_list[-2]

# print(output)

first_list = ["high", "low", "middle", "high-lows", "dark space"]
second_list = [1, 2, 3]

zipped_object = zip(first_list, second_list)
print(list(zipped_object))












