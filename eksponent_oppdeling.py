import numpy as np
import math as math

def productNotation(n, i):
    value = float(n)                   # Når j=1, vil verdien være n
    expCount = 0
    for j in range(2, (i+1)):    # Vi starter på 2, ettersom vi allerede har regnet ut verdien for j=1
        value *= float(n-j+1)/float(j)
        
        # Vi ønsker å kun ha verdier mellom 10 og 1, dermed bruker vi while setninger:
        while value > 10:
            value /= float(10)
            expCount += 1

        while value < 1:
            value *= float(10)
            expCount -= 1

    # Skriver ut binomial koeffisienten på standardform:
    print(f"{value}e+{expCount}")

productNotation(5000, 4)
productNotation(1000, 500)
productNotation(100000, 99940)


"""
Kjøreeksempel:
>> python eksponent_oppdeling.py
2.601042812375e+13
2.7028824094543573e+299
1.180691979962599e+218
"""
