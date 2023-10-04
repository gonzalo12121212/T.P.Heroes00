from data_stark import*

def listado_heroes ()->str:
    """Recorre una lista con nombres

    Returns:
        str: devuelve un str
    """
    for heroe in lista_heroes:
        print("Nombre del Heroe: ")
        print("")
        print(heroe ["nombre"])
        print("")
    return heroe

def listado_nombre_y_altura ():
    for heroe in lista_heroes:
        print("Nombre y Altura del Heroe: ")
        print("")
        print(f"{heroe['nombre']} - Altura: {heroe['altura']} cm")
        print("")
    return heroe

def heroe_mas_alto ()->float:
    max_altura = float(lista_heroes[0]["altura"])
    superheroe_mas_alto = lista_heroes[0]["nombre"]

    for heroe in lista_heroes:
        altura_actual = float(heroe["altura"])
        if altura_actual > max_altura:
            superheroe_mas_alto = heroe["nombre"]
    
    print("El heroe mas alto es:")
    print("")
    print(f"**{superheroe_mas_alto}**")
    print("")
    return heroe

def heroe_menos_alto ():

    min_altura = float(lista_heroes[0]["altura"])
    superheroe_menos_alto = lista_heroes[0]["nombre"]

    for heroe in lista_heroes:
        altura_actual = float(heroe["altura"])
        if altura_actual < min_altura:
            superheroe_menos_alto = heroe["nombre"]

    print("El heroe menos alto es:")
    print("")
    print(f"**{superheroe_menos_alto}**")
    print("")
    return heroe

def promedios_altura ():

    total_alturas = 0
    cantidad_heroe = 0

    for heroe in lista_heroes:
        total_alturas += float(heroe["altura"])
        cantidad_heroe += 1

    altura_promedio = total_alturas / cantidad_heroe

    print("La altura promedio de los superheroes es: ")
    print("")
    print(f"{altura_promedio:.2f}")
    print("")
    return heroe

def comparativa_de_alturas ():
    min_altura = float(lista_heroes[0]["altura"])
    superheroe_menos_alto = lista_heroes[0]["nombre"]

    for heroe in lista_heroes:
        altura_actual = float(heroe["altura"])
        if altura_actual < min_altura:
            superheroe_menos_alto = heroe["nombre"]

    max_altura = float(lista_heroes[0]["altura"])
    superheroe_mas_alto = lista_heroes[0]["nombre"]

    for heroe in lista_heroes:
        altura_actual = float(heroe["altura"])
        if altura_actual > max_altura:
            superheroe_mas_alto = heroe["nombre"]

    print("El heroe mas alto es: ")
    print("")
    print(superheroe_mas_alto[0])
    print("")
    print("El heroe mas bajo es: ")
    print("")
    print(superheroe_menos_alto[0])
    print("")
    return heroe

def comparativa_pesos ():

    peso_mas_pesado = float(lista_heroes[0]["peso"])
    peso_menos_pesado = float(lista_heroes[0]["peso"])
    superheroe_mas_pesado = lista_heroes[0]["nombre"]
    superheroe_menos_pesado = lista_heroes[0]["nombre"]

    for heroe in lista_heroes:
        peso_actual = float(heroe["peso"])
        if peso_actual > peso_mas_pesado:
            peso_mas_pesado = peso_actual
            superheroe_mas_pesado = heroe["nombre"]
        else:
            peso_menos_pesado = peso_actual
            superheroe_menos_pesado = heroe["nombre"]

    print("")
    print("El heroe mas pesado es: ")
    print("")
    print(superheroe_mas_pesado)
    print("")
    print("El heroe menos pesado es: ")
    print("")
    print(superheroe_menos_pesado)
    return heroe
