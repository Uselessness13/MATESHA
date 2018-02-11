import random

b = [[random.randint(0, 0) for x in range(8)] for j in range(8)]
for i in range(len(b)):
    for j in range(len(b[i])):
        s = str(b[i][j])
        s = s.rjust(4)
        print(s, end=' ')
    print('\n')
print("-------" * 6)
x = 1
y = 1
print("Start", "x", x, "y", y)
while x < 7 or y < 7:
    if x % 2 == 1 and y % 2 == 1:
        x = x + 1
        y = y + 1
    elif y % 2 == 1:
        y = y + 1
    elif x % 2 == 1:
        x = x + 1
    print("AI", "x", x, "y", y)
    print("Me ")
    x = int(input("x"))
    y = int(input("y"))
print("AI win!")
