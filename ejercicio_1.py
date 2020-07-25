""" Enunciado Ejercicio 1 """

#Escribir un programa que pregunte al usuario su edad y muestrre por pantalla si es mayor de edad o no

print('------------------------ Bienvenido ------------------------')
user_age = int(input('Ingrese su edad: '))

if user_age >= 18:
    print('Es mayor de edad')
else:
    print('No es mayor de edad')