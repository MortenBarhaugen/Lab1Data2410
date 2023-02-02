def jainsall2(bw):
    xlist = bw
    xres = []


    for i in xlist:
        streng = 'Kbps'
        if(streng in i):
            temp = eval(i[0])
            temp = temp/1000
            xres.append(temp)
        else:
            temp = i[0]
            xres.append(eval(temp))

    xlist2 = []
    xsum = 0

    for i in xres:
        xsum += i
        xlist2.append(i**2)
    
    above = xsum**2

    xsum2 = 0
    for i in xlist2:
        xsum2 += i

    final = above / (len(xlist2)*xsum2)

    print(final)

bw = []
with open("data2.txt") as file_name:
    for line in file_name:
        #print(line.split())
        #bw.append(line.split()[0])
        bw.append(line.split())
    
print(bw)
jainsall2(bw)