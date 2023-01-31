def jains():
    x1, x2 = 25, 25
    xsum = x1 + x2
    above = xsum**2
    print(above)

    x3 = x1**2
    x4 = x2**2
    xsum2 = 2*(x3+x4)
    print(xsum2)

    final = above / xsum2
    print(final)

jains()

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