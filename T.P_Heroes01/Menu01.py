from Tp_Heroes01 import*

def mostrar_menu():
    """ Muestra un menu personalizado con 8 opciones (una opcion es el exit)
    """
    
    print("1. Lista de Superheroes Masculinos")
    print("2. Lista de Superheroes Femeninos")
    print("3. Muestra al Heroe mas alto")
    print("4. Muestra a la Heroina mas alta")
    print("5. Muestra al Heroe mas bajo")
    print("6. Muestra a la Heroeina mas baja")
    print("7. Calcula el promedio de los heroes masculinos")
    print("8. Calcula el promedio de las heroinas femeninos")
    print("9. Muestra el mas bajo y alto de todos los superheroes y superheroinas")
    print("10. Determina cuantos superheroes tienen cada tipo de color de ojos")
    print("11. Determina cuantos superheroes tienen cada tipo de color de pelo")
    print("12. Determina cuantos superheroes tienen cada tipo de inteligencia")
    print("13. Determina a los superheroes por color de ojos")
    print("14. Determina a los superheroes por colo de pelos")
    print("15. Determina a los superheroes por tipo de inteligencia")
    print("")

def opcion_1():
    print("")
    genero_Masculino()
    
def opcion_2():
    print("")
    genero_Femenino()

def opcion_3():
    print("")
    mas_alto_Masculino()

def opcion_4 ():
    print("")
    mas_alto_Femenino()

def opcion_5 ():
    print("")
    mas_bajo_Masculino()

def opcion_6 ():
    print("")
    mas_bajo_Femenino()
    
def opcion_7 ():
    print("")
    promedios_altura_Masculino()

def opcion_8():
    print("")
    promedios_altura_Femenino()

def opcion_9():
    print("")
    alturas_totales_Superheroes()

def opcion_10():
    cant_color_de_ojos()
    print("")

def opcion_11():
    cant_color_de_pelo()
    print("")

def opcion_12():
    tipo_inteligencia()
    print("")

def opcion_13():
    heroes_por_color_de_ojos()
    print("")

def opcion_14():
    heroes_por_color_de_pelo()
    print("")

def opcion_15():
    heroe_por_tipo_de_inteligencia()
    print("")