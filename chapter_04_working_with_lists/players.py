players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])

print(players[1:4])

print(players[:4])  # from start to designated

print(players[2:])  # from designated to end

print(players[-3:]) # prints the last 3 elements

# looping through slicing 
print("Here, are the first three players on my team:")
for player in players[-3:]:
    print(player.title())

