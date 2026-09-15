from nomina import Empleado
from nomina import Nomina

from inventario import Equipo
from inventario import Inventario

nomina = Nomina()
inventario = Inventario()

# MENU PRINCIPAL


def menu_principal():

    while True:

        print("\n===== EMPRESA =====")
        print("1. Nomina")
        print("2. Inventario")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_nomina()

        elif opcion == "2":
            menu_inventario()

        elif opcion == "3":
            print("Programa terminado.")
            break

        else:
            print("Opcion no valida.")


# MENU DE NOMINA

def menu_nomina():

    while True:

        print("\n===== NOMINA =====")
        print("1. Agregar empleado")
        print("2. Mostrar empleados")
        print("3. Editar empleado")
        print("4. Eliminar empleado")
        print("5. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_empleado()

        elif opcion == "2":
            mostrar_empleados()

        elif opcion == "3":
            editar_empleado()

        elif opcion == "4":
            eliminar_empleado()

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


def agregar_empleado():

    nombre = input("Nombre: ")
    cargo = input("Cargo: ")
    sueldo = float(input("Sueldo: "))

    empleado = Empleado(nombre, cargo, sueldo)

    nomina.agregar(empleado)

    print("Empleado agregado correctamente.")


def mostrar_empleados():

    empleados = nomina.obtener()

    if len(empleados) == 0:
        print("No hay empleados.")
        return

    for i in range(len(empleados)):

        print("\nEmpleado", i + 1)
        print("Nombre:", empleados[i].get_nombre())
        print("Cargo:", empleados[i].get_cargo())
        print("Sueldo:", empleados[i].get_sueldo())


def editar_empleado():

    empleados = nomina.obtener()

    if len(empleados) == 0:
        print("No hay empleados.")
        return

    mostrar_empleados()

    posicion = int(input("\nSeleccione el empleado: ")) - 1

    nombre = input("Nuevo nombre: ")
    cargo = input("Nuevo cargo: ")
    sueldo = float(input("Nuevo sueldo: "))

    if nomina.editar(posicion, nombre, cargo, sueldo):
        print("Empleado editado correctamente.")
    else:
        print("Posicion no valida.")


def eliminar_empleado():

    empleados = nomina.obtener()

    if len(empleados) == 0:
        print("No hay empleados.")
        return

    mostrar_empleados()

    posicion = int(input("\nSeleccione el empleado: ")) - 1

    if nomina.eliminar(posicion):
        print("Empleado eliminado correctamente.")
    else:
        print("Posicion no valida.")

# MENU DE INVENTARIO

def menu_inventario():

    while True:

        print("\n===== INVENTARIO =====")
        print("1. Agregar equipo")
        print("2. Mostrar equipos")
        print("3. Editar equipo")
        print("4. Eliminar equipo")
        print("5. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_equipo()

        elif opcion == "2":
            mostrar_equipos()

        elif opcion == "3":
            editar_equipo()

        elif opcion == "4":
            eliminar_equipo()

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


def agregar_equipo():

    nombre = input("Nombre del equipo: ")
    cantidad = int(input("Cantidad: "))

    equipo = Equipo(nombre, cantidad)

    inventario.agregar(equipo)

    print("Equipo agregado correctamente.")


def mostrar_equipos():

    equipos = inventario.obtener()

    if len(equipos) == 0:
        print("No hay equipos.")
        return

    for i in range(len(equipos)):

        print("\nEquipo", i + 1)
        print("Nombre:", equipos[i].get_nombre())
        print("Cantidad:", equipos[i].get_cantidad())


def editar_equipo():

    equipos = inventario.obtener()

    if len(equipos) == 0:
        print("No hay equipos.")
        return

    mostrar_equipos()

    posicion = int(input("\nSeleccione el equipo: ")) - 1

    nombre = input("Nuevo nombre: ")
    cantidad = int(input("Nueva cantidad: "))

    if inventario.editar(posicion, nombre, cantidad):
        print("Equipo editado correctamente.")
    else:
        print("Posicion no valida.")


def eliminar_equipo():

    equipos = inventario.obtener()

    if len(equipos) == 0:
        print("No hay equipos.")
        return

    mostrar_equipos()

    posicion = int(input("\nSeleccione el equipo: ")) - 1

    if inventario.eliminar(posicion):
        print("Equipo eliminado correctamente.")
    else:
        print("Posicion no valida.")


menu_principal()
