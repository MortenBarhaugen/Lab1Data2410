def jainsall():
    xlist = [25, 25]
    xlist2 = []
    xsum = 0
    for i in xlist:
        xsum += i
        xlist2.append(i**2)
    
    above = xsum**2

    xsum2 = 0
    for i in xlist2:
        xsum2 += i

    final = above / (len(xlist2)*xsum2)

    print(final)

jainsall()