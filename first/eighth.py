a = 6
b = 8
summ = a * b
move = 1

print("Now we have " + str(summ) + " pieces")
while summ >= 2:
    print("Dasha takes:", move)
    summ -= move
    print("Pieces left:" + summ)
    if summ >= 2:
        print("Marya takes:", move)
        summ -= move
        print("Pieces left" + summ)
print("Darya won!")
