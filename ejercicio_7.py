
if __name__ == "__main__":
    
    print('Renta \t\t\t\t\t Tipo de impositivo \n')
    print('Menos de 10000€ \t\t\t\t 5%')
    print('Entre de 10000€ y 20000€ \t\t\t 15%')
    print('Menos de 20000€ y 35000€ \t\t\t 20%')
    print('Menos de 35000€ y 60000€ \t\t\t 30%')
    print('Más de 60000€ \t\t\t\t\t 45%')

    rent = float(input('Ingrese su renta anual: '))

    if rent < 10000:
        print('Tipo de impositivo es 5% ')
    elif rent > 10000 and rent < 20000:
        print('Tipo de impositivo es 15% ')
    elif rent > 20000 and rent< 35000:
        print('Tipo de impositivo es 20% ')
    elif rent > 35000 and rent < 60000:
        print('Tipo de impositivo es 30% ')
    elif rent > 60000:
        print('Tipo de impositivo es 45% ')    

