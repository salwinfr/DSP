#LINEAR CONVOLUTION
import numpy as np
a = "yes"
while a.lower() == "yes":
    def linear_convo(x, h):  # Indented this block under the while loop
        l1 = len(x)
        l2 = len(h)
        y = np.zeros(l1 + l2 - 1)
        for i in range(l1 + l2 - 1):
            y[i] = 0
            for j in range(l1):
                if i - j >= 0 and i - j < l2:
                    y[i] += x[j] * h[i - j]
        return y

    x = list(eval(input("Enter the elements in x[n]:")))
    h = list(eval(input("Enter the elements in h[n]:")))
    y = linear_convo(x, h)
    print("Linear convolution result= ", y)
    a = input("Do you want to continue?yes/no: ")
