# se importa la libreria tkinter cn todas sus funciones 
from cgitb import text
import fractions
from tkinter import*

#-----------------
#ventana principal
#---------------

# se declara una variable llamada ventana principal y que adquiere las caracteristicas
ventana_principal= Tk()

# titulo de la ventana
ventana_principal.title("Nayarith zambrano gomez")

# establecer tamaño a la ventana
ventana_principal.geometry("800x500")
#icono de la ventana principal
#ventana.principal

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana principal
ventana_principal.config(bg="goldenrod1")

#---------------
# frame entrada
#---------------
frame_entrada = Frame(ventana_principal )
frame_entrada.config (bg="dark green",width=80, height=480)
frame_entrada.place(x=10,y=10)


#--------------------
# frame operaciones
#--------------------
frame_operaciones = Frame(ventana_principal )
frame_operaciones.config (bg="dark orange",width=80, height=480)
frame_operaciones.place(x=83,y=10)


#--------------------
# frame resultados
#--------------------
frame_resultados = Frame(ventana_principal )
frame_resultados.config (bg="maroon",width=615, height=480)
frame_resultados.place(x=175,y=10)



# se ejecuta el metodo mainpool() de la clase tk() a traves  de la instancia ventana_principal. este metodo despliega  una ventana simple  en pantalla y queda a la espera de lo que el usuario  haga (click en boton, escribir, etc).  Cada accion del usuario se conoce como un evento.  El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()                                                                                                     