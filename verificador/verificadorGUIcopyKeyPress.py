from tkinter import *
from PIL import Image, ImageTk
import apiBuscar



codigo = ''
try:
    def on_key_pressed(event):
        global codigo
        if event.keysym == 'Return':
            llamadaDatos(codigo)
            codigo = ''
        else:
            codigo += event.keysym

except:
    print("No pudo generar el evento")
def llamadaDatos(codigo):
    try:
        respuesta = apiBuscar.buscarProducto(codigo)
        if respuesta == 0:
            resultado_label.config(text="No se localizó el código del producto " + codigo)
        elif respuesta == -1:
            resultado_label.config(text='Error en la conexión')
        else:
            resultado_label.config(text='Nombre del Producto: ' + str(respuesta[1]) + "\n" + 'Precio del Producto: ' + str(respuesta[2]))
            if hasattr(llamadaDatos, 'imagen_label'):#La función hasattr(objeto, atributo) es una función incorporada de Python que se utiliza para verificar si un objeto tiene un atributo específico. Toma dos argumentos:
                llamadaDatos.imagen_label.destroy()  # Elimina el widget Label si existe
            
            img = Image.open(respuesta[3]) #llamamos la imagen. 
            img = img.resize((100, 100))  # Ajusta el tamaño de la imagen si es necesario
            img_tk = ImageTk.PhotoImage(img) #usamos la propiedad para poder cargar el pad de la imagen. 
            imagen_label = Label(ventana, image=img_tk) #colocamos un lable que nos de la imagen. 
            imagen_label.image = img_tk #mostramos la imagen en la ventana con tkner 
            imagen_label.pack()
            #Colocar la imagen
            ventana.update_idletasks()  # Actualizar la ventana antes de colocar la imagen
            #y = (resultado_label.winfo_reqheight() + bottonBuscar.winfo_reqheight() + imagen_label.winfo_reqheight()) +60
            imagen_label.place(x=50,y=50)
            llamadaDatos.imagen_label = imagen_label#guardamos los datos de la imagen. 
           
    except Exception as e:
        resultado_label.config(text='Error: ' + str(e))

ventana = Tk()
ventana.title('Verificador')
ventana['bg'] = '#58d1c5'
#ventana.geometry("{0}x{1}+0+0".format(ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
ventana.state('zoomed')

resultado_label = Label(ventana, text="", font="BOLD")
resultado_label.place(x=10, y=200)

ventana.bind('<Key>', on_key_pressed)
ventana.mainloop()
