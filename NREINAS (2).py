# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 19:27:07 2017

@author: Administrator
"""




print "PROBLEMA DE LAS N - REINAS"
print "\n"
print "Introduce el numero de Reinas:\n"

n= input()
print "\n"
fila =0
reinas = [-1]
estado=0

for i in range (n-1):
    reinas =reinas+[-1]
    print reinas
    finalizo =False
    if fila<n:
        while ((reinas[fila])<n-1 and finalizo):
            reinas [fila] =reinas [fila]+1
            for j in range (fila):
                if ((reinas[j]==reinas[fila]) or (abs (fila-j) == abs (reinas[fila]-reinas[j]))):
                    finalizo = False
                else:
                    finalizo =True
    print (finalizo, reinas)  