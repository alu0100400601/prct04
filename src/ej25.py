#!/usr/bin/python
#!encoding: UTF-8

from math import sqrt

a= float(raw_input('valor de a: '))
b= float(raw_input('valor de b: '))
c= float(raw_input('valor de c: '))

if(a==0):
  if(b==0):
    if(c==0):
      print 'la ecuacion tiene infinitas soluciones.'
    else:
      print 'la ecuacion no tiene solucion.'
  else:
    x=-c/b
    print 'la solucion de la ecuacion es: x=%4.3f' % x
else:
  x1= (-b + sqrt(b**2 - (4*a*c))) / (2*a)
  x2= (-b - sqrt(b**2 - (4*a*c))) / (2*a)
  print 'las soluciones de la ecuacion son: x1=%4.3f y x2=%4.3f' % (x1,x2)
