# 3.1 
friends =['miller', 'artyom', 'hunter', 'uhlman','till']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

# 3.2
print(f'Friend 1: {friends[0]}')
print(f'Friend 2: {friends[1]}')
print(f'Friend 3: {friends[2]}')
print(f'Friend 4: {friends[3]}')

# 3.3
best_transports = ['bosshoss', 'hummer', 'yacht']
print(f'I would like to own a {best_transports[2]}.')

# 3.4 
dinner_invites = ['Sandman', 'Berzerker', 'templar']
print(f'You are invited to the party {dinner_invites[1]}.')

#3.5  Modifying variables intead of poping / deleting and then inserting or appending them
dinner_invites[0] = 'bourbon'
print(f'You are invited to the party {dinner_invites[0]}.')

#3.6
dinner_invites.insert(0,'arnold')
dinner_invites.insert((len(dinner_invites)//2),'silvester')
dinner_invites.append("coleman")
print(dinner_invites)

# 3.7 
print(f"We will meet next time {dinner_invites.pop()}.")
print(f"We will meet next time {dinner_invites.pop()}.")
print(f"We will meet next time {dinner_invites.pop()}.")
print(f"We will meet next time {dinner_invites.pop()}.")
del dinner_invites[0]
del dinner_invites[0]
print(dinner_invites)


# 3.8
PlacesToVisit=['challenger deep', 'Mt.Everest', "Antartica", "Sahara", 'Belize']
print(PlacesToVisit)

print(sorted(PlacesToVisit))
print(PlacesToVisit)

print(sorted(PlacesToVisit,reverse=True))
print(PlacesToVisit)

PlacesToVisit.reverse()
print(PlacesToVisit)

PlacesToVisit.reverse()
print(PlacesToVisit)

PlacesToVisit.sort()
print(PlacesToVisit)

PlacesToVisit.sort(reverse=True)
print(PlacesToVisit) # we cannot produce ouput in one line as the method does not return any value it returns none.


# 3.9
print(f'no. of people invited in dinner{len(dinner_invites)}')

# 3.10
dinner_invites.insert(0,'Sam')
dinner_invites.append('Tom')
print(sorted(dinner_invites))
print(sorted(dinner_invites,reverse=True))
dinner_invites.sort()
print(dinner_invites)
dinner_invites.sort(reverse=True)
print(dinner_invites)
dinner_invites.pop()
del dinner_invites[0]
print(dinner_invites)
