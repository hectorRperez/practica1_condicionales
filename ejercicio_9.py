if __name__ == "__main__":
    
    user_age = int(input('Ingrese su edad: '))

    if user_age < 4:
        print('El total a pagar es: 0€')
    elif user_age >= 4 and user_age < 18:
        print('El total a pagar es: 5€')
    elif user_age >= 18:
        print('El total a pagar es: 10€')