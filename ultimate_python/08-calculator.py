"""Module providing a function printing python version."""

n1 = input("enter first number")
n2 = input("enter second number")

n1 = int(n1)
n2 = int(n2)

sum = n1 + n2
subtraction = n1 - n2
multi = n1 * n2
div = n1 / n2

message = f"""
for numbers {n1} and {n2}
the result of addition is {sum}
the result of subtraction is {subtraction}
the result of multiplication is {multi}
the result of division is {div}
"""
print(message)