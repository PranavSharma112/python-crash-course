# 4.1 
fav_pizzas =['pineapple pizza', 'chesseburst pizza', 'neapolitan pizza']
for pizza in fav_pizzas:
    print(f"I like {pizza.title()}.")
print("I really love pizza!")

# 4.2 
Animals = ['horse','zebra', 'donkey']
for animal in Animals:
    print(f'{animal.title()} are amazing animals.')
print("All the above stated anmals belong to the  scientific family Equidae and the genus Equus.")

# 4.3
for numbers in range(1,21):
    print(numbers, end=", ")

# 4.4
for n in range(1,1000000):
    print(n,end=",")
print()

# 4.5
million = []
for number in range(0,1000000):
    million.append(number)

print(f'Min: {min(million)}')
print(f"Max: {max(million)}")
print(f"Sum: {sum(million)}")

# 4.6
for odd in range(1,21,2):
    print(odd,end=", ")
print()

# 4.7
for three in range(3,33,3):
    print(three,end = ", ")
print()

# 4.8
cubes = []
for cube in range(1,11):
    cubes.append(cube**3)
print(cubes)

# 4.9 
print([cube**3 for cube in range(1,11)]) # Important

# 4.10
cubes = []
for cube in range(1,11):
    cubes.append(cube**3)
print("The first 3 elements in the list are ",cubes[:3])
print("The 3 middle elements in the list are ", cubes[4:7])
print("The last 3 elements in the list are ", cubes[7:], end="\n")

# 4.11 

fav_pizzas =['pineapple pizza', 'chesseburst pizza', 'neapolitan pizza']
friend_pizzas = fav_pizzas[:]
fav_pizzas.append('sicilian pizza')
friend_pizzas.append('pepperoni pizza')
print("My favourite pizzas")
for pizza in fav_pizzas:
    print(f"I like {pizza.title()}.")
print("My friend's favourite pizzas")
for pizza in friend_pizzas:
    print(f"I like {pizza.title()}.")

# 4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
# Main code logic  
friend_foods = my_foods[:]  # copying the lists for modification and retention of of original lists.

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are: ")
for food in my_foods:
    print(food, end=', ')

print("\nMy Friend's favourite foods are:")
for food in friend_foods:
    print(food, end=', ')

# A more cleaner way to join using join
print("My favourite foods are:", ", ".join(my_foods) + ".")

print("My Friend's favourite foods are:", ", ".join(friend_foods) + ".")

# 4.13
restaurant_foods = ('salads', 'desserts','appetizers', 'main course', 'side dishes')
for food in restaurant_foods:
    print(food.title())
print()

restaurant_foods = ('soups', 'desserts','appetizers', 'main course', 'beverages')
for food in restaurant_foods:
    print(food.title())


