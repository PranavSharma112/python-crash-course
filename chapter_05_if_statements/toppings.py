# available_toppings = ['mushrooms','olives','green peppers',
#                       'pepperoni', 'pinepple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']


if 'mushrooms' in requested_toppings:
    print('Adding Mushrooms.')
elif 'pepperoni' in requested_toppings:
    print("Adding Pepperoni.")
elif "extra cheese" in requested_toppings:
    print("Adding Extra Cheese.")

print("\nFinished making your pizza")


# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f'Adding {requested_topping}.')

#     else:
#         print(f"Sorry, we don't have {requested_topping}.")

# print("\nFinished making your pizza!")