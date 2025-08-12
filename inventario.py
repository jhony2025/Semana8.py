# inventario.py
import json
from producto import Producto

class Inventario:
    """
    Clase que gestiona una lista de productos.
    """

    def __init__(self, archivo_datos="datos_inventario.json"):
        """
        Inicializa el inventario, cargando datos si existen.
        :param archivo_datos: Archivo JSON donde se guarda el inventario
        """
        self.archivo_datos = archivo_datos
        self.productos = []
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto si el ID es único.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado con éxito.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto por su ID.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                self.guardar_en_archivo()
                print("Producto actualizado con éxito.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """
        Busca productos cuyo nombre contenga la cadena dada (sin importar mayúsculas).
        """
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return encontrados

    def mostrar_todos(self):
        """
        Muestra todos los productos del inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)

    # -------------------------------
    # Métodos para guardar y cargar datos
    # -------------------------------
    def guardar_en_archivo(self):
        """
        Guarda el inventario en un archivo JSON.
        """
        try:
            datos = [
                {
                    "id": p.get_id(),
                    "nombre": p.get_nombre(),
                    "cantidad": p.get_cantidad(),
                    "precio": p.get_precio()
                }
                for p in self.productos
            ]
            with open(self.archivo_datos, "w") as f:
                json.dump(datos, f, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def cargar_desde_archivo(self):
        """
        Carga el inventario desde un archivo JSON si existe.
        """
        try:
            with open(self.archivo_datos, "r") as f:
                datos = json.load(f)
                self.productos = [Producto(d["id"], d["nombre"], d["cantidad"], d["precio"]) for d in datos]
        except FileNotFoundError:
            self.productos = []
        except json.JSONDecodeError:
            print("Error: El archivo de datos está dañado. Se iniciará un inventario vacío.")
            self.productos = []
