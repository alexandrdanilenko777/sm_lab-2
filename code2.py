#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:35:38 2017

@author: Alexandr
"""

from pylab import *
t=arange(0.0, 1000, 0.01) # задаем массив значений
#x=(t*1j+5)**5 # задаем характеристический полином заведомо устойчивой системы
x=(t*1j+1)*(t*1j-0.2)*(t*1j+2)

re=real(x) # находим действительную часть
im=imag(x) # находим мнимую часть
plot(re, im, linewidth=0.8) # рисуем мнимую и дейстивтельную части
xlabel('Oscilation x') # подписываем ось х
ylabel('Oscilation y') # подписываем ось у
title('Godograf Michailova') # подписываем весь график
grid(True) # рисуем сетку
show() # выводим это все на экран