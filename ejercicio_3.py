""" Enunciado Ejercicio 3 """

# Escribir un programa que pida al usuario dos números y 
# muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error 

n1 = float(input('Ingrese el 1° número: '))
n2 = float(input('Ingrese el 2° número: '))

if n2 == 0:
    raise 'No se puede dividir por 0.'
else:
    print('La division es {} '.format(n1/n2))