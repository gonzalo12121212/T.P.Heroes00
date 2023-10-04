from Tp_Heroes import*

def mostrar_menu():
    """ Muestra un menu personalizado con 8 opciones (una opcion es el exit)
    """
    
    print("1. Lista de Superheroes ingresados")
    print("2. Lista de nombres y altura de los Superheroes")
    print("3. Muestra al Superheroe mas alto")
    print("4. Muestra al Superheroe mas bajo")
    print("5. Mide el promedio de las alturas de los Superheores")
    print("6. Compara las altura de los Superheroes")
    print("7. Compara los pesos de los Superheroes")
    print("8. Cerrar menu de opciones")
    print("")

def opcion_1():
    print("")
    listado_heroes()
    
def opcion_2():
    print("")
    listado_nombre_y_altura ()

def opcion_3():
    print("")
    heroe_mas_alto ()

def opcion_4 ():
    print("")
    heroe_menos_alto ()

def opcion_5 ():
    print("")
    promedios_altura()

def opcion_6 ():
    print("")
    comparativa_de_alturas()
    
def opcion_7 ():
    print("")
    comparativa_pesos ()
