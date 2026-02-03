# %% [markdown]
# # Introduction: Variables and Data Types

# %% [markdown]
# below are some codes that need be familiar with, including basic Hello World; print; function lists; variables

# %%
import math
print("Hello World")
print("*"*10)


def new_func():
    result = 2 + 3
    print(result)


new_func()

x = 1
y = 2
unit_price = 3

# %% [markdown]
# # fundamentals_1: *Define ctrl+r to run the code

# %% [markdown]
# ### variables define

# %%
students_count = 1000
rating = 4.99  # flowing point of number
is_published = True  # Boolean value can either be true or false
course_name = "Python Programming"  # string
print(students_count)

# make sure your variable names are descriptive
# cannot start with a number

# "" ''  '''  """ """ are used for multi line comments

# %% [markdown]
# ### ''' long line type in

# %%
message = '''Hello John,

This is a multi-line message.
I hope you are enjoying the course.
Best regards,
Instructor'''
print(message)


# %% [markdown]
# ### characters finding

# %%
course_name = "Python Programming"
print(len(course_name))
print(course_name[0])  # first character
print(course_name[-1])  # last character
print(course_name[0:3])  # first three characters
print(course_name[0:])  # from first to end
print(course_name[:3])  # first three characters
print(course_name[:])  # complete string

# %% [markdown]
# ### how to include quotes in a string
#

# %%
course = 'Python "Programming'
print(course)
course_1 = "Python 'Programming"
print(course_1)
course_2 = "Python \'Programming"
print(course_2)
course_3 = "Python \\ Programming"
course_4 = "Python \nProgramming"
print(course_3)
print(course_4)

# formatted strings
first_name = "John"
last_name = "Smith"
full = first_name + " " + last_name
print(full)

full_1 = f"{first_name} {last_name}"
# f-string
print(full_1)


# %% [markdown]
# ### conversion of characters into LARGE or small capitals

# %%
course_name = "Python Programming"
print(course_name.upper())
# .upper() method converts all characters to 大写
course_capital = course_name.upper()
print(course_capital)
print(course_name.lower())
# .lower() method converts all characters to 小写

# %%
print(course_name.title())
# .title() method converts the first character of each word to 大写

print(course_name.strip())
# .strip() method removes any whitespace from the beginning or the end
print(course_name.find("Pro"))
# .find() method returns the starting index of the substring

print(course_name.replace("P", "j"))
print("Pro" in course_name)
print("swift" not in course_name)

# %% [markdown]
# # numbers

# %%
# numbers
x = 1
x = 1.1
# x =  # a + bi     #i is the complex number
x = 1 + 2j
# three types of number we have in the python

# %%
print(10 + 3)  # addition
print(10 - 3)  # subtraction
print(10 * 3)  # multiplication
print(10 / 3)  # division always results in flowing point number
print(10 // 3)  # floor division results in integer
print(10 % 3)  # modulus returns the remainder
print(10 ** 3)  # exponentiation

# %%
y = 10
y = y + 3
y += 3
print(y)

# working with numbers
print(round(2.9))  # round to nearest integer
print(abs(-2.9))  # absolute value

print(math.ceil(2.2))  # rounds up to nearest integer
print(math.floor(2.9))  # rounds down to nearest integer

# %%
x = input("x:")  # this function returns to a string
print(type(x))

# %%
x = 1
y = int(x) + 1  # convert string to integer
print(f"x:{x}, y:{y}")  # f-string to format the output

# Falsy values: 0, 0.0, "", None, False

# %% [markdown]
# # fundamentals_2: programming codes

# %%
# exercise
# 1. A website requires a username and password to register. The username must be less
# than 10 characters long and the password must be at least 8 characters long. Write a
# program that checks if the username and password meet these requirements.
username = input("Enter username: ")
password = input("Enter password: ")
if len(username) < 10 and len(password) >= 8:
    print("Username and password are valid")
else:
    print("Username or password are invalid")
# 2. A bank offers a loan to customers based on their credit score and annual income.
# The minimum credit score required is 700 and the minimum annual income required is
# $50,000. Write a program that checks if a customer is eligible for a loan
credit_score = int(input("Enter credit score:"))
annual_income = int(input("Enter annual income:"))
if credit_score >= 700 and annual_income >= 50000:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# %% [markdown]
# ### Comparsion operaters
#

# %%

temperature = 35
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature < 10:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Done")
# my vpn location is Hong Kong


# %%
age = 22
if age >= 18:
    print("eligible")
else:
    print("not eligible")

# %% [markdown]
# ### Turnernary operator

# %%
age = 22
if age >= 18:
    message = "eligible"
else:
    message = "not eligible"

message = "eligible" if age >= 18 else "not eligible"
print(message)


# %% [markdown]
# ### logical operaters

# %% [markdown]
# and , or , not \\
# and = all conditions must be true \\
# or = at least one condition must be true \\
# not = reverses the boolean value \\

# %%
high_income = True
good_credit = True

if high_income and good_credit:
    print("eligible for loan")
else:
    print("not eligible for loan")


# %%
if high_income or good_credit:
    print("eligible for loan")
if not high_income:
    print("not eligible for loan")

# %%
student = True
if not student:
    print("eligible for discount")
else:
    print("not eligible for discount")

# %%
student_1 = False
if not student_1:
    print("eligible for discount")
else:
    print("not eligible for discount")

# %%
if (high_income or good_credit) and not student:
    print("eligible for loan")
else:
    print("not eligible for loan")

# %% [markdown]
# ### operator precedence

# %%
if high_income or good_credit or not student:
    print("eligible for loan")

# %%
if high_income and good_credit and not student:
    print("eligible for loan")

# %%
price = 1000000
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("eligible for loan")
else:
    print("not eligible for loan")

# %% [markdown]
# ### chaining comparison operaters

# %%
# age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("eligible")
else:
    print("not eligible")

# equivalent to
age = 22
if age >= 18 and age < 65:
    print("eligible")

# %%
# exercise

if 10 == "10":
    print("true")
else:
    print("false")
# false because 10 is integer and "10" is string

if 10 != 10.0:
    print("true")
else:
    print("false")
# false because 10 and 10.0 are equal

print("sending a message")

# %% [markdown]
# ### use loop to create repetition

# %%
for number in range(3):
    print("Attempt", number)

# %%
for number in range(3):
    print("Attempt", number + 1, "times")

# %%
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# %%
for number in range(1, 4):
    print("Attempt", number, number * ".")


# %%
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# %%
successful = True
for number in range(3):
    print("Attempt", number)
    if successful:
        print("Successful")
        break
# jump out of the loop, use 'break' statement

# %%
successful = False
for number in range(3):
    print("Attempt", number)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
# 'else' block in loop will be executed only if the loop is not terminated by 'break' statement
# useful when searching for an item in a collection


# %% [markdown]
# ### nested loops

# %%
for x in range(5):  # outer loop
    for y in range(3):  # innner loop
        print(f"({x}, {y})")

# %% [markdown]
# (0, 0) first iteration of outer loop, first iteration of inner loop

# %% [markdown]
# ### iterables

# %%
print(type("5"))
print(type(range(5)))

for x in "Python":
    print(x)

# %%
for x in range(5):
    print(x)

# %%
for x in ["Mosh", "John", "Sarah"]:
    print(x)

# %%
for x in (1, 2, 3):
    print(x)

# %% [markdown]
# ### while loop

# %%
number = 100
while number > 0:
    print(number)
    number //= 2

# %%
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
# keep asking for input until user types 'quit'
# Lowercase method to make the input case-insensitive

# %% [markdown]
# ### infinite loop

# %%
command = ""
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

# %%
# exercises
range(1, 10)
for number in range(1, 10):
    print(number)
# print all even numbers between 1 and 10
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")


# %% [markdown]
# # Functions

# %%
def greet():
    print("Hi there")
    print("Welcome aboard")


greet()

# %%


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Susan", "Bi")
greet("John", "Smith")

# %%


def greet(name):
    print(f"hi{name}")

# 1-perform a task
# 2-return a value


def get_greeting(name):
    return f"hi {name}"


message = get_greeting("Susan")
print(message)

# %%
open("context.txt", "w").write(message)

# %%


def increrment(number, by=1):
    return number + by


result = increrment(2, 3)
print(result)

# %%
print(increrment(2, by=1))

# %%
print(increrment(2, 5))

# %%


def multiply(x, y):
    return x * y

# %%


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
