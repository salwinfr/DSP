#linear_using_circular
import numpy as np

def circular_convolution(x, h):  # Define circular_convolution
    N = max(len(x), len(h))
    x = x + [0] * (N - len(x))
    h = h + [0] * (N - len(h))
    y = [0] * N
    for n in range(N):
        for k in range(N):
            y[n] += x[k] * h[(n - k) % N]
    return y

def linear_using_circular(x, h):
    N = len(x) + len(h) - 1
    for i in range(N - len(x)):
        x.append(0)
    for i in range(N - len(h)):
        h.append(0)
    y = circular_convolution(x, h)  # Now circular_convolution is defined
    y1 = np.array(y).reshape(1, N)
    return y1

a = "yes"
while a.lower() == "yes":
    x = list(eval(input("Enter the elements in x[n]:")))
    h = list(eval(input("Enter the elements in h[n]:")))
    y = linear_using_circular(x, h)
    print(y)
    a = input("Do you want to continue?yes/no: ")
