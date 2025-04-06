#lambda functions

users = [
    ["emiliano",4],
    ["felipe",1],
    ["pulga",5]
    ]


users.sort(key=lambda parametres:parametres[1] )
print(users)