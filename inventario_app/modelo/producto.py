# ============================================
# MODELO: Producto
# Representa un ítem del inventario de la tienda
# ============================================
class Producto:
    # ----------- CONSTRUCTOR -----------
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio
    
    # ----------- GETTERS -----------
    def get_id(self):
        return self.__id_producto
    
    def get_nombre(self):
        return self.__nombre
    
    def get_cantidad(self):
        return self.__cantidad
    
    def get_precio(self):
        return self.__precio
    
    # ----------- SETTERS -----------
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("⚠️ Cantidad inválida")
    
    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("⚠️ Precio inválido")
    
    # ----------- MÉTODO STR -----------
    def __str__(self):
        return (
            f"[{self.__id_producto}] "
            f"{self.__nombre} | "
            f"Cant: {self.__cantidad} | "
            f"${self.__precio:.2f}"
        )