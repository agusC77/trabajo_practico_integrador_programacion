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
        if texto_busqueda in nombre_normalizado:
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
