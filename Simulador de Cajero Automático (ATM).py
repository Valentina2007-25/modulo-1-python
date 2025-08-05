'''Crea un programa que simule las operaciones de un cajero automático. El
programa debe gestionar un saldo inicial.
• Debe encapsular la lógica en funciones como consultar_saldo(),
depositar(), retirar().
• Utiliza un bucle while para mantener el programa en ejecución hasta que el
usuario decida salir.
• Valida las operaciones (ej. no se puede retirar más dinero del que hay en el
saldo).
• El código debe ser claro, legible y seguir las recomendaciones de PEP 8.
• Conceptos integrados: Funciones, bucle while, condicionales, variables,
operadores, I/O, PEP 8.'''

# Saldo inicial
saldo = 1000.0

def consultar_saldo():
    """Muestra el saldo actual del usuario."""
    print(f"\nTu saldo actual es: ${saldo:.2f}")

def depositar():
    """Pide un monto, verifica que sea válido y lo suma al saldo."""
    global saldo
    try:
        monto = float(input("Ingresa la cantidad a depositar: "))
        if monto > 0:
            saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
        else:
            print("El monto debe ser mayor que cero.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def retirar():
    """Pide un monto, verifica si hay saldo suficiente y lo descuenta."""
    global saldo
    try:
        monto = float(input("Ingresa la cantidad a retirar: "))
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
        elif monto > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def mostrar_menu():
    """Muestra las opciones del cajero."""
    print("\n--- Cajero Automático ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

# Bucle principal del cajero
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        consultar_saldo()
    elif opcion == "2":
        depositar()
    elif opcion == "3":
        retirar()
    elif opcion == "4":
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")
