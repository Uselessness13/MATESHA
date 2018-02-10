a = 0
b = 20
while b != 0:
    N = int(input("Enter number: "))
    if N == 1:
        a = 3
        print(a)
        b = b - N - a
        a = 0
        print(b)
    elif N == 2:
        a = 2
        print(a)
        b = b - N - a
        a = 0
        print(b)
    elif N == 3:
        a = 1
        print(a)
        b = b - N - a
        a = 0
        print(b)
print("AI player win!")
