""" Enunciado Ejercicio 5 """ 

""" Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no. """

if __name__ == "__main__":
    
    user_age = int(input('Ingrese su edad: '))
    monthly_income = float(input('Cuanto es sus ingreso: '))

    if user_age >= 16 and monthly_income >= 1000:
        print('Debes pagar impuestos!!')
    else:
        print('Aún no cumples los requisitos')