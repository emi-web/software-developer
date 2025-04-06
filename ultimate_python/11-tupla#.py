#una tupla es lo mismo que una lista , la unica diferencia es que no la puedes modificar

numbers = [1,2,3] + [4,5,6]
print(numbers)


point = tuple([1,2])
print(point)

lessNumbers =  numbers[:2]
print(lessNumbers)

first,second,*another = numbers
print(first,second,another)

for n in numbers:
    print(n)

# the only way to modyfi is

listNumbers = list(numbers)
listNumbers[0] = "happy chanchy"
print(listNumbers)
