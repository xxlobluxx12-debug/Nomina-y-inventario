class Empleado:

    def __init__(self, nombre, cargo, sueldo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__sueldo__ = sueldo

    def get_nombre(self):
        return self.__nombre__

    def get_cargo(self):
        return self.__cargo__

    def get_sueldo(self):
        return self.__sueldo__

    def set_nombre(self, nombre):
        self.__nombre__ = nombre

    def set_cargo(self, cargo):
        self.__cargo__ = cargo

    def set_sueldo(self, sueldo):
        self.__sueldo__ = sueldo


class Nomina:

    def __init__(self):
        self.__empleados__ = []

    def agregar(self, empleado):
        self.__empleados__.append(empleado)

    def obtener(self):
        return self.__empleados__

    def editar(self, posicion, nombre, cargo, sueldo):

        if posicion >= 0 and posicion < len(self.__empleados__):

            self.__empleados__[posicion].set_nombre(nombre)
            self.__empleados__[posicion].set_cargo(cargo)
            self.__empleados__[posicion].set_sueldo(sueldo)

            return True

        return False

    def eliminar(self, posicion):

        if posicion >= 0 and posicion < len(self.__empleados__):

            self.__empleados__.pop(posicion)

            return True

        return False
