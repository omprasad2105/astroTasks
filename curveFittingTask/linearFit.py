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

x_square_sum = np.sum([xi**2 for xi in x])
x_sum = np.sum(x)

xy_sum = np.sum([xi*yi for xi,yi in zip(x,y)])
y_sum = np.sum(y)

a00 = x_square_sum
a01 = x_sum
a10 = x_sum
a11 = n
a = np.array([[a00, a01], [a10, a11]])
b0 = xy_sum
b1 = y_sum
b = np.array([b0, b1])

a_inv = np.linalg.inv(a)
m, c = np.dot(a_inv, b)  #[m, c] = (a^-1)b

plt.scatter(x,y, color='red')
plt.plot(x,[m*xi + c for xi in x], color='blue')
plt.legend(["Data", "Best fit line"])
plt.show()