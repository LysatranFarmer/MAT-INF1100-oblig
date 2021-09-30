import numpy as np
import math as math

def productNotation(n, i):
    value = float(n)                   # Når j=1, vil verdien være
    for j in range(2, (i+1)):    # Vi starter på 2, ettersom vi allerede har regnet ut uttrykket for j = 1
         value *= float((n-j+1)/j)
         # if j < 110 and j > 80:
         #     print(value)

    print(f"n = {n} og i = {i} gir: {float(value)}")

productNotation(5000, 4)       # Test nr 1
productNotation(1000, 500)     # Test nr 2
productNotation(100000, 99940) # Test nr 3

"""
Viktig å bemerke seg:
Test nr 3 vil møte på en overflow for j=87, ettersom tallet blir over Python sin max float value, og da vil den returnere enten inf, eller en likende verdi
(man kan fjerne kommentarene på linje 8 og 9, og se når det skjer). Verdien vil etter hvert gå ned, men den viser det fortsatt som inf, selv om
verdien for den siste testen teknisk sett er mindre enn den ved test nr 2.
"""


"""
Kjøreeksempel (Test nr 2)
>> python binomial_koeffisient.py
n = 5000 og i = 4 gir: 26010428123750.0
n = 1000 og i = 500 gir: 2.702882409454359e+299
n = 100000 og i = 99940 gir: inf
"""
