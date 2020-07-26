if __name__ == "__main__":
    

    
    print('Nivel \t\t\t\t Puntuación \n')
    print('Inaceptable \t\t\t 0.0')
    print('Aceptable \t\t\t 0.4')
    print('Merito \t\t\t\t 0.6 más')

    bonus = 2400

    user_score = float(input('Ingrse la puntuación obtenida: '))

    if user_score == 0:
        print('Tu nivel es inaceptable | Bonificación obtenida {} €'.format(bonus * user_score))
    elif user_score == 0.4:
        print('Tu nivel es aceptable | Bonificación obtenida {} €'.format(bonus * user_score))
    elif user_score >= 0.6:
        print('Tu nivel es Merito | Bonificación obtenida {} €'.format(bonus * user_score))
    else:
        print('Puntuación invalida')