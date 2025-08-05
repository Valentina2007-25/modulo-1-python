'''Desarrolla un programa que pida al usuario una frase. El programa debe contar
cuántas vocales y cuántas consonantes contiene la frase (sin contar espacios ni
símbolos) y mostrar los resultados.
• Conceptos aplicados: Variables (contadores), bucle for, condicional
if/else, método lower() de strings.'''

frase = input("Ingresa una frase: ")

# Inicializar contadores
vocales = 0
consonantes = 0


frase = frase.lower() # Convertir la frase a minúsculas para facilitar la comparación

for caracter in frase:# Recorrer cada carácter en la frase
    if caracter.isalpha():  # Solo procesar letras
        if caracter in "aeiou":
            vocales += 1
        else:
            consonantes += 1

print(f"Número de vocales: {vocales}")# Mostrar los resultados
print(f"Número de consonantes: {consonantes}")
