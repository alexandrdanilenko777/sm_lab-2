#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:32:53 2017

@author: Alexandr
"""

from pylab import *
t=arange(0.0, 500, 0.01) # задаем массив значений
s=cos(t) # первое колебание
r=cos(5*t) # второе колебание
plot(s, r, linewidth=0.5) # рисуем оба колебания
xlabel('Oscilation x') # подписываем ось х
ylabel('Oscilation y') # подписываем ось у
title('Lissaghu curve 1x2') # подписываем весь график
grid(True) # рисуем сетку
show() # выводим это все на экран