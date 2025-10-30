from validaciones import numero_positivo

# Funcipon para crear un archivo que almacenara los paises con los que trabajaremos
def crear_archivo(pais, continente):
    nombre_pais = ""
    poblacion = 0
    superficie = 0
    opcion = ""
    with open("informacion_pais.txt", "a") as contenido:
        # EL usuario agregara todos los países que desee
        while True:
            print(" Ingrese el nombre del país a agregar: ")
            nombre_pais = input("Esperando nombre: ").lowwer()
            # Verifica si el país que esta intentando ingresar existe, si no es asi se informa que el país no existe y se 
            # vuelve a pedir que ingreses un país
            if nombre_pais in pais:
                print(" Ingrese la población del pais: ")
                poblacion = numero_positivo()
                print(" Ingrese la superficie del país: ")
                superficie = numero_positivo() 
                # Falta agregar continente
                contenido.write(nombre_pais + "," + poblacion + "," + superficie)
            else:
                print(f"Error, el país {nombre_pais} no existe.")
                print()
                continue
            # El usuario indica si quiere agregar o no otro país (Falta "validar" que el usuario ingrese si o si 1 o 2)
            print()
            print("Elija la opción deseada:")
            print("1) Agregar país")
            print("2) Salir")
            opcion = input("Esperando elección: ")
            print()
            if opcion == "2":
                break