from validaciones import numero_positivo
import csv
# Funcion para crear un archivo que almacenara los paises con los que trabajaremos
def crear_archivo(pais):
    nombre_pais = ""
    poblacion = 0
    superficie = 0
    opcion = ""
    existe = False
    with open("informacion_pais.csv", "w") as archivo: #"informacion.csv" es el archivo que se va a generar desde 0
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre_pais", "continente","poblacion","superficie"]) # encabezado del archivo
        # EL usuario agregara todos los países que desee
        enunciado = True
        while enunciado == True:
            print(" Ingrese el nombre del país a agregar: ")
            nombre_pais = input("ingrese el nombre del pais: ").lower()
            # Verifica si el país que esta intentando ingresar existe, si no es asi se informa que el país no existe y se 
            # vuelve a pedir que ingreses un país
            for i in pais:
                existe = False
                lista = i.split(",")
                if lista[0] == nombre_pais:
                    print(f"Ingrese la población de {nombre_pais}:")
                    poblacion = numero_positivo()
                    poblacion = int(poblacion)
                    print(f"Ingrese la superficie de {nombre_pais}:")
                    superficie = numero_positivo()
                    escritor.writerow([nombre_pais + "," + lista[1] + "," + poblacion + "," + superficie])
                    existe = True
                    break

            if not existe:
                print(f"Error, el país {nombre_pais} no existe.")
                continue

            # El usuario indica si quiere agregar o no otro país (Falta "validar" que el usuario ingrese si o si 1 o 2)
            print()
            print("Elija la opción deseada:")
            print("1) Agregar país")
            print("2) Salir")
            opcion = input("Esperando elección: ")
            while opcion not in ["1","2"]:
                print("error, elija una de las siguientes opciones: ")
                print("1) Agregar país")
                print("2) Salir")
                opcion = input("ingrese la opcion deseada: ")
            print()
            if opcion == "1":
                enunciado == True
                continue

            elif opcion == "2":
                enunciado == False