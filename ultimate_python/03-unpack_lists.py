numbers = [1, 2, 3, 4, 5, 6, 7 , 8, 9,]

#first ,second ,thirst = numbers
#print(first,second,thirst)

#print the first number
#print the first and second number

first, second, *another = numbers
print(first)

print(first,second,another)

#print the first and second element

first,*another,last = numbers
print(first,second,another)