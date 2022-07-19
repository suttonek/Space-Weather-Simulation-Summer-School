#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Eric Sutton'
__email__ = 'eric.sutton@colorado.edu'

from math import factorial
from math import pi


def cos_approx(x, accuracy=10):
    """Returns an approximation to the cos(x) function based on the Taylor
    expansion sum from 0 to 'accuracy' of ( (-1)^n * x^(2*n) / (2*n)! ), where
    'n' is the index into the expansion term, 'x' is the input into the Cosine
    function, and n='accuracy' is the last term in the truncation.
    test line
    """
    # Generate individual terms of the Taylor expansion
    summands = [(-1)**n*x**(2*n)/factorial(2*n) for n in range(accuracy+1)]
    # Return the sum of the Taylor expansion terms
    return sum(summands)



# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    print("cos(0) = ", cos_approx(0))
    print("cos(pi) = ", cos_approx(pi))
    print("cos(2*pi) = ", cos_approx(2*pi))
    print("more accurate cos(2*pi) = ", cos_approx(2*pi, accuracy=50))
