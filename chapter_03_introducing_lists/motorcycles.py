# Top tip:keep the names of your list always in plural if you don't want to sound unintelligent

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Appending
motorcycles.append('bosshoss')
print(motorcycles)
# appends the value to the last to the list 

# a very common way to build list is defining an empty one and then appending all elements one after the other

# Insertion
motorcycles.insert(0,'bmw')
# this operation shifts position of every other value in the list to the right

# Deleting elements in the list
del motorcycles[0]
print(motorcycles)

# Poping
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
print(f"The last motorcycle that I owned was a {popped_motorcycles}")
# removes last element in the list

# removing items from any position
first_owned = motorcycles.pop(0)
print(f"My first motorcycle was a {first_owned}")

# removing items by value 
motorcycles.remove('suzuki')
print(motorcycles)

