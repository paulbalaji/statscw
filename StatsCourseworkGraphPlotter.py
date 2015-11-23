import math
import matplotlib.pyplot as plt

x_label = "k"
y_label = "standard deviation of Yk"

def getIndividualVariance(k, n):
    top = k * (n - 1)
    bottom = math.pow((k - n + 1), 2)
    variance = top / bottom
    return variance

def getTotalStdDeviation(k):
    varSum = 0
    for n in range(1, k+1):
        varSum += getIndividualVariance(k, n)
    stddev = math.sqrt(varSum)
    return stddev

def calculateAllStdDeviations(k):
    xvals = []
    yvals = []
    for i in range(1, k+1):
        stddev = getTotalStdDeviation(i)
        yvals.append(stddev)
        xvals.append(i)
        string = ""+str(i)+": "+str(stddev)
        print(string)
    return xvals, yvals

def plotGraph(xvals, yvals):
    plt.plot(xvals, yvals, "ro")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

if __name__ == "__main__":
    k = int(input("Give a value for k: "))
    print(x_label + ": " + y_label)
    xvals, yvals = calculateAllStdDeviations(k)
    plotGraph(xvals, yvals)    
    print("\nProgram Complete.")
