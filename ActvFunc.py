import math
import matplotlib.pyplot as plt
def sigmoid(x,beta):
    f=1/(1+beta*math.exp(-x))
    return(f)

def dsigmoid(x,beta):
    f=beta*x/(1-beta*x)
    return(f)
'''
beta: [b1,b2,b3,b4] and
&& alpha in:

(b1*e**x)-(b2*e**-x)
--------------------
(b3*e**x)+(b4*e**-x)

for x=alpha*t
'''
def tanH(x,alpha,*beta):
    b1,b2,b3,b4=beta
    x=alpha*x
    f=((b1*math.exp(x))-(b2*math.exp(-x)))/((b3*math.exp(x))+(b4*math.exp(-x)))
    return(f)
