money=1331
x=1

print "move Alice: ", x
while money>=x:
    print "Bazilio can make move: ", x ,"or", x+1
    a= input("move Bazilio: ")
    print a
    if (a == x) or (a == x+1):
        money = money-a
        x=x+1
        print "move Alice: ", x
        money = money-x
        print money
    else:
        print "wrong move"
    print " "
print "Alice win!"
