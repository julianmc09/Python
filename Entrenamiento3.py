# Inventario (diccionario con nombre como clave y tupla (precio, cantidad) como valor)
inventario = {}
# Funciones para cada opcion del menu

def AgregarProducto(nombre, precio, cantidad):
    if nombre in inventario:
        print(f"El producto {nombre} ya existe.")
    else:
        inventario[nombre] = (precio, cantidad)
        print(f"Producto {nombre} agregado exitosamente.")

def ConsultarProducto(nombre):
    producto = inventario.get(nombre)
    if producto:
        print(f"Producto: {nombre}\nPrecio: {producto[0]}\nCantidad: {producto[1]}")
    else:
        print(f"El producto {nombre} no se encuentra en el inventario.")

def ActualizarPrecio(nombre, NuevoPrecio):
    if nombre in inventario:
        _,cantidad = inventario[nombre]
        inventario[nombre] = (NuevoPrecio, cantidad)
        print(f"Precio del producto {nombre} actualizado a {NuevoPrecio}.")
    else:
        print(f"No se puede actualizar. El producto {nombre} no esta en el inventario.")

def EliminarProducto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"El producto {nombre} se ha eliminado del inventario.")
    else:
        print(f"No se puede eliminar. El producto {nombre} no existe.")

def CalcularValorTotal():
    calcular = lambda inv: sum(precio * cantidad for precio, cantidad in inv.values())
    total = calcular(inventario)
    print(f"Valor total del inventario: {total}")

# Validación de datos limpios
def leer_entero(mensaje):
    entrada = input(mensaje)
    if entrada.isdigit():
        return int(entrada)
    else:
        print("Informacion ingresada no válida")
        return None

# Creacion del menu

while True:
    opcion = input("Ingrese la opcion que desea realizar:\n 1.Añadir producto\n 2.Consultar producto\n 3.Actualizar precio\n 4.Eliminar producto\n 5.Calcular valor total del inventario\n 6.Salir del menu\n ")
    if opcion == "1":
        nombre = input("Nombre del producto: ").strip()
        precio = leer_entero("Precio del producto: ")
        cantidad = leer_entero("Cantidad del producto: ")
        if precio is not None and cantidad is not None:
            AgregarProducto(nombre, precio, cantidad)

    elif opcion == "2":
        nombre = input("Nombre del producto a consultar: ").strip()
        ConsultarProducto(nombre)

    elif opcion == "3":
        nombre = input("Nombre del producto a actualizar: ").strip()
        NuevoPrecio = leer_entero("Nuevo precio: ")
        if NuevoPrecio is not None:
            ActualizarPrecio(nombre, NuevoPrecio)

    elif opcion == "4":
        nombre = input("Nombre del producto a eliminar: ").strip()
        EliminarProducto(nombre)

    elif opcion == "5":
        CalcularValorTotal()

    elif opcion == "6":
        print("Usted ha salido del menu")
        break
    else:
        print("Opcion no valida.")
