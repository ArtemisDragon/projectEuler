ones = [2,3,4,5,6,7,8,9]
relativePrimeDict = {}
numberSize = 1000

def findFactors(input):
    factors = [1]

    for x in ones:
        if input % x == 0:
            factors.append(x)

    return factors

def isRelativePrime(xFactors, y):
    yFactors = findFactors(y)
    xFactors.reverse()

    for value in xFactors:
        if value == 1:
            return True
        if value in yFactors:
            return False

def getAllRelativePrimes(x):
    xFactors = findFactors(x)
    relativePrimes = []
    y = x - 1

    while y > 1:
        if isRelativePrime(xFactors, y):
            relativePrimes.append(y)
        y -= 1

    relativePrimes.append(1)
    relativePrimeDict[x] = relativePrimes

for i in range(numberSize):
    if i != 0:
        getAllRelativePrimes(i)

# for key in relativePrimeDict:
#     print(key)
#     print(relativePrimeDict[key])