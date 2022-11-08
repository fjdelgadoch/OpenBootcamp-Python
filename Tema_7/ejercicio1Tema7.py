from operacionesBasicas import *

print("\nOPERACIONES MATEMÁTICAS BÁSICAS\n")

op1 = float(input("Introduce el primer número: "))
op2 = float(input("Introduce el segundo número: "))
oper = input("Indique la operación ha realizar: ")

suma = sumar(op1, op2)
resta = restar(op1,op2)
multiplica = multiplicar(op1,op2)
divide = dividir(op1,op2)
resto = restoDivision(op1,op2)

if oper == "suma":
    print(f"\nSUMA: {op1} + {op2} = {suma}")

elif oper == "resta":   
    print(f"\nRESTA: {op1} - {op2} = {resta}")

elif oper == "multiplica":
    print(f"\nMULTIPLICACIÓN: {op1} * {op2} = {multiplica}")

elif oper == "divide":
    print(f"\nDIVISIÓN: {op1} / {op2} = {divide} RESTO: {resto}")

elif oper == "todas":
    print(f"\nSUMA: {op1} + {op2} = {suma}")
    print(f"\nRESTA: {op1} - {op2} = {resta}")
    print(f"\nMULTIPLICACIÓN: {op1} * {op2} = {multiplica}")
    print(f"\nDIVISIÓN: {op1} / {op2} = {divide} RESTO: {resto}")

else:
    print("\nLa operación introducida no es correcta.")