#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def generateXYdata(ratingsOfOneCompany):
    numberOfValueJumps =  countValueJumps(ratingsOfOneCompany)
    sortedRatingsOfOneCompany = np.sort(ratingsOfOneCompany)
    y_data = [0.0]
    # y_data.insert(0, 0)
    x_data = [0]
    x_point = 0

    for ratingValue in sortedRatingsOfOneCompany:
        x_point+=1
        x_data.append(x_point)
        y_data.insert(x_point, ratingValue)

    result = [x_data, y_data]
    print('x len ', len(x_data))
    print('y len ', len(y_data))

    fit_curve(model_taylor, x_data, y_data)

    quota = numberOfValueJumps / len(ratingsOfOneCompany)
    title = 'suspicious rating value offsets: '+ str(numberOfValueJumps) + ', equals ' + str(quota)
    plt.scatter(x_data, y_data)
    plt.xlabel("# ratings")
    plt.ylabel("rating value in stars")
    plt.title(title)
    plt.show()
    return result

def countValueJumps(ratingsOfOneCompany):
    valueJumpCount = 0
    for count in range(len(ratingsOfOneCompany)-1):
        ratingOne = ratingsOfOneCompany[count]
        followingRating = ratingsOfOneCompany[count+1]
        if(abs(ratingOne - followingRating) > 2):
            valueJumpCount += 1
    print('suspicious rating value offsets: ', valueJumpCount)
    quota = valueJumpCount / len(ratingsOfOneCompany)
    print('quota: ', quota)
    return valueJumpCount

# define model function:
def model_taylor(x, a, b, c, d, e):
    return  a*x**4 + b*x**3 + c*x**2 + d*x + e

def fit_curve(modelFunction, x_data, y_data):
    initialGuess = [4, 3, 2, 1, 0]
    popt, pcov = curve_fit(modelFunction, x_data, y_data, initialGuess)
    xFit = np.arange(0.0, 200, 0.01)
    plt.plot(xFit, model_taylor(xFit, *popt))
    plt.ylim(0, 6)
    plt.xlim(0, 68)