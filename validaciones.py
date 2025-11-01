def numero_positivo():
    try:
        numero = input("Esperando ingreso: ").strip()
        # El número ingresado se pasa a float para verificar que sea un número válido
        numero_aux = float(numero)
        return numero
    except ValueError:
        print("Error, el valor ingresado no puede contener:")
        print("- Letras")
        print("- Espacios")
        print("- Caracteres especiales")
        print("- Valores negativos")
        print("- El campo vacío")

#==============================================================================================================================

def validar_texto():
    while True:
        try:
            texto = input("esperando texto: ").lower().strip()
            if not texto:
                print("error, el campo no puede estar vacio")
                continue
            if all(letra.isalpha() or letra == " " for letra in texto):
                return texto
            else:
                raise ValueError
            
        except ValueError:
            print("el nombre ingresado no puede tener: ")
            print("-caracteres especiales")
            print("-numeros")
            print("-el campo vacio")

#==============================================================================================================================

def verificar_pais_archivo(pais_ingresado):
    import csv
    ya_ingresado = False  # Se inicializa antes del bucle
    
    with open("informacion_pais.csv", "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        datos = list(lector)
    
    for fila in datos:
        if fila["País"] == pais_ingresado:
            ya_ingresado = True
            break 
    
    return ya_ingresado
