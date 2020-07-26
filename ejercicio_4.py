""" Enunciado Ejercicio 4 """

# Escribir un programa que pida al usuario un número entero y muestre por # pantalla si es par o impar

n = int(input('Ingrese un número: '))

if n % 2 == 0:
    print(' {} es par '.format(n))
else:
    print('{} es impar '.format(n))    