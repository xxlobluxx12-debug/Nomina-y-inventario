class Equipo:

    def __init__(self, nombre, cantidad):
        self.__nombre__ = nombre
        self.__cantidad__ = cantidad

    def get_nombre(self):
        return self.__nombre__

    def get_cantidad(self):
        return self.__cantidad__

    def set_nombre(self, nombre):
        self.__nombre__ = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad__ = cantidad


class Inventario:

    def __init__(self):
        self.__equipos__ = []

    def agregar(self, equipo):
        self.__equipos__.append(equipo)

    def obtener(self):
        return self.__equipos__

    def editar(self, posicion, nombre, cantidad):

        if posicion >= 0 and posicion < len(self.__equipos__):

            self.__equipos__[posicion].set_nombre(nombre)
            self.__equipos__[posicion].set_cantidad(cantidad)

            return True

        return False

    def eliminar(self, posicion):

        if posicion >= 0 and posicion < len(self.__equipos__):

            self.__equipos__.pop(posicion)

            return True

        return False
