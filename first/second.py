money = 1331
move = 1

print("move Alice: ", move)
while money >= move:
    print("Bazilio possible moves: ", move, "or", move + 1)
    a = int(input("Bazilio move: "))
    print(a)
    if (a == move) or (a == move + 1):
        money -= a
        move += 1
        print("Alice move: ", move)
        money -= move
        print(money)
    else:
        print("wrong move")
    print(" ")
print("Alice win!")
