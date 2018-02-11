import random

b = [[random.randint(0, 0) for x in range(8)] for j in range(8)]
for i in range(len(b)):
    for j in range(len(b[i])):
        s = str(b[i][j])
        s = s.rjust(4)
        print(s, end=' ')
    print('\n')
print("-------" * 6)

x = 2
y = 1
print("Start", "x", x, "y", y)

while x < 8 and y < 8:
    if x > y:
        y = x
    else:
        x = y
        print("Kasparov", "x", x, "y", y)
        print("Karpov")
        x = int(input("x"))
        y = int(input("y"))
print("Kasparov win!")
