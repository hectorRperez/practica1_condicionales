# Practica de Ejercicios de Python 

## Ejercicio 1 
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

___

## Ejercicio 2

Escribir un programa que almacene la cadena de
caracteres *contraseña* en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coidicen con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas

Utilizo el modulo 

~~~
from getpass import getpass
~~~

Para ocultar la contraseña ingresada por la terminal

___

## Ejercicio 3

Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error 

___

## Ejercicio 4

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar 

___

## Ejercicio 5

Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

___

## Ejercicio 6

Los alumnos de un curso se han divido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M  y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde


___
## Ejercicio 7 

Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

![Impuestos en los paises ejemplo](./impuestos.png)

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde

___
## Ejercicio 8

En una determinada empresa, sus empleados son evaluados al fina de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejor beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero en valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los nivles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel


![Ejercicio 8 tabla de puntuación](./ejercicio_8.png)

Escrbir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario

___
## Ejercicio 9 

Escribit un programa para una empresa que tiene salas de juego para todas las edades y quiere calcular de forma automatica el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y moestrar el precio de la entrada. Si el clinte es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€

___
## Ejercicio 10

La pizzeria Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparece a continuación 

- ingredientes vegetarianos: Pimiento y tofu
- ingredientes no vegetarianos: Peperoni, Jamón y Salmón

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todo los ingredientes que lleva

