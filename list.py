friends = ["prasanth","Vinoth","ANil"]
celebrity=["VK","MSD","ST","VS","SG"]

print(friends)
print(friends[1])
print(len(friends))
print(friends[1:])
#To add an element to the list
friends.append("Vidhya")
#To insert an element in the specified index
print(friends.insert(0,"Kannan"))
friends[len(friends)-2]= "Anil"
print(friends)
#Extend is used add a list to another list

friends.extend(celebrity)
print("EXtended list ",friends)
print(friends.__contains__("MSD"))
print(friends.__sizeof__())

#To remove an element
friends.reverse()
print(friends)

# TO empty the list we suse
#friends.clear()
print(friends)

#Pops the last element out and removes from the list
print(friends.pop())
print(friends)

# To find the index of a element in a list
print(friends.index("MSD"))

friends.append("SG")
print(friends.count("SG"))

print(friends.sort())
#Reverses the list from the given order
celebrity.reverse()
print(celebrity)
print(friends)

#To copy the lsit

friends_copy = friends

print(friends_copy[2:])

