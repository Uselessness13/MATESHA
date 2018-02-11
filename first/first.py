move = 0
left = 20


def printer(move, left):
    print("AI move" + move)
    print("Stones left" + left)


while left != 0:
    N = int(input("Enter number: "))
    if N == 1:
        move = 4 - N
        left -= (N + move)
        printer(move, left)
    elif N == 2:
        move = 4 - N
        left -= (N + move)
        printer(move, left)
    elif N == 3:
        move = 4 - N
        left -= (N + move)
        printer(move, left)
print("You lose :(")
