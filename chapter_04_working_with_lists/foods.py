my_foods = ['pizza', 'falafel', 'carrot cake']
# Main code logic  
friend_foods = my_foods[:]  # copying the lists for modification and retention of of original lists.

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are: ")
print(my_foods)

print("\nMy Friend's favourite foods are:")
print(friend_foods)

# A couple of things to take notes on
#  friend_foods = my_foods
# what happens is instead of copying one into the other they point to same memory space changes to one is reflected in the other

