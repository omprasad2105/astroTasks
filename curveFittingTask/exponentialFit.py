import numpy as np
import matplotlib.pyplot as plt

print("Enter the no of data points: ", end='')
n=int(input())
data_x=[]
data_y=[]
for i in range(n):
    xi=float((input("enter x value:")))
    yi=float((input("enter y value:")))
    data_x.append(xi)
    data_y.append(yi)
    print()

# I will will perform linear regression on the log values     y = Ae^(kx)  =>  (log y) = kx  + (log A)
x = data_x
y = np.log(data_y)

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
k, logA = np.dot(a_inv, b)

plt.scatter(data_x,data_y, color='red')
plt.plot(data_x,[np.exp(k*xi + logA) for xi in x], color='blue')
plt.legend(["Data", "Best fit exponential"])
plt.show()