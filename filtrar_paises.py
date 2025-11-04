import csv
from validaciones import validar_texto
from ver_informacion_paises import eliminar_acentos 

#================================================================================================================================

# Función para mostrar los países de un continente específico
def paises_continente():
    # Variable que almacenara los continentes
    continentes = ["america", "asia", "africa", "europa", "oceania"]
    # Variable para que el usuario elija un continente
    continente_elejido = ""
    # Variable para verificar que el continente que ingreso el usuario existe
    existe = False

    while True:
        print("Ingrese el nombre de un continente para, mostrar solo los países de ese continente:")
        continente_elejido = validar_texto()
        continente_elejido = eliminar_acentos(continente_elejido)

        # Verifica que el usuario haya ingresado un continente exixtesnte
        for continente in continentes:
            continente == continente_elejido
            existe = True
            break

        if existe:
            break
        else:
            print(f"{continente_elejido} no es un continente.")
            print()

    with open("informacion_pais.csv", "r", encoding= "utf-8", newline= "") as archivo:
        diccionario = csv.DictReader(archivo)
        lista = list(diccionario)

    # Este mtch es para mostrar correctamente el nombre de los continentes debido a que le quitamos los acentos 
    # para que el programa siga funcionando a pesar de que no se ingrese  sin acentos
    match continente_elejido:
        case "america":
            print(f"Países de América: ")
        case "asia":
            print(f"Países de Asia: ")
        case "africa":
            print(f"Países de África: ")
        case "oceania":
            print(f"Países de Oceanía: ")
    
    for linea in lista:
        if linea["Continente"] == continente_elejido:
            print(f"- {linea["País"].title()}")

#================================================================================================================================