from matplotlib import *
from numpy import *
from matplotlib.colors import *
from matplotlib.pyplot import *
from control import *

k = 5
x = arange(0.,20.,0.1)
t = arange(0.,20.,0.1)

def f(a):
    if (a<1):
        return 0
    else:
        return 1

#u = map(lambda a: int(a>300),x)
u = map(f,x)

#num = [0.5 * k]
#den = [1,2,0]  
#very interesting stuff
tau = 35
k2 = 2
eps = 0.5

#num = [tau*tau] # unit 2
#den = [1,2*tau*eps,tau*tau]  #unit 2

num3 = [21*tau] # unit 3
den3 = [1,4,3]  #unit 3 
num4 = [1] # unit 3
den4 = [0,1,0]  #unit 3 
#sys = tf(num,den)
sys1= tf(num3,den3)
feedback(k2, sys1)
sys2 = tf(num4,den4)
feedback(k2, sys1+sys2)

T, yOut, xOut = lsim(feedback(k2, sys1+sys2),u,t)
grid(True)
plot(yOut,T)
show()

