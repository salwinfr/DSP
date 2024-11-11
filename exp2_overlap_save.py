import numpy as np
from numpy import *
x=[1,2,3,4,5,6,7,8]
h=[1,-1]
N=4
n1=len(x)
M=len(h)
L=N-M+1
if(N!=M):
  for i in range(M,N):
    h.append(0)

row_number=n1//L
if((n1%L)==0):
  row_number=n1//L 
else:
  row_number=n1//L +1

column_number=(M-1)+L
X=np.zeros((row_number+1,column_number))
k=0
for i in range(0,row_number):
  for j in range(M-1,column_number):
    X[i][j]=x[k]
    k=k+1
    if(k==n1):
      break
if X[row_number-1][column_number-1]!=0:
  
  for j in range(0,M-1):
     X[row_number-1+1][j]=x[n1-M+1+j]
  

for i in range(1,row_number):
  for j in range (0,(M-1)):
    if(X[i][j]==0):
      X[i][j]=X[i-1][j+N-M+1]





def find_cir_conv(x1,x2):
    N1 = len(x1)
    N2 = len(x2)
    N =max([N1,N2])
    
    x1 = pad(x1, (0, N - len(x1)))
    x2 = pad(x2, (0, N - len(x2)))
    conv=zeros((N,N))

    for i in range(N):
        conv[:,i]=roll(x1,i)
    result = dot(conv,x2)
    return result

output=[0]*((row_number+1)*column_number)
for i in range(0,row_number+1):
   output[i]=find_cir_conv(X[i],h)
    
count=0
y=[0]*(25)
for i in range(0,row_number+1):
  for j in range(M-1,column_number):
    y[count]=output[i][j]
    count=count+1
    

y = [int(x) for x in y]
print("output is:",y[0:n1+M-1])