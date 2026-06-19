# 2.1 Simple message assigned using a variable and then printing it 
message = "This is practice."
print(message)

# 2.2 Simple Messages: Assign a message to a variable, and print that message.
# then change the value to a new variable to a new message, and print the new message 

msg = "Hello Wolrd!"
print(msg)
msg = "Hello Python"
print(msg)

# 2.3 Personal Message: Use a variable to represent a person's name,and print a message
# a message to that person. your message should be simple, such as, 
# "Hello Eric, Would You like to learn some Python today?"

Erics_message = "Hello Eric, Would You like to learn some Python today?"
print(Erics_message)

# 2.4 Name Cases: Use a variable to represent a person then print their name in uppercase, lowercase and title
name = "James bond"
print(name.title())
print(name.upper())
print(name.lower())

# 2.5 Famous Quote: Find a Quote from a famous person you admire. Print the quote and 
# the name of the author. Your output  should look something like the following, including the quotation marks:
# Albert Einstein once said, "A person who never made a mistake never tried anything new"

NameOfFamousPerson = "Marcus Aurelius"
Quote = "Become indifferent to what makes no difference"

print(f'{NameOfFamousPerson} once said, "{Quote}"')

# 2.6 Famous Quote 2: Repeat Excercise 2.5, but this time, represent the famous person's
# name using a variable called famous_person. Then compose your message and represent it 
# with a new a new variable called message . Print that message .

# Solved above

# 2.7 Stripping Names use a variable  to represent a person's name, and include 
# some whitespace characters at the beginning and end of the name /
# Make Sure you use each characters at the beginning and end of the name 
#       Print the name once, so the whitespace around the name is displayed. 
# then print the name using each of the three stripping functions, lstrip(), rstrip(), strip()
name = "  James  "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# 2.8 Fil Extensions: Python has a removesuffix() metod that works exactly like removepreffix(),
# Assign the value 'python_notes.txt' to a variable called filename.
# the use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))