#los diccionaros son una coneccin de datos que se encuentran agrupados por una llave y un valor

point = {"x": 25,"y": 50 } #only acept string
print(point)
print(point["x"])
print(point["y"])

point["z"] = 45
#print(point,point{"lala"})
if "lala " in point:
    print("i'd faund lala" , point["lala"])

print(point.get("x"))
print(point.get("lala",97))

del point["x"]
del(point["y"])


print(point)
point["x"] = 25

for valor in point:
    print(valor,point[valor])

for valor in point.items():
    print(valor)

for key ,valor in point.items():
    print(key,valor)

# uso realsta de los diccionarois 

users = [
    {"id":1,"name":"chanchy"},
    {"id":2,"name":"happy"},
    {"id":3,"name":"nicolas"},
    {"id":4,"name":"felipe"},

]

for user in users:
    print(user["name"])