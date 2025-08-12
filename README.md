Diagrama de clases y flujo
Diagrama UML simplificado
┌───────────────────┐
│     Producto      │
├───────────────────┤
│ - id_producto     │
│ - nombre          │
│ - cantidad        │
│ - precio          │
├───────────────────┤
│ + get_id()        │
│ + get_nombre()    │
│ + get_cantidad()  │
│ + get_precio()    │
│ + set_nombre()    │
│ + set_cantidad()  │
│ + set_precio()    │
│ + __str__()       │
└───────────────────┘

          ▲
          │ (contiene)
          │
┌───────────────────┐
│    Inventario     │
├───────────────────┤
│ - productos[]     │
│ - archivo_datos   │
├───────────────────┤
│ + añadir_producto()│
│ + eliminar_producto() │
│ + actualizar_producto()│
│ + buscar_por_nombre() │
│ + mostrar_todos()     │
│ + guardar_en_archivo()│
│ + cargar_desde_archivo() │
└───────────────────┘

          ▲
          │ (usa)
          │
┌───────────────────┐
│      main.py      │
├───────────────────┤
│ + menu()          │
└───────────────────┘
Flujo del programa
main.py se ejecuta → crea un objeto Inventario.

Inventario intenta cargar datos desde datos_inventario.json.

Menú en consola:

Opción 1 → crear Producto y añadirlo a Inventario.

Opción 2 → eliminar producto por ID.

Opción 3 → actualizar cantidad/precio.

Opción 4 → buscar productos por nombre.

Opción 5 → mostrar todos los productos.

Opción 6 → salir.

Cada cambio se guarda en el archivo JSON automáticamente.

# Sistema de Gestión de Inventarios (Python)

Este proyecto es un sistema simple de gestión de inventarios en **Python** utilizando Programación Orientada a Objetos (POO) y estructuras de datos personalizadas.  
Los datos se guardan en un archivo **JSON** para que el inventario se mantenga entre ejecuciones.

---

# Funcionalidades
- Añadir productos (ID único).
- Eliminar productos por ID.
- Actualizar cantidad o precio.
- Buscar productos por nombre (búsqueda parcial).
- Mostrar todos los productos.
- Guardar y cargar datos automáticamente en un archivo JSON.

---

# Tecnologías usadas
- **Python 3.x**
- **POO (Programación Orientada a Objetos)**
- Manejo de **archivos JSON**
- **Control de versiones** con Git y GitHub

---

# Estructura del proyecto
proyecto_inventario/
│
├── producto.py # Clase Producto
├── inventario.py # Clase Inventario (gestiona la lista de productos)
├── main.py # Menú interactivo
├── datos_inventario.json # Archivo donde se guardan los datos
└── README.md # Documentación del proyecto


---

# Ejecución
1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/proyecto_inventario.git
   cd proyecto_inventario

Ejecutar el programa:
python main.py

Ejemplo de uso
===== SISTEMA DE INVENTARIO =====
1. Añadir producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto por nombre
5. Mostrar todos los productos
6. Salir
Seleccione una opción: 1
ID: P001
Nombre: Camiseta
Cantidad: 10
Precio: 15.5
Producto añadido con éxito.

Diagrama de clases
┌───────────────────┐
│     Producto      │
├───────────────────┤
│ - id_producto     │
│ - nombre          │
│ - cantidad        │
│ - precio          │
├───────────────────┤
│ + getters/setters │
│ + __str__()       │
└───────────────────┘

┌───────────────────┐
│    Inventario     │
├───────────────────┤
│ - productos[]     │
│ - archivo_datos   │
├───────────────────┤
│ + añadir/eliminar │
│ + actualizar      │
│ + buscar/mostrar  │
│ + guardar/cargar  │
└───────────────────┘

Autor; Johnny Vera 
Estudiante de Universidad Estatal Amazinica UEA 
Asignatura: POO
Proyecto desarrollado como práctica de POO, manejo de archivos y estructuras de datos.
