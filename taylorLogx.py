import numpy as np
import matplotlib.pyplot as plt
from math import factorial

a = 1

# A list of the 4 first derivatives (including the 0th derivative) of the function f(x)=log(x)
derivativeList = [lambda x: np.log(x), lambda x: 1/x, lambda x: -1/x**2, lambda x: 2/x**3]

# Function that calculates the value of the n'th part in a Taylor polynomial
def P(x, n):
    # We gather the n'th derivative of the function f(x) from our derivativeList
    derivative = derivativeList[n]

    # Return the value of the n'th part of the Taylor polynomial
    return derivative(a)/factorial(n)*(x-a)**n

dx = np.linspace(0.05, 1.95, 100)

exact_yArray = np.log(dx)
P1_list = []; P2_list = []; P3_list = []

# Calculate the y-values of the Taylor polynomials for n=1, 2, 3
for i in range(len(dx)):
    P1_list.append(P(dx[i], 1))
    # We use the value of P1 to calculate the value of P2, and then likewise with P3, to save computing power:
    P2_list.append(P1_list[i] + P(dx[i], 2))
    P3_list.append(P2_list[i] + P(dx[i], 3))

# Plotting:
ax = plt.subplot()
ax.set(xlabel = "x", ylabel = "y")
ax.plot(dx, exact_yArray, "r", label="f(x) = log(x)")
ax.plot(dx, P1_list, "b", label="Taylor approximation n = 1")
ax.plot(dx, P2_list, "y", label="Taylor approximation n = 2")
ax.plot(dx, P3_list, "c", label="Taylor approximation n = 3")
ax.grid()
ax.legend(loc="best")
plt.show()

"""
Kjøreeksempel:
python taylorLogx.py
Et koordinatsystem med 4 funksjoner skrives ut
"""
