def jainsall2(bw): 
    xlist = bw
    xres = []


    for i in xlist:        #hardcoding the input to check which values are given in kbps
        streng = 'Kbps'
        if(streng in i):    #calculates new value if true
            temp = eval(i[0])
            temp = temp/1024    #divide value by 1024 to get mbps
            xres.append(temp)    #appends value to the new array
        else:            #does the same as the other functions
            temp = i[0]
            xres.append(eval(temp))

    xlist2 = []            #array to hold the powered numbers
    xsum = 0

    for i in xres:        #same as previous function from janisall
        xsum += i
        xlist2.append(i**2)

    above = xsum**2

    xsum2 = 0
    for i in xlist2:
        xsum2 += i

    final = above / (len(xlist2)*xsum2)

    print(final)

bw = []
with open("data2.txt") as file_name: #function reads the data2.txt file
    for line in file_name:
        bw.append(line.split())      #splits the lines into sub arrays f.eks [['value','unit'], ... , ['value','unit']]

print(bw)
jainsall2(bw) #initiating functions