def whileloop(numinput):
    i = 0
    numbers = []

    for i in range(0, numinput):
        print "At the top i is %d." % i
        numbers.append(i)
        i += 1
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i
        
    print "The numbers:"

    for num in numbers:
        print num
whileloop(5)

