#sets means group or set, es una conecccion de datos que no se puede repetir y que tampoco esta ordenada

first = {1,1,2,2,3,4}
#first.add(5)
#first.remove(1)
#print(first)

second = [2,3,4,5]
second = set(second)

print(second)
 

#operators in sets

print(first | second) # this is an union

print(first & second)  #this is an intersection

print(first - second) # this is an a diference

print(first ^ second)  #symmetrical difference , if any number is repeated ,will not print  

if 5 in second:
    print("hello world")