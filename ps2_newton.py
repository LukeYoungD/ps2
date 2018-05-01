# 6.00 Problem Set 2
#
# Successive Approximation
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    total = 0.0
    pos = 0
    # print("degree = ", degree)
    for e in poly:
        # print (str(e) + " ")
        # print ("pos =" + str(pos) + " " + str(x**pos))
        
        total += (e*(x**pos))
        # degree = degree -1
        pos += 1
    # print("Poly Evaluates to: " + str(total))
    return total
# end evaluate_poly


def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    newPoly = ()
    pos = 0
    for e in poly:
        # print (str(e) + " ")
        # print ("pos =" + str(pos) + " " + str(x**pos))
        
        if pos != 0:
            t = e*pos
            newPoly += (t,)
        pos += 1
    print("The derivative of: " + str(poly) + " is: " + str(newPoly))
    return newPoly
# end compute_deriv

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    iterations = 0
    x_1 = x_0
    primePoly = compute_deriv(poly)    
    # computes the value first
    difference = evaluate_poly(poly, x_0)
    # print(" Initial guess results in y = " + str(difference))
    # then starts the loop and will not exicute if perfect guess
    while (abs(difference) >= epsilon):
        # print("x_0 = " + str(x_0) + " x_1 = " + str(x_1))
        x_1 = x_0 - (evaluate_poly(poly, x_0) / evaluate_poly(primePoly, x_0))
        difference = evaluate_poly(poly, x_1)
        x_0 = x_1
        iterations += 1

    print("Found root at x = " + str(x_0)+ " y = " + str(evaluate_poly(poly, x_0)) + " and it took " + str(iterations) + " iterations")
    return (x_0, iterations)

## Test Code Follwoing
expr = (0.0, 0.0, 5.0, 9.3, 7.0)
print evaluate_poly(expr, -13)

exprTwo = (-13.39, 0.0, 17.5, 3.0, 1.0)
compute_deriv(exprTwo)

exprThree = (-13.39, 0.0, 17.5, 3.0, 1.0)
guess = 0.1
tolerance = 0.0001
compute_root(exprThree, guess, tolerance)
