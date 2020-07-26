""" Enunciado Ejercicio 6 """

""" Los alumnos de un curso se han divido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M  y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde """

if __name__ == "__main__":
    
    grupo_a = []
    grupo_b = []

    gender = input('Ingrese su sexo (M/F): ')
    name = input('Ingrese su nombre: ')

    if gender.upper() == 'F':
        if name.lower() < 'm':
            grupo_a.append(name)
            print('El estudiante fue asignado al grupo A')
        else:
            grupo_b.append(name)
            print('El estudiante fue asignado al grupo B')
    
    elif gender.upper() == 'M':
        if name.lower() > 'n':
            grupo_a.append(name)
            print('El estudiante fue asignado al grupo A')
        else:
            grupo_b.append(name)
            print('El estudiante fue asignado al grupo B')
    else:
        print('Se ingreso una opción invalida')