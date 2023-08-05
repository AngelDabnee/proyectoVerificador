from tkinter import *
from PIL import Image, ImageTk

#propiedades de la ventana. 
ventana = Tk()
ventana.title('Prueba Imagen')
ventana['bg'] = '#58d1c5'
ventana.geometry('500x500')


#creamos una variable para la imagen. 
try:
    img = Image.open('../img/productos/caguamaMiler.jpg')
    img = img.resize((500, 500))  # Ajusta el tamaño de la imagen si es necesario
    img_tk = ImageTk.PhotoImage(img)
    resultado_label = Label(ventana, image=img_tk)
    resultado_label.place(x=10, y=200)
except:
    resultado_label = Label(ventana, text='error para todos')
    
resultado_label.pack()
ventana.mainloop()
