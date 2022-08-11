from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage 
import pygame
import random
import mutagen 
#from mutagen.mp3 import MP3

#pygame.mixer.pre_init(frequency=44100)
pygame.mixer.init()
pygame.mixer.init(frequency=44100)
cancion_actual =""
direcion = ""

def abrir_archivo():
    global direcion, pos, n, cancion_actual
    pos = 0 
    n = 0 
    direcion = filedialog.askopenfilenames(initialdir ="/",
                                        title="Escoger la cancion(es)",
                                    filetype=(("mp3 files", "*.mp3*"),("All file", "*-*")))
n = len(direcion)
cancion_actual = direcion[pos]

nombre_cancion = cancion_actual.split("/")
nombre_cancion = nombre_cancion[-1]

lista = []
for i in range(50,200,10):
    lista.append(i)
    