import apiBuscar
codigo = ""
while codigo != "salir":
    codigo = input('Escriba el codigo del producto: ')
    if codigo.lower()=="salir":break
    respuesta = apiBuscar.buscarProducto(codigo)
    if respuesta == 0:
        print("No se localizó el codigo del producto " + codigo)
    elif respuesta == -1:
        print('error en la conexion')
    else:
        print('Nombre del Producto: ' + str(respuesta[1]) + "\n" + 'Precio del Producto ' + str(respuesta[2]) + "\n" + 'Precio del Producto ' + str(respuesta[3]))
print("Gracias por usar el sistema amiko")