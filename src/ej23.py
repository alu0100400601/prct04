#!/usr/bin/python
#!encoding: UTF-8

a= float(raw_input('valor de a: '))
b= float(raw_input('valor de b: '))
if(a!=0):
  x=-b/a
  print 'solucion: ', x
if(a==0):
  if(b!=0):
    print 'la ecuacion no tiene solucion.'
  else:
    print 'la ecuacion tiene infinitas soluciones.'