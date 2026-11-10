car = 'subaru'

# 5 Tests that evaluate to True
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')

print("\nIs the length of car == 6? I predict True.")
print(len(car) == 6)

print("\nDoes car start with 's'? I predict True.")
print(car.startswith('s'))

print("\nIs car lowered == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

print("\n" + "-"*20 + "\n")

# 5 Tests that evaluate to False
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

print("Is car == 'Subaru'? I predict False.")  # Case-sensitive!
print(car == 'Subaru')

print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

print("\nIs the length of car > 10? I predict False.")
print(len(car) > 10)

print("\nDoes car end with 'x'? I predict False.")
print(car.endswith('x'))

# 1. Tests for equality and inequality with strings
string1 = "Apple"
string2 = "Banana"
print("Is string1 == string2? I predict False.")
print(string1 == string2)

print("\nIs string1 != string2? I predict True.")
print(string1 != string2)

# 2. Tests using the lower() method
user_input = "Python"
print("\nIs user_input.lower() == 'python'? I predict True.")
print(user_input.lower() == 'python')

# 3. Numerical tests
age_1 = 21
age_2 = 18

print("\nIs age_1 == 21? I predict True.")
print(age_1 == 21)

print("\nIs age_1 != age_2? I predict True.")
print(age_1 != age_2)

print("\nIs age_2 > age_1? I predict False.")
print(age_2 > age_1)

print("\nIs age_1 >= 21? I predict True.")
print(age_1 >= 21)

# 4. Tests using 'and' and 'or' keywords
print("\nIs age_1 > 20 and age_2 < 20? I predict True.")
print(age_1 > 20 and age_2 < 20)

print("\nIs age_1 < 20 or age_2 < 15? I predict False.")
print(age_1 < 20 or age_2 < 15)

# 5. Test whether an item is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("\nIs 'mushrooms' in requested_toppings? I predict True.")
print('mushrooms' in requested_toppings)

# 6. Test whether an item is NOT in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

print("\nIs user not in banned_users? I predict True.")
print(user not in banned_users)

# 5.3 Alien Colors #1:
print("\n # 5.3")
import random
alien_color = ['green', 'yellow', 'red']
z = random.choice(alien_color)
if 'green' in z:
    print("+5 points")
elif 'yellow' in z:
    print('+ 10 points')
elif 'red' in z:
    print('+ 15 points')
elif 'brown' in z:
    print('+ 0 points')
else:
    print('no points for you!')


# 5.6 stages of life
print("\n#5.6")

r = [1,2,4,7,17,39,67,156,20000]
n = random.choice(r)
if n<2:
    print("baby")
elif n>=2 and n<4:
    print("toddler")
elif n>=4 and n<13:
    print("kid")
elif n>=13 and n<20:
    print("teenager")
elif n>=20 and n<65:
    print("adult")
elif n>=65 and n<=160:
    print("elder")
else:
    print("Liar!")


