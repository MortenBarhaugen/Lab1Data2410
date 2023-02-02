def jains(x1, x2):
    x1, x2 = float(x1), float(x2) #Throughput numbers
    xsum = float(x1) + float(x2)
    above = xsum**2 #Calculating final sum above division line

    x3 = x1**2
    x4 = x2**2
    xsum2 = 2*(x3+x4) #Calculating final sum below division line

    final = above / xsum2 #Calculates final result
    print(final) #Prints result
    
jains(input('Number 1: '), input('Number 2: '))