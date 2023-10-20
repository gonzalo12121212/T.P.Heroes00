from data_stark01 import*

# for heroes in lista_heroes01:
#         try:
             
#             if heroes ["genero"] == "F":
#                 print("")
#                 print("Los Heroes con el genero Femenino son: ")
#                 print("")
#                 print(f"{heroes['nombre']} / {heroes['genero']}")
#                 print("")       
#         except:     
#                 print("No se encontraron heroes femenino")
for heroe in lista_heroes01:
        altura_actual = float(heroe["altura"])
        max_altura = float(lista_heroes01[0]["altura"])
        heroinas = heroe["genero"] == "Femenino"
        if heroinas:
            try:
                if altura_actual > max_altura and heroinas:
                    superheroe_mas_alto = heroe["nombre"]
                    altura_actual_F = float(heroe["altura"])
            except:
                print("No se encontraron heroinas femeninas")
        else:
            print("vete a chingar heroe masculino")
            break
        print("La heroina mas alta es:")
        print("")
        print(f"**{superheroe_mas_alto}: {altura_actual_F}**")
        print("")
