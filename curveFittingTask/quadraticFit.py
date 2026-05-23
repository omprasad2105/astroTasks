import numpy as np
import matplotlib.pyplot as plt

print("Enter the no of data points: ", end='')
n=int(input())
x=[]
y=[]
for i in range(n):
    xi=float((input("enter x value:")))
    yi=float((input("enter y value:")))
    x.append(xi)
    y.append(yi)
    print()

x_fourthpower_sum = np.sum([xi**4 for xi in x])
x_cube_sum = np.sum([xi**3 for xi in x])
x_square_sum = np.sum([xi**2 for xi in x])
x_sum = np.sum(x)

x_square_y_sum = np.sum([(xi**2)*yi for xi,yi in zip(x,y)])
xy_sum = np.sum([xi*yi for xi,yi in zip(x,y)])
y_sum = np.sum(y)

a00 = x_fourthpower_sum
a01 = x_cube_sum
a02 = x_square_sum
a10 = x_cube_sum
a11 = x_square_sum
a12 = x_sum
a20 = x_square_sum
a21 = x_sum
a22 = n
a = np.array([[a00, a01, a02], [a10, a11, a12], [a20, a21, a22]])
b0 = x_square_y_sum
b1 = xy_sum
b2 = y_sum
b = np.array([b0, b1, b2])

a_inv = np.linalg.inv(a)
a, b, c = np.dot(a_inv, b)  #[a, b, c] = (a^-1)b

plt.scatter(x,y, color='red')
plt.plot(x,[(a*xi**2 + b*xi + c) for xi in x], color='blue')
plt.legend(["Data", "Best fit quadratic"])
plt.show()