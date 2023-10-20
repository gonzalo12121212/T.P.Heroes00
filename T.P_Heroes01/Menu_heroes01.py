from Menu01 import*
from Tp_Heroes01 import*

while True:

    print("T.P Superheroes    ")
    print("")
    print("*** Menu de Heroes ***")
    print("")

    mostrar_menu()

    try:
        opcion = input("Selecciona una opción: ")
        print("")
    except:
        print("Reintente ingresando un valor numerico, porfavor")
    
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
            opcion_8()
            break

        case '9':
            opcion_9()
            break

        case '10':
            opcion_10()
            break

        case '11':
            opcion_11()
            break

        case '12':
            opcion_12()
            break

        case '13':
            opcion_13()
            break

        case '14':
            opcion_14()
            break

        case '15':
            opcion_15()
            break
