import mysql.connector
def buscarProducto(producto):
    try:
        conexionpyhton = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'pos') 
        resultado = conexionpyhton.cursor()
        resultado.execute("SELECT * FROM productos WHERE codigo = '"+producto+"'")
        registros = resultado.fetchone()
        if registros:
            #Regresamos el precio del producto
            #return str(registros[2])
            return registros
        else:
            #Se regresa 0 cuando no se encuentra el producto
            return 0

    except:
        #Se regresa -1 cuando hay un error en la conexión. 
        return -1