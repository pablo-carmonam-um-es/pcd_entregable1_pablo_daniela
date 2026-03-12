class Repuesto:
    def __init__(self, nombre, proveedor, cantidad, precio):
        self.nombre = nombre
        self.proveedor = proveedor
        self.__cantidad = cantidad # Atributo privado con doble guion bajo
        self.precio = precio
    
    def get_cantidad(self):
        return self.__cantidad
    
    def modificar_cantidad(self, variacion):
        #if self.__cantidad + variacion < 0:
            #raise StockInsuficienteError(f"No hay suficiente stock para {self.nombre}.")
        self.__cantidad += variacion
    
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
