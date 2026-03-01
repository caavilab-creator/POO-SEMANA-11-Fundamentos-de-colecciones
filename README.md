# 📦 Sistema Avanzado de Gestión de Inventario

Sistema de gestión de inventarios desarrollado con **Programación Orientada a Objetos (POO)** en Python. Permite administrar productos de una tienda de manera eficiente, con almacenamiento persistente en archivos y uso optimizado de colecciones (diccionarios).

## ✨ Características

- ✅ **CRUD Completo**: Crear, leer, actualizar y eliminar productos
- 🔍 **Búsqueda Rápida**: Búsqueda por ID (diccionario) y por nombre
- 💾 **Persistencia de Datos**: Almacenamiento automático en archivo `inventario.txt`
- 🎯 **POO**: Diseño orientado a objetos con encapsulamiento
- 📊 **Validaciones**: Control de datos inválidos y duplicados
- 🖥️ **Interfaz Intuitiva**: Menú interactivo en consola
- 📁 Estructura del Proyecto
- inventario_app/
│
├── modelo/
│   ├── __init__.py
│   └── producto.py          # Clase Producto (atributos y métodos)
│
├── servicio/
│   ├── __init__.py
│   └── inventari.py         # Clase Inventario (CRUD y persistencia)
│
├── main.py                  # Menú interactivo y punto de entrada
└── servicio/registros/
    └── inventario.txt       # Archivo de persistencia (se genera automáticamente)
  🎯 Uso
Al ejecutar el programa, se verá el siguiente menú:
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
