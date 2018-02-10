a=48
x=1
print "48 parts"
while a>=2:
    print "Darya take:", x
    a=a-x
    print a
    if a>=2:
        print "Marya take:", x
        a=a-x
        print a
    
print "Darya win!"
