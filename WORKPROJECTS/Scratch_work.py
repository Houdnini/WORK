from sympy import cos, symbols, solve
# Be careful of * imports, * imports could lead to confusion between modules imported
x, y, z = symbols('x y z')

x1 = cos(x)
y1 = cos(2*x)
tofx = solve(y-x1, y)
print(tofx)

