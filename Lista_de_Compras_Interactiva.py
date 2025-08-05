'''Desarrolla un programa que permita al usuario gestionar una lista de compras. El
programa debe usar un bucle while para mostrar un menú con opciones:
1. Agregar ítem a la lista.
2. Eliminar ítem de la lista.
3. Ver la lista completa.
4. Salir. El programa debe gestionar la lista de compras y seguir las
instrucciones del usuario.
• Conceptos aplicados: Listas (métodos append, remove), bucle while,
if/elif/else, input().'''
from operator import itemgetter

lista_compras = []
while True:
    print("\nMenú:")
    print("1. Agregar ítem a las lista")
    print("2. Eliminar ítem de la lista")
    print("3. Ver lista completa")
    print("4. Salir")

    Opcion = input("seleccione una opcion:")

    if Opcion == "1":
        item = input("ingresa una lista:")
        lista_compras.append(item)
        print(f"{item}\nlista agregada")

    elif Opcion == "2":
        item = input("ingresa una lista para eliminar:")
        if item in lista_compras:
           lista_compras.remove(item)
           print(f"{item}lista eliminada")
        else:
            print(f"{item}la lista no existe.")

    elif Opcion == "3":
      print("lista de compras:")
      for i, item in enumerate(lista_compras, start = 1,):
       print(f"{i}. {item}")


    elif Opcion == "4":
      print("programa terminado.")
      break
else:
    print("Opcion no valida")

