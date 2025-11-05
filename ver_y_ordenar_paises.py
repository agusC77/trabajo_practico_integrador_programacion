import csv
from validaciones import *

# ===========================================================================================================================
# esta funcion sirve para eliminar los acentos de las palabras
def eliminar_acentos(texto):
    acentos = {
        "á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u",
        "Á":"A", "É":"E", "Í":"I", "Ó":"O", "Ú":"U"
    }
    texto_sin = ""
    for letra in texto:
        if letra in acentos:
            texto_sin += acentos[letra]
        else:
            texto_sin += letra
    return texto_sin

# ===========================================================================================================================

# Esta funcion sirve para que cuando se seleccione la opcion numero 2 se ejecute el codigo lo siguiente:
def ver_informacion_pais(texto_busqueda): # la funcion recibe el pais al cual, le buscara la informacion
    with open("informacion_pais.csv", "r", encoding="utf-8", newline="") as archivo: #abre el archivo para leerlo
        lineas = archivo.readlines()
    # separamos el encabezado del archivo de la lista de paises
    encabezado = lineas[0].strip().split(",")
    paises = [linea.strip().split(",") for linea in lineas[1:]]

    # elimina los acentos del pais que estamos buscando
    texto_busqueda = eliminar_acentos(texto_busqueda.lower().strip())

    # Busca los paises de la lista que coincidan con el texto ingresado por el usuario
    coincidencias = []
    for pais in paises:
        nombre_normalizado = eliminar_acentos(pais[0].lower())
        if nombre_normalizado.startswith(texto_busqueda):
            coincidencias.append(pais)

    if not coincidencias:
        print("No hay países que coincidan con la búsqueda.")
        return
    #si se encuentran coincidencias, se le avisa al usuario cuantas hay
    print(f"\nSe encontraron {len(coincidencias)} coincidencia(s) en el archivo:")
    for i in range(len(coincidencias)):
        print(f"{i+1}) {coincidencias[i][0]}")

    # elegir el pais dependiendo de la cantidad de coincidencias
    if len(coincidencias) > 1:
        while True:
            eleccion = input("\nSeleccione el número del país que desea ver: ")
            if eleccion.isdigit() and 1 <= int(eleccion) <= len(coincidencias):
                pais_elegido = coincidencias[int(eleccion)-1]
                break
            else:
                print("Error: número inválido.")
    else:
        pais_elegido = coincidencias[0] #si solo hay una coincidencia se la asigna a la variable sin tener que elegir 

    # Mostrar información del país elegido
    print("\nInformación del país seleccionado:")
    for i in range(len(encabezado)):
        print(f"{encabezado[i]}: {pais_elegido[i]}")

# ===========================================================================================================================

#esta funcion permite ordenar los paises segun su continente alfabeticamente
def mostrar_paises_ordenados_alfabeticamente():
    print("Mostrando países en orden alfabético...\n")

    with open("informacion_pais.csv", "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)  # convierte el lector en una lista de diccionarios

    # Función que devuelve el campo por el que queremos ordenar
    def obtener_pais(fila):
        return fila["País"].lower()  # usa la tilde exacta del encabezado

    # Ordenar las filas por el nombre del país
    filas.sort(key=obtener_pais)

    # Muestra los países ordenados alfabeticamente
    for pais in filas:
        print(f"{pais['País']} - {pais['Continente']} - poblacion: {pais['Población']} - superficie: {pais['Superficie']}")

    print("\n✅ Fin de la lista ordenada.")

# ===========================================================================================================================

#esta funcion permite ordenar los paises segun su poblacion de menor a mayor o viceversa

def ordenar_segun_poblacion(opcion_elegida):
    with open("informacion_pais.csv", "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)
    def obtener_poblacion(fila):
        return int(fila["Población"])
    
    match opcion_elegida:
        case "1":
            filas.sort(key=obtener_poblacion)
            print("\n los paises ordenados segun su poblacion de menor a mayor:\n")
        case "2":
            filas.sort(key=obtener_poblacion, reverse=True)
            print("\n los paises ordenados segun su poblacion de mayor a menor:\n")
    for pais in filas:
        print(f"{pais['País']} - {pais['Continente']} - poblacion: {pais['Población']} - superficie: {pais['Superficie']}")

# ===========================================================================================================================

#esta funcion permite ordenar los paises segun su superficie de menor a mayor o viceversa

def ordenar_segun_superficie(opcion_elegida):
    with open("informacion_pais.csv", "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)
    def obtener_superficie(fila):
        return int(fila["Superficie"])
    
    match opcion_elegida:
        case "1":
            filas.sort(key=obtener_superficie)
            print("\n los paises ordenados segun su superficie de menor a mayor:\n")
        case "2":
            filas.sort(key=obtener_superficie, reverse=True)
            print("\n los paises ordenados segun su superficie de mayor a menor:\n")
    for pais in filas:
        print(f"{pais['País']} - {pais['Continente']} - poblacion: {pais['Población']} - superficie: {pais['Superficie']}")

# ===========================================================================================================================

#esta funcion sirve para ver unicamente las estadisticas de un pais elegido
def ver_estadisticas(pais_elegido):
    existe = False
    with open("informacion_pais.csv", "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)
    for pais in filas:
        if pais["País"].lower() == pais_elegido:
            print(f"----------{pais_elegido}-----------")
            print(f"poblacion: {pais['Población']}")
            print(f"superficie: {pais["Superficie"]}")
            existe = True
            break
    if not existe:
        print(f"el pais {pais_elegido} no existe, no esta ingresado en el archivo o esta mal escrito su nombre")