import sympy
# 微分計算
x = sympy.Symbol('x')
y = x**2 - 2*x + 2
Dy = sympy.Derivative(y, x).doit()
print(Dy)