""" Enunciado Ejercicio 2 """

#Escribir un programa que almacene la cadena de
# caracteres *contraseña* en una variable, 
# pregunte al usuario por la contraseña e 
# imprima por pantalla si la contraseña introducida
# por el usuario coidicen con la guardada en la variable
# sin tener en cuenta mayúsculas y minúsculas


from getpass import getpass

key = 'contraseña'
password = getpass('Introduce la contraseña: ')

if key == password:
    print('Las contraseñas coinciden')
else:
    print('Las contraseñas no coiciden')

