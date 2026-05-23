import numpy as np
import matplotlib.pyplot as plt

m = int(input("Enter the order of polynomial :"))
n=int(input("Enter the no of data points: "))
x=[]
y=[]
for i in range(n):
    xi=float((input("enter x value:")))
    yi=float((input("enter y value:")))
    x.append(xi)
    y.append(yi)
    print()

def poly(x,coeffs):
    return np.sum([coeffs[k] * x**k for k in range(m+1)])

def x_nthpower_sum(n):
    return np.sum([xi**n for xi in x])
def x_nthpower_y_sum(n):
    return np.sum([(xi**n * yi) for xi,yi in zip(x,y)])

a = np.array([[x_nthpower_sum(j+k) for j in range(m+1)] for k in range(m+1)])
b = np.array([x_nthpower_y_sum(k) for k in range(m+1)])

a_inv = np.linalg.inv(a)
coeffs = np.dot(a_inv, b)  #[coeff] = (a^-1)b

plt.scatter(x,y, color='red')
plt.plot(x,[poly(xi, coeffs) for xi in x], color='blue')
plt.legend(["Data", f"Best fit degree {m} polynomial"])
plt.show()