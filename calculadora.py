#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

functions = ['sum','rest','mult','div']

if len(sys.argv) != 4:
    sys.exit("Numero de argumentos incorrecto")

try:
    int(sys.argv[2])
    float(sys.argv[3])
except ValueError:
    print "Error:necesito numeros"
    exit()

def suma(op1,op2):
    return op1 + op2
def resta(op1,op2):
    return op1-op2
def multiplicacion(op1,op2):
    return op1*op2
def division(op1,op2):
    try:
        return(op1/op2)
    except ZeroDivisionError:
        print("no podemos dividir entre 0")
        exit()

if sys.argv[1] == functions[0]:
    print suma(float(sys.argv[2]) , float(sys.argv[3]))
elif sys.argv[1] == functions[1]:
    print resta(float(sys.argv[2]) , float(sys.argv[3]))
elif sys.argv[1] == functions[2]:
    print multiplicacion(float(sys.argv[2]) , float(sys.argv[3]))
elif sys.argv[1] == functions[3]:
    print dividision(float(sys.argv[2]) , float(sys.argv[3]))
else:
    print ("acabe")
