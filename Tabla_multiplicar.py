'''Pide al usuario un número entero y muestra la tabla de multiplicar de ese número
del 1 al 10. El formato de salida debe ser claro, por ejemplo: 5 x 1 = 5.
• Conceptos aplicados: input(), int(), bucle for con range(), f-strings.'''

numero =int(input("Ingrese un numero:")) #el usuario debera digitar un  numero

print(f"\n Tabla de multiplicar: {numero}:\n")# realiza salto de linea y muestra la tabla

for i in range(1,11): #guarda un rango especifico que es del 1 al 11
    result = numero * i  #va multiplicando 1 al 10
    print(f"{numero} x {i} = {result}") # muestra la tabla de multiplicar del numero que digito mas el resultado