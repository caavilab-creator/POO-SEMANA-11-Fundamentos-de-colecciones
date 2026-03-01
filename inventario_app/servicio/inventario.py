# ============================================
# SERVICIO: Gestión del Inventario
# CRUD de Productos
# ============================================
import os
from modelo.producto import Producto

class Inventario:
    def __init__(self, ruta_archivo: str = None):
        base_dir = os.path.dirname(__file__)
        ruta_archivo = os.path.join(
            base_dir,
            "registros",
            "inventario.txt"
        )
        self.ruta_archivo = ruta_archivo
        self.productos = {}  # Diccionario {id_producto: Producto}
        self.cargar_desde_archivo()
    
    # ----------- CARGAR DESDE ARCHIVO -----------
    def asegurar_archivo(self):
        carpeta = os.path.dirname(self.ruta_archivo)
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                pass
    
    def cargar_desde_archivo(self) -> None:
        """
        Lee inventario.txt y carga self.productos.
        Si el archivo no existe, lo crea.
        """
        self.asegurar_archivo()
        self.productos.clear()
        with open(self.ruta_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                producto = self._linea_a_producto(linea)
                if producto:
                    self.productos[producto.get_id()] = producto
    
    def guardar_en_archivo(self) -> None:
        """
        Guarda la lista de productos en inventario.txt.
        """
        self.asegurar_archivo()
        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            for producto in self.productos.values():
                f.write(self._producto_a_linea(producto) + "\n")
    
    def _producto_a_linea(self, producto: Producto) -> str:
        """
        Convierte un Producto a una línea TXT: id|nombre|cantidad|precio
        """
        nombre = producto.get_nombre().replace("|", "/")
        return f"{producto.get_id()}|{nombre}|{producto.get_cantidad()}|{producto.get_precio()}"
    
    def _linea_a_producto(self, linea: str):
        """
        Convierte una línea TXT a Producto.
        Maneja errores sin romper el programa.
        """
        try:
            partes = linea.split("|")
            if len(partes) != 4:
                return None
            id_p = int(partes[0])
            nombre = partes[1]
            cantidad = int(partes[2])
            precio = float(partes[3])
            return Producto(id_p, nombre, cantidad, precio)
        except Exception:
            return None
    
    # ----------- AGREGAR -----------
    def agregar_producto(self):
        try:
            id_p = int(input("ID: "))
            # Validar duplicado
            if self.buscar_por_id(id_p):
                print("⚠️ Ya existe un producto con ese ID")
                return
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            nuevo = Producto(id_p, nombre, cantidad, precio)
            self.productos[id_p] = nuevo
            self.guardar_en_archivo()
            print("✅ Producto agregado")
        except ValueError:
            print("⚠️ Error en los datos ingresados")
    
    # ----------- LISTAR -----------
    def listar_productos(self):
        if not self.productos:
            print("📭 No hay productos registrados")
            return
        print("\n📋 INVENTARIO DE LA TIENDA")
        print("-" * 60)
        for producto in self.productos.values():
            print(producto)
        print("-" * 60)
        print(f"Total de productos: {len(self.productos)}")
    
    # ----------- BUSCAR POR ID -----------
    def buscar_por_id(self, id_producto):
        return self.productos.get(id_producto)
    
    # ----------- BUSCAR POR NOMBRE -----------
    def buscar_por_nombre(self, nombre_producto):
        resultados = []
        for producto in self.productos.values():
            if nombre_producto.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados
    
    # ----------- ACTUALIZAR -----------
    def actualizar_producto(self):
        try:
            id_p = int(input("ID a actualizar: "))
            producto = self.buscar_por_id(id_p)
            if not producto:
                print("❌ Producto no encontrado")
                return
            print(f"Producto actual: {producto}")
            nueva_cantidad = int(input("Nueva cantidad: "))
            nuevo_precio = float(input("Nuevo precio: "))
            producto.set_cantidad(nueva_cantidad)
            producto.set_precio(nuevo_precio)
            self.guardar_en_archivo()
            print("✅ Producto actualizado")
        except ValueError:
            print("⚠️ Datos inválidos")
    
    # ----------- ELIMINAR -----------
    def eliminar_producto(self):
        try:
            id_p = int(input("ID a eliminar: "))
            producto = self.buscar_por_id(id_p)
            if not producto:
                print("❌ Producto no encontrado")
                return
            confirmacion = input(f"¿Está seguro de eliminar '{producto.get_nombre()}'? (s/n): ")
            if confirmacion.lower() == 's':
                del self.productos[id_p]
                self.guardar_en_archivo()
                print("🗑️ Producto eliminado")
            else:
                print("❌ Eliminación cancelada")
        except ValueError:
            print("⚠️ ID inválido")