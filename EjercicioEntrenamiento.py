#Declaracion de variables principales
print("Ingrese lo que desea comprar")
Nombre = input("Nombre del producto: ")
print("Ingrese el precio por unidad")
PrecioU = float(input("Precio por unidad del producto: "))
Cantidad = 0
Descuento = 0
PrecioInicial = 0
PrecioF = 0

#Condicion para que el precio no sea un numero negativo
if PrecioU>0:
    Cantidad = int(input("Ingrese la cantidad de productos: "))

    #Condicion para que la cantidad de productos no se un numero negativo
    if Cantidad>0:
        Descuento = float(input("Agregue el descuento que tiene en su producto: "))

        #Condicion para validar que el descuentro ingresado para el producto sea entre 0 y 100
        if Descuento >= 0 and Descuento<=100:

            #Condicion para saber si hay descuento o no en el producto
            if Descuento != 0:
                PrecioInicial = PrecioU*Cantidad
                Descuento = PrecioInicial*(Descuento/100)
                PrecioF = PrecioInicial - Descuento
                print("Informacion del producto: ")
                print(f"Nombre: {Nombre}  Precio sin descuento: {PrecioInicial}  Precio con descuento: {PrecioF}")
            else: 
                PrecioInicial = PrecioU*Cantidad
                PrecioF = PrecioInicial
                print("Informacion del producto: ")
                print(f"Nombre: {Nombre}  Precio del producto: {PrecioInicial}")

                #Mensajes para cuando no se ingrese un numero establecido, como por ejemplo un numero negativo o un numero fuera del porcentaje de 0 a 100
        else:
            print("Numero no valido")
    else:
        print("Numero no valido")
else:
    print("Numero no valido")
