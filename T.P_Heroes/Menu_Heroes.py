from Menu import*

while True:

    print("T.P Superheroes    ")
    print("")
    print("*** Menu de Heroes ***")
    print("")

    mostrar_menu()

    try:
        opcion = input("Selecciona una opción: ")
    except:
        print("Reintente ingresando un valor numerico, porfavor")
    try:
        match opcion :
            case '1':
                opcion_1()
                break

            case '2':
                opcion_2()
                break

            case '3':
                opcion_3()
                break

            case '4':
                opcion_4()
                break

            case '5':
                opcion_5()
                break

            case '6':
                opcion_6()
                break

            case '7':
                opcion_7()
                break

            case '8':    
                break

    except:
        print("Opción inválida. Inténtalo de nuevo.")