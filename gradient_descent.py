from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

f = 6 * (x ** 6) + 2 * (x ** 4) * (y ** 2) + 10 * (x ** 2) + 6 * x * y + 10 * (y ** 2) - 6 * x + 4

fpx = f.diff(x)
fpy = f.diff(y)
grad = [fpx,fpy]

#Start point
theta_x = 0
theta_y = 0

alpha = 0.005
iterations = 0
precision = 1/10**15
max_iterations = 10000

while True:
    temp_theta_x = theta_x - alpha * N(fpx.subs(x, theta_x).subs(y, theta_y)).evalf()
    temp_theta_y = theta_y - alpha * N(fpy.subs(y, theta_y)).subs(x, theta_x).evalf()

    iterations += 1
    if iterations > max_iterations:
        print("Too many iterations.")
        break

    if abs(temp_theta_x - theta_x) < precision and abs(temp_theta_y - theta_y) < precision:
        print(f"Number of iterations: {iterations}")
        print(f"x0 = {temp_theta_x}")
        print(f"y0 = {temp_theta_y}")
        break

    theta_x = temp_theta_x
    theta_y = temp_theta_y