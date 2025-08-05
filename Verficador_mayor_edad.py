'''Escribe un programa que solicite la edad del usuario y determine si es mayor de
edad o no. El programa debe mostrar un mensaje apropiado. Adicionalmente, si la
edad está entre 18 y 25 años, debe mostrar un mensaje indicando que es un "joven
adulto".
• Conceptos aplicados: int(), input(), operadores relacionales y lógicos,
condicionales (if, elif, else).'''

edad =int(input("ingrese su Edad: ")) #el usuario debe digitar una edad
if edad>=1 and edad<=18: # realiza la condicion si es menor de edad
    print(f"eres menor de edad")
elif edad >= 18 and edad <= 25: #muestra un mensaje indicando que es un "joven adulto" si la edad esta entre 18 y 25.
    print(f"eres un Joven adulto")
elif edad>=18:   #si es mayor de 18, muestra un mensaje de mayor de edad
    print(f"es mayor de edad")
elif edad<=0:  # si la edad es menor o igual que 0 mostrara un mensaje de opcion invalida
    print(f"{edad} no es una opcion invalida")
