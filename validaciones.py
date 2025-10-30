def numero_positivo():
    numero = 0
    try:
        numero = float(input("Esperando ingreso: "))
    except ValueError:
        print("Error, el valor ingresado no puede contener:")
        print("- Letars")
        print("- Espacios")
        print("- Caracteres especiales")
        print("- Valores negativos")
        print("- El campo vacío")