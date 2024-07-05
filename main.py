import globales
import ventas
import os


def menu_general():
    os.system("cls")
    print("1. Asiganar montos aleatorios")
    print("2. Ver estadisticas")
    print("3. Salir")
    
    opcion = globales.seleccionar_opcion(3)

    while True:
        if opcion == 1:
            print("asignar")
        elif opcion == 2:
            print("Ver estadisticas")
        elif opcion == 3:
            return
        input()

def menu_estadisticas():
    print("1. Producto con valor más alto.")
    print("2. Producto con valor más alto.")
    print("3. Promedio del valor de los productos.")
    print("4. Media geométrica del valor de los productos")
    print("5. Salir")

    opcion = globales.seleccionar_opcion(5)

    while True:
        if opcion == 1:
            print("Producto con valor más alto.")
        elif opcion == 2:
            print("Producto con valor más alto.")
        elif opcion == 3:
            print("Promedio del valor de los productos.")
        elif opcion == 4:
            print("Media geométrica del valor de los productos")
        elif opcion == 5:
            return
        input()

menu_general()

