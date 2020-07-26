if __name__ == "__main__":
    print('--------- Pizzaría Bella Napoli ----------')
    
    print('Seleccione una opción de pizza \n')
    print('1) Pizza Vegetaria')
    print('2) Pizza no vegetariana')

    option = int(input('Ingrese una opción: '))

    if option == 1:
        print('Ingredientes vegetarianos: \n')
        print('1) Pimientos ')
        print('2) Tofu')
        print('3) Ambos')
        option = int(input('Ingredientes disponibles: '))

        if option == 1:
            option = 'Pimiento'
        elif option == 2:
            option = 'Tofu'
        elif option == 3:
            option = 'Pimiento y Tofu'
        else:
            print('Opción invalida')

        print('Pedido final: \n')
        print('1) Pizza vegetariana, mozzarella, tomate más {} \n'.format(option))

    elif option == 2:
        print('Ingredientes no vegetarianos: \n')
        print('1) Peperoni ')
        print('2) Jamón')
        print('3) Salmón')
        print('4) Todos ')
        option = int(input('Ingredientes disponibles: '))

        if option == 1:
            option = 'Peperoni'
        elif option == 2:
            option = 'Jamón'
        elif option == 3:
            option = 'Salmón'
        elif option == 4:
            option = 'Peperoni, Jamón y Salmón'
        else:
            print('Opción invalida')
        print('Pedido final: \n')
        print('1) Pizza no vegetariana con mozzarella, tomate más {} \n'.format(option))