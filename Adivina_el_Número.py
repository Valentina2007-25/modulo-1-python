'''Crea un juego donde el programa "piensa" un número secreto entre 1 y 100
(puedes definirlo estáticamente, por ejemplo, numero_secreto = 42). El usuario
debe adivinarlo. En cada intento, el programa le dirá si el número ingresado es
mayor o menor que el número secreto. El juego termina cuando el usuario adivina
el número.
• Conceptos aplicados: Bucle while, if/elif/else, input(), int(), operadores
relacionales.'''

print("Adivina el número entre 1 y 100") #muestra un mensaje

num_secreto = 42 #se guarda el numero secreto que escogi
numero = int(input("Ingresa un número: ")) # pide al usuario digitar un numero

while numero < 1 or numero > 100: #se establece un limite que se debe escoger entre esos numeros
    print(f"el numero debe estar entre 1 y 100") #muestra un mesnaje indicando en que rango debe esocger los numeros
    numero = int(input("sigue intentando")) #si no adivina el numero entonces mostrara este mensaje para vovler a intentatarlo

while numero != num_secreto:  #si el numero es dirente e igual al numero secreto
    if numero < num_secreto:  #si el numero es menor que el numero secreto mostrara que el numero secreto es mayor
        print("El número secreto es mayor.")
    elif numero > num_secreto:   #si el numero es mayor que el numero secreto mostrara que el numero secreto es menor
        print("El número secreto es menor.")
    numero = int(input("Sigue intentando: "))

 # si se digita el numero secreto e ntonces mostrara el siguiente mensaje
print(f"{numero} es el número secreto, muy bien")


