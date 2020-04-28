def ID_CODIGO():
    while True:
        codigo = input("Codigo: ")
        if codigo == "":
            print("No puede dejar vacio.")
        else:
            return codigo

def ID_NOMBRE():
    while True:
        nombre = input("Nombre del Cliente: ")
        if nombre == "":
            print("Debe ingresar un nombre.")
        else:
            return nombre

def INGRESAR_DIRECCION():
    while True:
        direccion = input("Direccion: ")
        if direccion == "":
            print("Debe ingresar una direccion.")
        else:
            return direccion

def INGRESAR_TELEFONO():
    while True:
        telefono = input("Telefono: ")
        if telefono == "":
            print("Debe ingresar un No. de Telefono.")
        else:
            return telefono

def ImprimirClientes():
    if len(clientes) == 0:
        print("Esta Vacia.")
    else:
        clientes.sort()
        print("\n".join(i[0] + " - " + str(i[1])+ " - " +str(i[2]) + " - " + str(i[3])  for i in clientes))

def IdCodigoProyecto():
    while True:
        codigopro = input("Codigo del Proyecto: ")
        if codigopro == "":
            print("No puede dejar vacio.")
        else:
            return codigopro

def INGRESAR_DESCRIPCION():
    while True:
        nombreppr = input("Nombre del Proyecto: ")
        if nombreppr == "":
            print("Debe ingresar un nombre de Proyecto ")
        else:
            return nombreppr

def INGRESAR_ESTADO():
    while True:
        estado = input("Estado del Proyecto: ")
        if estado == "":
            print("Debe ingresar un estado del proyecto.")
        else:
            return estado

def ID_CODIGO_CLIENTE():
    while True:
        codigo = input("Codigo del Cliente: ")
        if codigo == "":
            print("No puede dejar vacio.")
        else:
            return codigo

def ImprimirProyectos():
    if len(proyectos) == 0:
        print("La lista esta Vacia.")
    else:
        proyectos.sort()
        print("\n".join(i[0] + " - " + str(i[1])+ " - " +str(i[2]) + " - " +str(i[3]) for i in proyectos))

def idRegion():
    while True:
        codigoreg = input("Codigo de Region: ")
        if codigoreg == "":
            print("No puede dejar vacio.")
        else:
            return codigoreg

def INGRESAR_MUNICIPIO():
    while True:
        nombremun = input("Nombre del Municipio: ")
        if nombremun == "":
            print("Debe ingresar un nombre de Municipio ")
        else:
            return nombremun

def INGRESAR_DEPARTAMENTO():
    while True:
        codigodep = input("Nombre del Departamento: ")
        if codigodep == "":
            print("Debe ingresar un Nombre de Departamento.")
        else:
            return codigodep

def ImprimirRegion():
    if len(regiones) == 0:
        print("La lista esta Vacia.")
    else:
        regiones.sort()
        print("\n".join(i[0] + " - " + str(i[1])+ " - " +str(i[2]) for i in regiones))

def PantallaRegionProyecto():
    if len(proyectos) == 0:
        print("La lista esta Vacia.")
    else:
        proyectos.sort()
        print("\n".join(i[0] + " - " + str(i[1])+ " - " +str(i[2])for i in proyectos)
        + " - "+"\n".join(i[0] + " - " + str(i[1])+ " - " +str(i[2])for i in clientes))

def borrarCliente():
    if len(clientes) == 0:
        print("No se ha ingresado ningun cliente.")
    else:
        codigo = ID_CODIGO()
        indice = buscarCliente(codigo)
        if indice == -1:
            print("No se ha encontrado el cliente '{}'".format(codigo))
            return False
        print("Se ha eliminado el cliente '{}' con nombre {}".format(codigo, clientes[indice][1]))
        del clientes[indice]
        return True

def buscarCliente(nombre):
    for i, e in enumerate(clientes):
        if e[0] == nombre:
            return i
    return -1


def borrarProyecto():

    if len(proyectos) == 0:
        print("No se ha ingresado ningun Proyecto ")
    else:
        codigo = IdCodigoProyecto()
        indice = buscarProyecto(codigo)
        if indice == -1:
            print("No se ha encontrado el Proyecto '{}'".format(codigo))
            return False

        print("Se ha eliminado el proyecto '{}' con nombre {}".format(codigo, proyectos[indice][1]))
        del proyectos[indice]
        return True


def buscarProyecto(nombre):
    for i, e in enumerate(proyectos):
        if e[0] == nombre:
            return i
    return -1


def borrarRegion():

    if len(regiones) == 0:
        print("No se ha ingresado ninguna Region ")
    else:
        codigo = idRegion()
        indice = buscarRegion(codigo)
        if indice == -1:
            print("No se ha encontrado Ninguna Region '{}'".format(codigo))
            return False

        print("Se ha eliminado La Region '{}' con nombre {}".format(codigo, regiones[indice][1]))
        del regiones[indice]
        return True


def buscarRegion(nombre):
    for i, e in enumerate(regiones):
        if e[0] == nombre:
            return i
    return -1


def Menu():
    print("---------------------------------------------------------------")
    print("Selecciona una opción...")
    print("\t1 - Registrar Cliente Nuevo.")
    print("\t2 - Listado de los clientes.")
    print("\t3 - Ingresar Proyectos.")
    print("\t4 - Listado de Proyectos.")
    print("\t5 - Ingresar Municipio y Departamento ")
    print("\t6 - Listado de Municipios y Departamentos ")
    print("\t7 - Registro detallado de Proyectos ")
    print("\t8 - Eliminar ")
    print("\t0 - Salir")

def menu2():

    print("Seleccione una opción...")
    print("a - Eliminar Cliente ")
    print("b - Eliminar Proyecto ")
    print("c - Eliminar Region ")
    print("d - Regresar al Menu ")

clientes = []
proyectos = []
regiones = []


while True:
    Menu()

    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion = -1

    if opcion == 1:
        clientes.append((ID_CODIGO(),ID_NOMBRE(), INGRESAR_DIRECCION(),INGRESAR_TELEFONO()))
    elif opcion == 2:
        ImprimirClientes()
    elif opcion == 3:
        proyectos.append((IdCodigoProyecto(), INGRESAR_DESCRIPCION(), INGRESAR_ESTADO(), ID_CODIGO_CLIENTE()))
    elif opcion == 4:
        ImprimirProyectos()
    elif opcion == 5:
        regiones.append((idRegion(), INGRESAR_MUNICIPIO(), INGRESAR_DEPARTAMENTO()))
    elif opcion == 6:
        ImprimirRegion()
    elif opcion == 7:
        PantallaRegionProyecto()
    elif opcion == 8:
        menu2()
        opcion2 = input(" Ingrese la Letra que desea elegir ")

        if opcion2 == "a":
            borrarCliente()
        if opcion2 == "b":
            borrarProyecto()
        if opcion2 == "c":
            borrarRegion()
        if opcion2 == "d":
            break

    elif opcion == 0:
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")