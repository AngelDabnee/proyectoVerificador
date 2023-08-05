import mysql.connector
try:
    conexionpyhton = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'pos') 
    resultado = conexionpyhton.cursor()
    nombre = ""
    while nombre != "salir":
        nombre = input('Escriba el nombre del producto: ')
        if nombre.lower()=="salir":
            break
        resultado.execute("SELECT * FROM productos WHERE nombre = '"+nombre+"'")
        registros = resultado.fetchone()
        if registros:
                print("Precio: " + str(registros[2]) +  "\nCon Código de Barra: " + str(registros[0]) )
        else:
            print("No encontré el producto ")
except:
    print('error en la conexion')
print("Gracias por usar el sistema amiko")