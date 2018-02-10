import random

b=[[random.randint(0,0) for x in range(8)] for j in range (8)]
for i in range(len(b)):
    for j in range(len(b[i])):
        s=str(b[i][j])
        s=s.rjust(4)
        print s,
    print '\n'
print "-------"*6
x=2
y=3

print "Start", "x:", x, "y:", y
while (x<>8 and y<>6) or (x<>7 and y<>7):
    x=x+2
    y=y+1
    print "AI", "x:", x, "y:", y
    if (x==8 and y==6)  or (x==7 and x==7):
        print "AI win!"
        break
    print "Me. Can move only: ", "x:", x+2,"y:",  y+1, "or", "x:",x+1,"y:", y+2
    x=input("x:")
    y=input("y:")
    
