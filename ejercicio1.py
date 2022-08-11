# se importa la libreria tkinter cn todas sus funciones 
from cgitb import text
from tkinter import*

#-----------------
#ventana principal
#---------------

# se declara una variable llamada ventana principal y que adquiere las caracteristicas
ventana_principal= Tk()

# titulo de la ventana
ventana_principal.title("Nayarith zambrano gomez")

# establecer tamaño a la ventana
ventana_principal.geometry("800x300")



# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana principal
ventana_principal.config(bg="cadetblue1")


# agregamos un widget a la ventana principal
letrero=Label(text="\n\nsistemas, la mejor!!\n\n", bg="cadetblue1")
letrero.pack()

# agregamos un widget a la ventana principal
letrero2=Label(text="\n\nNayarith zambrano!!\n\n", bg="cadetblue1")
letrero2.pack()

# agregamos un widget a la ventana principal
letrero3=Label(text="\n\ncolegio san jose de guanenta!!\n\n", bg="cadetblue1")
letrero3.pack()

# se ejecuta el metodo mainpool() de la clase tk() a traves  de la instancia ventana_principal. este metodo despliega  una ventana simple  en pantalla y queda a la espera de lo que el usuario  haga (click en boton, escribir, etc).  Cada accion del usuario se conoce como un evento.  El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop() 