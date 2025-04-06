#tuples - comprehension lists
# we going to change from users to names list

users = [
    ["emiliano",4],
    ["felipe",1],
    ["pulga",5]
]

#names = []
#for user in users:
#    names.append(user[0])
#print(names)

#map
#same but in one code line

#names = [users[0] for  user in users]

#filter elements
name = [user for user in users if user[1] > [2]] 
print(name)
