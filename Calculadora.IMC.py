'''Crea un programa que pida al usuario su peso (en kg) y su altura (en metros).
Calcula el IMC usando la fórmula:
IMC=altura2
     peso
y muestre el resultado con un mensaje claro y formateado, redondeado a dos
decimales.
• Conceptos aplicados: input(), print(), float(), variables, operadores
aritméticos, f-strings.'''


peso=(float(input("Ingrese su peso: "))) #guarda el peso digitado por el usuario
print(f"su peso es: {peso}kg") #imprime el peso digitado por el usuario

altura=(float(input("Ingrese su altura: "))) #guarda la altura digitada por el usuario
print(f"su altura es: {altura}m") #muestra la altura digitada por el usuario

IMC=(peso/altura) #guarda la operacion de IMC en el IMC
print(f"su IMC es: {IMC:.2f}") #imprime el resultado de IMC y mostrando solamente 2 decimales


