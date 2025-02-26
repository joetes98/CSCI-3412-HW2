import math
from scipy.special import lambertw
import pandas as pd

def squareRoot(time):
    n = time**2
    return n

def nSq(time):
    n = time**(1/2)
    return n

def nCubed(time):
    n = time**(1/3)
    return n

def nExp(time):
    n = math.log(time, 2)
    return n

def nFactorial(time):
    n = 0
    # iterate over each value of n until condition n value is found
    while(True):
        fact = math.factorial(n)
        if fact > time:
            break
        else:
            n += 1
    return n-1

def nLogN(time):
    # Lambert W function to solve nlogn = t equation
    n = (time * math.log(2, math.e)/lambertw(time * math.log(2, math.e)))
    return n
    
def main():

    # define various times in microseconds
    second = 10**6
    minute = 60 * second
    hour = 60 * minute
    day = 24 * hour
    month = 30 * day
    year = 365 * day
    century = 100 * year

    timeArray = [second, minute, hour, day, month, year, century]

    table = []

    print("logn")
    logn = []
    #logn.append("Log(n)")
    for x in timeArray:
        print("2^"+'{:.2e}'.format(x))
        logn.append("2^"+'{:.2e}'.format(x))
    table.append(logn)

    sqrtroot = []
    #sqrtroot.append("sqrt(n)")
    print("sqrt(n)")
    for x in timeArray:
        print('{:.2e}'.format(squareRoot(x)))
        sqrtroot.append('{:.2e}'.format(squareRoot(x)))
    table.append(sqrtroot)

    n = []
    #n.append("n")
    print("n")
    for x in timeArray:
        print('{:.2e}'.format(x))
        n.append('{:.2e}'.format(x))
    table.append(n)

    nlogn = []
    #nlogn.append("nlog(n)")
    print('nlogn')
    for x in timeArray:
        print(math.floor(nLogN(x)))
        nlogn.append(math.floor(nLogN(x)))
    table.append(nlogn)
    
    nSquare = []
    #nSquare.append("n^2")
    print("n^2")
    for x in timeArray:
        print(math.floor(nSq(x)))
        nSquare.append(math.floor(nSq(x)))
    table.append(nSquare)

    nCube = []
    #nCube.append("n^3")
    print("n^3")
    for x in timeArray:
        print(math.floor(nCubed(x)))
        nCube.append(math.floor(nCubed(x)))
    table.append(nCube)

    twoPow = []
    #twoPow.append("2^n")
    print("2^n")
    for x in timeArray:
        print(math.floor(nExp(x)))
        twoPow.append(math.floor(nExp(x)))
    table.append(twoPow)

    nFact = []
    #nFact.append("n!")
    print('n!')
    for x in timeArray:
        print(math.floor(nFactorial(x)))
        nFact.append(math.floor(nFactorial(x)))
    table.append(nFact)

    df = pd.DataFrame(table)
    columnLabels = ["second", "minute", "hour", "day", "month", "year", "century"]
    rowLabels = ['Log(n)', 'Sqrt(n)', 'n', 'nLog(n)', 'n^2', 'n^3', '2^n', 'n!']

    df.index = rowLabels
    df.columns = columnLabels

    print(df)

    # outputs html table from pandas dataframe
    html = df.to_html()
    #print(html)

if __name__ == '__main__':
    main()
