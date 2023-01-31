def jainsall2(bw):
    xlist = bw
    xres = [eval(i) for i in xlist]
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
with open("data.txt") as file_name:
    for line in file_name:
        #print(line.split())
        bw.append(line.split()[0])
    
print(bw)
jainsall2(bw)