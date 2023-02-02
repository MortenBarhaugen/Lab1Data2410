def jainsall(streng):
    xlist = []
    xlist = streng.split()      #transforms input string into subparts in the array
    xlist2 = []
    xsum = 0
    for i in xlist:
        temp = eval(i)          #tranlates from string to numeric value
        xsum += temp
        xlist2.append(temp**2)  #everything else does the same as the previous task

    above = xsum**2

    xsum2 = 0
    for i in xlist2:
        xsum2 += i

    final = above / (len(xlist2)*xsum2)

    print(final)

jainsall(input('Type a sequence of numbers seperated by space: '))