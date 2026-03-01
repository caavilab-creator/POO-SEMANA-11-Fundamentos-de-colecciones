# ============================================
# SISTEMA PRINCIPAL
# Inventario App
# ============================================
from servicio.inventari import Inventario

def mostrar_menu():
    print("""
=============================
  📦  SISTEMA DE INVENTARIO
=============================
1. Agregar producto
2. Listar productos
3. Buscar producto por ID
4. Actualizar producto
5. Eliminar producto
6. Buscar producto por nombre
0. Salir
=============================
""")

def main():
    inventario = Inventario()
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione opción: "))
            if opcion == 1:
                inventario.agregar_producto()
            elif opcion == 2:
                inventario.listar_productos()
            elif opcion == 3:
                id_p = int(input("ID a buscar: "))
                p = inventario.buscar_por_id(id_p)
                if p:
                    print("🔎 Encontrado:", p)
                else:
                    print("❌ No existe")
            elif opcion == 4:
                inventario.actualizar_producto()
            elif opcion == 5:
                inventario.eliminar_producto()
            elif opcion == 6:
                nombre = input("Nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)
                if resultados:
                    print("\n🔎 Resultados encontrados:")
                    for p in resultados:
                        print(p)
                else:
                    print("❌ No se encontraron productos")
            elif opcion == 0:
                inventario.guardar_en_archivo()
                print("💾 Cambios guardados en inventario.txt")
                print("👋 Saliendo del sistema...")
                break
            else:
                print("⚠️ Opción inválida")
        except ValueError:
            print("⚠️ Debe ingresar números")

if __name__ == "__main__":
    main()