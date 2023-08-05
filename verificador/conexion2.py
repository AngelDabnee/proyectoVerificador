import mysql.connector
def buscarProducto(producto):
    try:
        conexionpyhton = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'pos') 
        resultado = conexionpyhton.cursor()
        resultado.execute("SELECT * FROM productos WHERE nombre = '"+producto+"'")
        registros = resultado.fetchone()
        if registros:
            return str(registros[2])
        else:
            return 0

    except:
        return -1
nombre = ""
while nombre != "salir":
    nombre = input('Escriba el nombre del producto: ')
    if nombre.lower()=="salir":break
    respuesta = buscarProducto(nombre)
    if respuesta == 0:
        print("No se localizó el producto llamado " + nombre)
    elif respuesta == -1:
        print('error en la conexion')
    else:
        print('El precio es: ' + respuesta)
print("Gracias por usar el sistema amiko")