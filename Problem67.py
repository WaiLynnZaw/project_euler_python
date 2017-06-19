with open('data.txt') as f:
    numbers = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            numbers.append(line)

    for x in range(len(numbers)-1,-1,-1):
        for y in range(0,x):
            numbers[x-1][y]+=max(numbers[x][y],numbers[x][y+1])
    print numbers[0][0]
