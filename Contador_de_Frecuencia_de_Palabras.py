'''Crea una función que reciba un texto (string) y devuelva un diccionario con la
frecuencia de cada palabra. El diccionario tendrá las palabras como claves y su
conteo como valor. No debe distinguir entre mayúsculas y minúsculas.
• Conceptos aplicados: Diccionarios (método get), funciones, strings
(métodos split, lower), bucle for. '''

def contar_frecuencia_palabras(texto):
    # Primero convertimos todo el texto a minúsculas para que no haya diferencia entre "Hola" y "hola"
    texto = texto.lower()

    # Luego dividimos el texto en palabras usando el método split(), que separa por espacios
    palabras = texto.split()

    # Creamos un diccionario vacío donde guardaremos la frecuencia de cada palabra
    frecuencia = {}

    # Recorremos cada palabra en la lista
    for palabra in palabras:
        # Usamos el método get() para obtener el valor actual de la palabra.
        # Si la palabra no existe en el diccionario, get() devuelve 0 y sumamos 1.
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    # Al final devolvemos el diccionario con los conteos
    return frecuencia

# Ejemplo de uso
texto_usuario = "Hola hola mundo mundo mundo"
resultado = contar_frecuencia_palabras(texto_usuario)
print(resultado)
