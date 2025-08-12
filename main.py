# main.py
from inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("ID: ").strip()
                nombre = input("Nombre: ").strip()
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Cantidad y precio deben ser números.")

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ").strip()
            cantidad_input = input("Nueva cantidad (dejar vacío si no se cambia): ")
            precio_input = input("Nuevo precio (dejar vacío si no se cambia): ")

            cantidad = int(cantidad_input) if cantidad_input else None
            precio = float(precio_input) if precio_input else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre o parte del nombre a buscar: ").strip()
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for r in resultados:
                    print(r)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
