def getPowerof2(num):
    result = list(map(lambda x: 2 ** x, range(num)))
    resultNum = 0
    for i in range(num):
        resultNum = result[i]
    return resultNum

def getSumOfPowerDigits(num):
    input = getPowerof2(num)
    result = 0
    for i in str(input):
        result += int(i)
    print(result)

getSumOfPowerDigits(1001)
