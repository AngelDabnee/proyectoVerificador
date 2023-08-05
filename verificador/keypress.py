from tkinter import *
from PIL import Image, ImageTk

#propiedades de la ventana. 
ventana = Tk()
ventana.title('Prueba Imagen')
ventana['bg'] = '#58d1c5'
ventana.geometry('500x500')
codigo = ''
try:
    def on_key_pressed(event):
        global codigo
        if event.keysym == 'Return':
            #print(event.keysym)
            print('buscamos algo ' + codigo)
            codigo = ''
        else:
            codigo += event.keysym
    ventana.bind('<Key>',on_key_pressed)
except:
    print("No pudo generar el evento")

ventana.mainloop()
