from matplotlib import *
from numpy import *
from matplotlib.pyplot import *
from control import *

x = arange(0.,20.,0.01)
t = arange(0.,20.,0.01)

def f(a):
    if (a>1):
        return 0
    else:
        return 1

#u = map(f,x)

k1 = 5 #unit1
num = [0.5 * k1] #unit1
den = [1,2,0]  #unit1
sys = tf(num,den) #unit 1
#T, yOut, xOut = lsim(sys,u,t) #unit 1

tau = 35 #unit 2
k2 = 2 #unit 2
eps = 0.5 #unit 2
num2 = [tau*tau] # unit 2
den2 = [1,2*tau*eps,tau*tau]  #unit 2
sys2 = tf(num2,den2) #unit 2
#T, yOut, xOut = lsim(sys2,u,t) # unit 2

k3=2 # unit 3
k4=3 # unit 3
k5=5 # unit 3
num3 = [21*k3] # unit 3
den3 = [1,4,3]  #unit 3 
num4 = [1] # unit 3
den4 = [0,1,0]  #unit 3 

sys3= tf(num3,den3) # unit 3
sys4 = tf(num4,den4) # unit 3

         
mag, phase, omega = bode(sys2)
figure(1)
plot (omega, mag)
xlabel("x")
ylabel("y")
title("omega, mag")
grid(True)

figure(2)
plot (omega, phase)
xlabel("x")
ylabel("y")
title("omega, phase")
grid(True)
         
def Plot(n, func):
    global x, k4, k5, sys3, sys4, t, sys, sys2
    u = map(func,x)
    T, yOut, xOut = lsim(sys2,u,t)#lsim(feedback(k5, feedback(k4,sys3)+sys4),u,t) # unit 3

    subplot(2,2,n)
    grid(True)
    plot(yOut,T)
Plot(1, lambda a: int(a>1)) # impluse
Plot(2, lambda a: int(a<0.1)*10) #h
Plot(3, lambda a: a) # luft
Plot(4, lambda a: sin(a)) # sin
show()