from enum import Enum
from abc import ABCMeta, abstractmethod

class StockInsuficienteError(Exception):
    """Excepción lanzada cuando no hay suficiente stock de un repuesto."""
    pass

class RepuestoNoEncontradoError(Exception):
    """Excepción lanzada cuando no se encuentra un repuesto en el almacén."""
    pass

class Repuesto:
    def __init__(self, nombre, proveedor, cantidad, precio):
        self.nombre = nombre
        self.proveedor = proveedor
        self.__cantidad = cantidad # Atributo privado con doble guion bajo
        self.precio = precio
    
    def get_cantidad(self):
        return self.__cantidad
    
    def modificar_cantidad(self, variacion):
        if self._cantidad + variacion < 0:
            raise StockInsuficienteError(f"No hay suficiente stock para {self.nombre}.")
        self._cantidad += variacion
    
    def obtenerDatos(self):
        return "Nombre de la pieza: "+str(self.nombre)+"\nProveedor: "+str(self.proveedor)+"\nCantidad: "+str(self.__cantidad)+"\nPrecio: "+str(self.precio)

class Almacen:
    def __init__(self, nombre, localizacion):
        self.catalogo_piezas = []
        self.nombre = nombre
        self.localizacion = localizacion

    def añadir_pieza(self, pieza):
        for p in self.catalogo_piezas:
            if p.nombre == pieza.nombre:
                print("Pieza ya disponible en el catálogo")
                return # Evita que se añada el duplicado
        self.catalogo_piezas.append(pieza)
    
    def buscar_pieza(self, nombre):
        for pieza in self.catalogo_piezas:
            if pieza.nombre == nombre:
                return pieza
        #raise RepuestoNoEncontradoError(f"La pieza '{nombre}' no está disponible en este almacén.")
    
    def adquirir_pieza(self, nombre, cantidad):
        pieza_encontrada = self.buscar_pieza(nombre)
        pieza_encontrada.modificar_cantidad(-cantidad)
        print(f"Se ha adquirido una cantidad de {cantidad} piezas de {nombre}")
    
    def obtenerDatos(self):
        # Simplificamos la impresión del catálogo
        nombres_piezas = [p.nombre for p in self.catalogo_piezas]
        return "Nombre: "+str(self.nombre)+"\nLocalización: "+str(self.localizacion)+"\nCatálogo de piezas: "+str(nombres_piezas)



class UnidadCombate(metaclass=ABCMeta):
    def __init__(self, id_combate, clave_cifrada):
        self.id_combate = id_combate
        self.clave_cifrada = clave_cifrada
    
    @abstractmethod
    def obtenerDatos(self):
        return "Identificador de combate: "+str(self.id_combate)+"\nClave cifrada: "+str(self.clave_cifrada)

class Nave(UnidadCombate):
    def __init__(self, id_combate, clave_cifrada, nombre, catalogo_piezas):
        super().__init__(id_combate, clave_cifrada)
        self.nombre = nombre
        self.catalogo_piezas = catalogo_piezas # Lista de nombres de piezas según el diagrama/enunciado
    
    def añadir_piezas_catalogo(self, nombre_repuesto):
        if nombre_repuesto in self.catalogo_piezas:
            print("Esta pieza ya se encuentra en el catálogo")
            return
        self.catalogo_piezas.append(nombre_repuesto)
    
    def obtenerDatos(self):
        return super().obtenerDatos() + "\nNombre: " + str(self.nombre) + "\nCatálogo: " + str(self.catalogo_piezas)

class Ubicacion(Enum):
    ENDOR = 1
    CUMULO_RAIMOS = 2
    NEBULOSA_KALIIDA = 3

class EstacionEspacial(Nave):
    def __init__(self, id_combate, clave_cifrada, nombre, catalogo_piezas, tripulacion, pasaje, ubicacion):
        super().__init__(id_combate, clave_cifrada, nombre, catalogo_piezas)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.ubicacion = ubicacion
    
    def obtenerDatos(self):
        return super().obtenerDatos()+"\nTripulación: "+str(self.tripulacion)+"\nPasaje: "+str(self.pasaje)+"\nUbicación: "+str(self.ubicacion.name)

class Clase(Enum):
    EJECUTOR = 1
    ECLIPSE = 2
    SOBERANO = 3

class NaveEstelar(Nave):
    def __init__(self, id_combate, clave_cifrada, nombre, catalogo_piezas, tripulacion, pasaje, clase):
        super().__init__(id_combate, clave_cifrada, nombre, catalogo_piezas)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.clase = clase
    
    def obtenerDatos(self):
        return super().obtenerDatos()+"\nTripulación: "+str(self.tripulacion)+"\nPasaje: "+str(self.pasaje)+"\nClase: "+str(self.clase.name)

class CazaEstelar(Nave):
    def __init__(self, id_combate, clave_cifrada, nombre, catalogo_piezas, dotacion):
        super().__init__(id_combate, clave_cifrada, nombre, catalogo_piezas)
        self.dotacion = dotacion
    
    def obtenerDatos(self):
        return super().obtenerDatos()+"\nDotación: "+str(self.dotacion)
