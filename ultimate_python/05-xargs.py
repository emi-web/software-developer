#multiple arguments

def plus(*numbers):
    resoult = 0
    for number in numbers:
        resoult += number
    print(resoult)


plus(2, 5,7)
plus(2,5)
plus(2,8,7,45,32)