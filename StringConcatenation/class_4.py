###STRING CONCATENATION###

# first_name = "John"
# last_name = "Doe"

# print(first_name + " " + last_name)

# name = input("Tell us your name:")
# # age = input("How old are you?")
# year_of_birth = int(input("Year of Birth"))

# current_year = 2022
# age = current_year - year_of_birth

# print(f"welcome, {name}, We can see that you are {age} years old.")

###Indexing & slicing##

# b = "I am just good you know"
# print(b[2])

# b = "I am just good you know"
# print(b[-10])

# b = "I am just good you know"
# print(b[5:9])

# b = "I am just good you know"
# print(b[0:4]+" "+b[10:14])

# first_name = "emmanuel"
# last_name = "johnson"


# print(first_name[0:3] + " " + first_name[-3:])

first_name = input("first name: ")
last_name = input("last name: ")

username = last_name[:3] + first_name[-3:]
print(username)


