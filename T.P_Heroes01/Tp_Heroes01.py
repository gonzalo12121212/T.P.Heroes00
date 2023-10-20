from data_stark01 import lista_heroes01

def genero_Masculino():
    """Muestra una lista de superheroes por consola

    Returns:
        lista []
    """
    for heroes in lista_heroes01:
        try:    
            if heroes ["genero"] == "M":
                print("")
                print("Los Heroes con el genero Masculino son: ")
                print("")
                print(f"{heroes['nombre']} / {heroes['genero']}")
                print("")
        except:
            print("No se encontraron heroes masculino")

    return heroes


def genero_Femenino():
    """Muestra una lista de superheroes por consola

    Returns:
        lista []
    """

    for heroes in lista_heroes01:
        try:  
            if heroes ["genero"] == "F":
                print("")
                print("Los Heroes con el genero Femenino son: ")
                print("")
                print(f"{heroes['nombre']} / {heroes['genero']}")
                print("")       
        except:     
                print("No se encontraron heroes femenino")
    return heroes

def mas_alto_Masculino():
    """Muestra la altura mas alto de la lista lista_heroes01 genero masculino por consola

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con la altura mas alto.
    """
    max_altura = float(lista_heroes01[0]["altura"])
    superheroe_mas_alto = lista_heroes01[0]["nombre"]

    for heroe in lista_heroes01:
        altura_actual = float(heroe["altura"])
        try:
            if altura_actual > max_altura and heroe["genero"] == "Masculino":
                superheroe_mas_alto = heroe["nombre"]
                altura_actual_M = altura_actual
    
        except:
            print("No se encontraron Heroes masculinos")
    print("El heroe mas alto es:")
    print("")
    print(f"**{superheroe_mas_alto}: {altura_actual_M} cm**")
    print("")
    return heroe

def mas_alto_Femenino():
    """Muestra la altura mas alta de la lista lista_heroes01 genero femenino por consola

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con la altura mas alta.
    """
    max_altura = float(lista_heroes01[0]["altura"])
    superheroe_mas_alto = lista_heroes01[0]["nombre"]

    for heroe in lista_heroes01:
        altura_actual = float(heroe["altura"])
        try:
            if altura_actual > max_altura and heroe["genero"] == "Femenino":
                superheroina_mas_alto = heroe["nombre"]
                altura_actual_F = altura_actual
        except:
            print("No se encontraron Heroinas femenina")
    print("la heroina mas alta es:")
    print("")
    print(f"**{superheroina_mas_alto}: {altura_actual_F} cm**")
    print("")
    return heroe


def mas_bajo_Masculino():
    """Muestra la altura mas bajo de la lista lista_heroes01 genero masculino por consola

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con la altura mas bajo.
    """
    min_altura = float(lista_heroes01[0]["altura"])
    superheroe_mas_bajo = lista_heroes01[0]["nombre"]

    for heroe in lista_heroes01:
        altura_actual = float(heroe["altura"])
        try:
            if altura_actual < min_altura and heroe["genero"] == "Masculino":
                superheroe_mas_bajo = heroe["nombre"]
    
        except:
            print("No se encontraron Heroes masculinos")
    print("El heroe mas bajo es:")
    print("")
    print(f"**{superheroe_mas_bajo}: {min_altura} cm**")
    print("")
    return heroe

def mas_bajo_Femenino():
    """Muestra la altura mas baja de la lista lista_heroes01 genero femenino por consola

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con la altura mas baja.
    """
    min_altura = float('inf')  
    heroina_mas_baja = {}

    for heroe in lista_heroes01:
        if heroe["genero"] == "Femenino":
            altura_actual = float(heroe["altura"])
            if altura_actual < min_altura:
                heroina_mas_baja = heroe
                min_altura = altura_actual
    print("La heroína más baja es:")
    print("")
    print(f"**{heroina_mas_baja['nombre']} : {min_altura} cm**")
    return heroina_mas_baja

def promedios_altura_Masculino():
    """Muestra el promedio de alturas de la lista lista_heroes01 genero masculino por consola

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con el conteo de cada altura.
    """
    total_alturas = 0
    num_superheroes_masculinos = 0

    for heroe in lista_heroes01:
        if heroe["genero"] == "Masculino":
            total_alturas += float(heroe["altura"])
            num_superheroes_masculinos += 1
    
    if num_superheroes_masculinos > 0:
        promedio = total_alturas / num_superheroes_masculinos
        print("El promedio de alturas de superhéroes masculinos es:")
        print("")
        print(f"{promedio:2f} cm")
        return promedio

def promedios_altura_Femenino():
    """Muestra el promedio de alturas de la lista lista_heroes01 genero femenino por consola

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con el conteo de cada altura.
    """
    total_alturas = 0
    num_superheroes_femenino = 0

    for heroe in lista_heroes01:
        if heroe["genero"] == "Femenino":
            total_alturas += float(heroe["altura"])
            num_superheroes_femenino += 1
    
    if num_superheroes_femenino > 0:
        promedio = total_alturas / num_superheroes_femenino
        print("El promedio de alturas de superhéroinas femeninas es:")
        print("")
        print(f"{promedio:2f} cm")
        return promedio  

def alturas_totales_Superheroes ():
    """Muestra el promedio total de todas las alturas de la lista lista_heroes01 genero masculino y femenino por consola

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con el conteo de alturas.
    """
    max_altura = float(lista_heroes01[0]["altura"])
    superheroe_mas_alto = lista_heroes01[0]["nombre"]
    for heroe in lista_heroes01:
        altura_actual = float(heroe["altura"])
        try:
            if altura_actual > max_altura and heroe["genero"] == "Masculino":
                superheroe_mas_alto = heroe["nombre"]
                altura_actual_M = altura_actual
    
        except:
            print("No se encontraron Heroes masculinos")
    print("")
    print("Superheroe masculino mas alto: ")
    print(f"**{superheroe_mas_alto}: {altura_actual_M} cm**")
    max_altura = float(lista_heroes01[0]["altura"])
    superheroe_mas_alto = lista_heroes01[0]["nombre"]

    for heroe in lista_heroes01:
        altura_actual = float(heroe["altura"])
        try:
            if altura_actual > max_altura and heroe["genero"] == "Femenino":
                superheroina_mas_alto = heroe["nombre"]
                altura_actual_F = altura_actual
        except:
            print("No se encontraron Heroinas femenino")
    print("")
    print("Superheroina femenina mas alta: ")
    print(f"**{superheroina_mas_alto}: {altura_actual_F} cm**")
    print("")
    min_altura = float(lista_heroes01[0]["altura"])
    superheroe_mas_bajo = lista_heroes01[0]["nombre"]
    for heroe in lista_heroes01:
        altura_actual = float(heroe["altura"])
        try:
            if altura_actual < min_altura and heroe["genero"] == "Masculino":
                superheroe_mas_bajo = heroe["nombre"]
        except:
            print("No se encontraron Heroes masculinos")
    print("Superheroe masculino mas bajo: ")
    print(f"**{superheroe_mas_bajo}: {min_altura} cm**")
    print("")
    min_altura = float('inf')  
    heroina_mas_baja = {}
    for heroe in lista_heroes01:
        if heroe["genero"] == "Femenino":
            altura_actual = float(heroe["altura"])
            if altura_actual < min_altura:
                heroina_mas_baja = heroe
                min_altura = altura_actual
    print("Superheroina femenina mas baja: ")
    print(f"**{heroina_mas_baja['nombre']} : {min_altura} cm**")

def cant_color_de_ojos():
    """Cuenta cuántos superhéroes tienen cada tipo de color de ojos.

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con el conteo de cada tipo de color de ojos.
    """
    conteo_color_ojos = {}

    for heroe in lista_heroes01:
        color_ojos = heroe.get("color_ojos", "Desconocido")
        if color_ojos in conteo_color_ojos:
            conteo_color_ojos[color_ojos] += 1
        else:
            conteo_color_ojos[color_ojos] = 1
    print("Cantidad de superhéroes por color de ojos:")
    for color, cantidad in conteo_color_ojos.items():
        print(f"{color}: {cantidad}")
        
def cant_color_de_pelo():
    """Cuenta cuántos superhéroes tienen cada tipo de color de pelo.

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con el conteo de cada tipo de color de pelo.
    """
    conteo_color_pelo = {}

    for heroe in lista_heroes01:
        color_pelo = heroe.get("color_pelo", "Desconocido")
        if color_pelo in conteo_color_pelo:
            conteo_color_pelo[color_pelo] += 1
        else:
            conteo_color_pelo[color_pelo] = 1
    print("Cantidad de superhéroes por color de pelo:")
    for color, cantidad in conteo_color_pelo.items():
        print(f"{color}: {cantidad}")

def tipo_inteligencia():
    """Cuenta cuántos superhéroes tienen cada tipo de inteligencia.

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con el conteo de cada tipo de inteligencia.
    """
    conteo_inteligencia = {}

    for heroe in lista_heroes01:
        tipo_inteligencia = heroe.get("inteligencia", "No Tiene")
        if tipo_inteligencia in conteo_inteligencia:
            conteo_inteligencia[tipo_inteligencia] += 1
        else:
            conteo_inteligencia[tipo_inteligencia] = 1
    print("Cantidad de superhéroes por tipo de inteligencia:")
    for tipo, cantidad in conteo_inteligencia.items():
        print(f"{tipo}: {cantidad}")

    return conteo_inteligencia

def heroes_por_color_de_ojos():
    """Agrupa superhéroes por color de ojos.

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con superhéroes agrupados por color de ojos.
    """
    superheroes_por_color_ojos = {}

    for heroe in lista_heroes01:
        color_ojos = heroe.get("color_ojos", "Desconocido")
        if color_ojos in superheroes_por_color_ojos:
            superheroes_por_color_ojos[color_ojos].append(heroe)
        else:
            print("No se encontraon heroes")
    for color_ojos in lista_heroes01:
        heroes_ojos = color_ojos['color_ojos']
        heroe_1 = color_ojos['nombre']
        print("Superhéroe y su tipo de color de ojo: ")
        print("")
        print(f"Nombre:{heroe_1} / Color de ojo: {heroes_ojos}")
        print("")
    return heroe, color_ojos

def heroes_por_color_de_pelo():
    """Agrupa superhéroes por color de pelo.

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con superhéroes agrupados por color de pelo.
    """
    superheroes_por_color_pelo = {}

    for heroe in lista_heroes01:
        color_pelo = heroe.get("color_pelo", "Desconocido")
        if color_pelo in superheroes_por_color_pelo:
            superheroes_por_color_pelo[color_pelo].append(heroe)
        else:
            print("No se encontraon heroes")
    for color_pelo in lista_heroes01:
        heroes_pelo = color_pelo['color_pelo']
        heroe_1 = color_pelo['nombre']
        print("Superhéroe y su tipo de color de pelo: ")
        print("")
        print(f"Nombre:{heroe_1} / Color de pelo: {heroes_pelo}")
        print("")
    return heroe, color_pelo

def heroe_por_tipo_de_inteligencia():
    """Agrupa superhéroes por tipo de inteligencia.

    Args:
        lista_heroes01 (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con superhéroes agrupados por tipo de inteligencia.
    """
    superheroes_por_tipo_de_inteligencia = {}

    for heroe in lista_heroes01:
        inteligencia_tipo = heroe.get("inteligencia", "Desconocido")
        if inteligencia_tipo in superheroes_por_tipo_de_inteligencia:
            superheroes_por_tipo_de_inteligencia[inteligencia_tipo].append(heroe)
        else:
            print("No se encontraon heroes")
    for inteligencia_tipo in lista_heroes01:
        heroes_inteligencia = inteligencia_tipo['inteligencia']
        heroe_1 = inteligencia_tipo['nombre']
        print("Superhéroe y su tipo de inteligencia: ")
        print("")
        print(f"Nombre:{heroe_1} / Tipo de inteligencia: {heroes_inteligencia}")
        print("")
    return heroe, inteligencia_tipo