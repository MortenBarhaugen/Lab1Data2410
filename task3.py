def jainsall2(bw):
    xlist = bw
    xres = [eval(i) for i in xlist]
    xlist2 = []
    xsum = 0
    for i in xres: #Iterates through the xres-array
        xsum += i #Adds the elemets from the xres-array to xsum
        xlist2.append(i**2) #Squares the elements from xres and adds them to xlist2
    
    above = xsum**2 #Calculates result above division line

    xsum2 = 0
    for i in xlist2: #Iterates through xlist2
        xsum2 += i #Adding all elements from xlist2 to xsum2

    final = above / (len(xlist2)*xsum2) #Calculates final result

    print(final)

bw = []
with open("data.txt") as file_name:
    for line in file_name: #Iterates through the lines in data.txt
        bw.append(line.split()[0]) #Adds the first element in the sub-array to the bw-array
    
jainsall2(bw)