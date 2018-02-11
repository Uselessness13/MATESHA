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
y = 3

print("Start", "x:", x, "y:", y)
while x != 9 and y != 9:
    if x == y:
        x = 8
        y = 8
        print("AI", "x:", x, "y:", y)
        print("AI win!")
        break
    elif x == 8:
        y = 8
        print("AI", "x:", x, "y:", y)
        print("AI win!")
        break
    elif y == 8:
        x = 8
        print("AI", "x:", x, "y:", y)
        print("AI win!")
        break
    elif x != 8 and y != 8:
        if y != 7:
            if x != 7:
                y = y + 1
                x = x + 1
                print("AI", "x:", x, "y:", y)
                if x == 8 and y == 8:
                    print("AI win!")
                    break
            else:
                y = y + 1
                print("AI", "x:", x, "y:", y)
                if x == 8 and y == 8:
                    print("AI win!")
                    break
        else:
            x = x + 1
            print("AI", "x:", x, "y:", y)
            if x == 8 and y == 8:
                print("AI win!")
                break
        x = int(input("x:"))
        y = int(input("y:"))
