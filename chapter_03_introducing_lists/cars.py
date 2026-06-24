cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# the sort method makes irreversible changes 
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Temporary Sorting its a function and its a temporary sorting
print(sorted(cars))


# Printing a list in reverse order it is a method also applies permanent change
cars.reverse()
print(cars)

