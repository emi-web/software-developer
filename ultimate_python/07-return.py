#how to assign the result to a variable outside this function for later use (return)
def plus(a,b):
    result = a + b
    return result

c = plus(1,2)  # c going to be 3
d = plus(c,2)

print(d)