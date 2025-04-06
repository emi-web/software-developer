#sort lists

numbers = [2,4,1,45,75,22]

#numbers.sort(reverse=True)
numbers2 = sorted(numbers)
print(numbers)
print(numbers2)

users = [
    [4,"emiliano"],
    [1,"felipe"],
    [5,"pulga"]
    ]
users.sort()
print(users)

#another table but the numbers are on the another side
users = [
    ["emiliano",4],
    ["felipe",1],
    ["pulga",5]
    ]

def sort(element):
    return element[1]
users.sort(key=sort)
print(users)