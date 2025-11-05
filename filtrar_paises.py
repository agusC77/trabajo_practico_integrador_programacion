import csv
from validaciones import validar_texto
from ver_y_ordenar_paises import eliminar_acentos 

#================================================================================================================================

# Función para mostrar los países de un continente específico
def paises_continente():
    # Variable que almacenara los continentes
    continentes = ["america", "asia", "africa", "europa", "oceania"]
    # Variable para que el usuario elija un continente
    continente_elegido = ""
    # Variable para verificar que el continente que ingreso el usuario existe
    existe = False

    while True:
        print(" Ingrese el nombre de un continente para, mostrar solo los países de ese continente:")
        continente_elegido = validar_texto()
        continente_elegido = eliminar_acentos(continente_elegido)
        # Verifica que el usuario haya ingresado un continente exixtesnte
        for continente in continentes:
            if continente == continente_elegido:
                existe = True
                break
        if existe:
            break
        else:
            print(f"{continente_elegido} no es un continente.")
            print()

    with open("informacion_pais.csv", "r", encoding= "utf-8", newline= "") as archivo:
        diccionario = csv.DictReader(archivo)
        lista = list(diccionario)

    # Este match es para mostrar correctamente el nombre de los continentes debido a que le quitamos los acentos 
    # para que el programa siga funcionando a pesar de que no se ingrese  sin acentos
    match continente_elegido:
        case "america":
            print(f" Países de América: ")
        case "asia":
            print(f" Países de Asia: ")
        case "africa":
            print(f" Países de África: ")
        case "oceania":
            print(f" Países de Oceanía: ")
    
    for linea in lista:
        if linea["Continente"] == continente_elegido:
            print(f"- {linea["País"].title()}")

#================================================================================================================================

def paises_poblacion():
    # Variables para calcular el promedio de población
    promedio_poblacion = 0
    suma_poblacion = 0
    cantidad_paises = 0
    # Variables para almacenar los países
    poblacion_alta = []
    poblacion_media = []
    poblacion_baja = []
    # Variables para verificar y para que el usuario elija una opcion
    opcion = ""
    validar_poblacion_alta = 0
    validar_poblacion_media = 0
    validar_poblacion_baja = 0

    # Genera una lista de diccionario, cada diccionario es un país
    with open("informacion_pais.csv", "r", encoding= "utf-8", newline= "")as archivo:
        diccionario = csv.DictReader(archivo)
        lista = list(diccionario)

    # Calcula el promedio de población en el mundo
    for linea in lista:
        suma_poblacion += int(linea["Población"]) 
        cantidad_paises += 1
    promedio_poblacion = int(suma_poblacion / cantidad_paises) 

    # Agrupa a los países por mucha, media o poca población teniendo en cuenta el promedio de población del mundo
    for pais in lista:
        if int(pais["Población"]) > promedio_poblacion:
            poblacion_alta.append(pais["País"])
            validar_poblacion_alta += 1
        elif int(pais["Población"]) == promedio_poblacion:
            poblacion_media.append(pais["País"])
            validar_poblacion_media += 1
        elif int(pais["Población"]) < promedio_poblacion:
            poblacion_baja.append(pais["País"])
            validar_poblacion_baja += 1

    # El usuario elije si quiere ver
    while True: 
        print(" Elija la opcón deseada:")
        print(" 1) Ver paises con población promedio")
        print(" 2) Ver paises con población por encima del promedio")
        print(" 3) Ver paises con población por debajo del promedio")
        opcion = input(" Esperando elección: ")
        if not opcion in ["1","2", "3"]:
            print(" Error, valor inválido debes elegir entre la opción 1, 2 y 3")
            print()
        else:
            print()
            break

    # Se muestra por pantalla los paises
    match opcion:
        case "1":
            if validar_poblacion_media > 0:
                print(" Países con una población igual al promedio: ")
                for pais in poblacion_media:
                    print(f"- {pais.title()}")
            else:
                print(" No hay países con una población igual al promedio")
            
        case "2":
            if validar_poblacion_alta > 0:
                print(" Países con una población por encima del promedio: ")
                for pais in poblacion_alta:
                    print(f"- {pais.title()}")
            else:
                print(" No hay paises con una población por encima del promedio")
            
        case "3":
            if validar_poblacion_baja > 0:
                print(" Países con una población por debajo del promedio: ")
                for pais in poblacion_baja:
                    print(f"- {pais.title()}")
            else:
                print(" No hay paises con una población por denajo del promedio")
    print()

#================================================================================================================================

def paises_superficie():
    # Variables para calcular el promedio de la superficie de los países del mundo
    promedio_superficie = 0
    suma_superficie = 0
    cantidad_paises = 0
    # Variables para almacenar los países
    superficie_alta = []
    superficie_media = []
    superficie_baja = []
    # Variables para verificar y para que el usuario elija una opcion
    opcion = ""
    validar_superficie_alta = 0
    validar_superficie_media = 0
    validar_superficie_baja = 0

    with open("informacion_pais.csv", "r", encoding= "utf-8", newline= "") as archivo:
        diccionario = csv.DictReader(archivo)
        lista = list(diccionario)

    # Calcula el promedio de la superficie de los países del mundo
    for pais in lista:
        suma_superficie += int(pais["Superficie"]) 
        cantidad_paises += 1
    promedio_superficie = int(suma_superficie / cantidad_paises)

    # Define que país tiene una superficie por encima del promedio, cuales tienen menor que el promedio y cuales tienen una 
    # superficie igual al promedio
    for pais in lista:
        if int(pais["Superficie"]) > promedio_superficie:
            superficie_alta.append(pais["País"])
            validar_superficie_alta += 1
        elif int(pais["Superficie"]) == promedio_superficie:
            superficie_media.append(pais["País"])
            validar_superficie_media += 1
        elif int(pais["Superficie"]) < promedio_superficie:
            superficie_baja.append(pais["País"])
            validar_superficie_baja += 1

    # El usuario elije si quiere ver
    while True: 
        print(" Desea ver paises con:")
        print(" 1) Superficie igual al promedio")
        print(" 2) Superficie por encima del promedio")
        print(" 3) Superficie por debajo del promedio")
        opcion = input(" Esperando elección: ")
        if not opcion in ["1","2", "3"]:
            print(" Error, valor inválido debes elegir entre la opción 1, 2 y 3")
            print()
        else:
            print()
            break

    # Se muestra por pantalla los paises
    match opcion:
        case "1":
            if validar_superficie_media > 0:
                print(" Países con una superficie igual al promedio: ")
                for pais in superficie_media:
                    print(f"- {pais.title()}")
            else:
                print(" No hay países con una superficie igual al promedio")
            
        case "2":
            if validar_superficie_alta > 0:
                print(" Países con una superficie por encima del promedio: ")
                for pais in superficie_alta:
                    print(f"- {pais.title()}")
            else:
                print(" No hay paises con una superficie por encima del promedio")
            
        case "3":
            if validar_superficie_baja > 0:
                print(" Países con una superficie por debajo del promedio: ")
                for pais in superficie_baja:
                    print(f"- {pais.title()}")
            else:
                print(" No hay paises con una superficie por denajo del promedio")
    print()