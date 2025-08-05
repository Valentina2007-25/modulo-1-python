'''Escribe una función que reciba una palabra o frase y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda),
ignorando espacios y mayúsculas/minúsculas. La función debe retornar True o
False.
• Conceptos aplicados: Funciones, strings (métodos replace, lower), slicing
([::-1]), booleanos.'''

def es_palindromo(texto):

    texto = texto.lower().replace(" ", "") # Convertimos a minusculas quitando los espacios
    return texto == texto[::-1] # Comparamos el texto con su versión invertida

palabra = input("Ingresa una palabra o frase: ")  # Pedimos al usuario una palabra o frase

if es_palindromo(palabra):    # Usamos la función y mostramos el resultado
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
