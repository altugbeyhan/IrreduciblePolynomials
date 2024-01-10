# n = max degree < 8, p = prime

from sympy import symbols, factor, expand, degree
x = symbols('x')

def firstPart(n,p):
    polynomials = []
    print(f"All Polynomials for n={n}, p={p}:")
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    for e in range(p):
                        for f in range(p):
                            for g in range(p):
                                for h in range(p):
                                    poly = a*x**7 + b*x**6 + c*x**5 + d*x**4 + e*x**3 + f*x**2 + g*x + h
                                    if degree(poly)<=n:
                                        polynomials.append(poly)
                                        print(poly)

    return polynomials

def secondPart(polynomials,p):
    reducible = []
    print("\nReducible Polynomials:")
    for poly in polynomials:
        factored = factor(poly, domain=f'GF({p})')
        if degree(poly)!=1:
            if poly not in [x**2, x**3, x**4, x**5, x**6, x**7]:
                if factored != poly:
                    reducible.append(poly)
                    print(poly)

    return reducible

def thirdPart(polynomials, reducible):
    irreducible = set(polynomials) - set(reducible)
    print("\nIrreducible Polynomials:")
    for poly in irreducible:
        print(poly)

def GF(n,p):
    all_polys = firstPart(n,p)
    reducible_polys = secondPart(all_polys,p)
    thirdPart(all_polys, reducible_polys) 
    
GF(n=3,p=2)

"""

OUTPUT

All Polynomials for n=3, p=2:
0
1
x
x + 1
x**2
x**2 + 1
x**2 + x
x**2 + x + 1
x**3
x**3 + 1
x**3 + x
x**3 + x + 1
x**3 + x**2
x**3 + x**2 + 1
x**3 + x**2 + x
x**3 + x**2 + x + 1

Reducible Polynomials:
x**2 + 1
x**2 + x
x**3 + 1
x**3 + x
x**3 + x**2
x**3 + x**2 + x
x**3 + x**2 + x + 1

Irreducible Polynomials:
0
1
x**3 + x + 1
x**3
x
x**2 + x + 1
x**2
x**3 + x**2 + 1
x + 1

"""
