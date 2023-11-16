'''Q3: The problem in this section is the same for all groups. The length of the arc between any two points a and b for a 
function f (x) is defined as S = ∫ √ (1 + (f ′(x))2 dx) Write a program to that takes as inputs a function f (x), 
an interval [a, b] and outputs the arc length over [a, b]. The program should use centered difference 
to approximate f ′(x) and trapezoidal rule to approximate the integral. Hence, the program should also take in n, 
the number of sub-divisions of the interval [a, b] as input. Use the same n for the approximations of the derivative 
and the integral.'''

import numpy as np

def arc_length(f,a,b,n): 
    dx = (b-a)/n
    h = 0.0001
    F_a = np.sqrt(1+((f(a+h)-f(a-h))/(2*h))**2)
    F_b = np.sqrt(1+((f(b+h)-f(b-h))/(2*h))**2)
    e = (F_a + F_b)/2
    F_sum = 0.0
    for i in range(1,n):  
        xi = a + i*dx
        F_sum += np.sqrt(1+((f(xi+h)-f(xi-h))/(2*h))**2)
    return dx*(e+F_sum)

#print(arc_length(np.exp2, 0, 1, 100000))


