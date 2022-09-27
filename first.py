# A simple string example

short_string_variables = "have a great weak, Ninjas"
print(short_string_variables)

# Print the first letter of a single variables
first_letter_variables = "New York City"[0]
print(first_letter_variables)

#Mixed upper lower case letter variable
mixed_letter_variable = "This a Mixed Variable"
print(mixed_letter_variable.lower())
#Lenght of the variables
print(len(mixed_letter_variable))

#Use '+'sign inside a print command

first_name = "David"
print("First name is : " +first_name)

#Replace a part of a string
first_serial_number = "ABC123"
print("change serial number #1: " +first_serial_number.replace('123' , '456'))

#Replace a part of a string -> Twice!
second_serial_number = "ABC123ABC"
print("Changed serial number #2 : " +second_serial_number.replace('ABC' ,  'ZZZ' , 2))

#Take a part of  a variable, according to specific index range
range_of_index = second_serial_number[0:3]
print(range_of_index)

# One last string + adding spaces between multiple variables is print
first_word = "think"
second_word = "your"
third_word = "NINJAS !"
print(first_word+" "+second_word+" "+third_word)