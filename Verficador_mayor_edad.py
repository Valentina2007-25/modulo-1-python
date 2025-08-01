'''Escribe un programa que solicite la edad del usuario y determine si es mayor de
edad o no. El programa debe mostrar un mensaje apropiado. Adicionalmente, si la
edad está entre 18 y 25 años, debe mostrar un mensaje indicando que es un "joven
adulto".
• Conceptos aplicados: int(), input(), operadores relacionales y lógicos,
condicionales (if, elif, else).'''

edad =int(input("ingrese su Edad: ")) #el usuario debe digitar una edad
if edad>=1 and edad<=18:
    print(f"eres menor de edad")
elif edad >= 18 and edad <= 25:
    print(f"eres un Joven adulto")
elif edad>=18:
    print(f"es mayor de edad")
elif edad<=0:
    print(f"{edad} no es una opcion valida")
