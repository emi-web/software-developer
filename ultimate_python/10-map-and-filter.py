users = [
    ["emiliano",4],
    ["felipe",1],
    ["pulga",5]
]


#map
names = list(map(lambda user: user[0],users))
#print(names)

#filter
names = list(filter(lambda user:user[1]>2,users))
print(users)
