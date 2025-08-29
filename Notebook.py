#importacion de librrias
import tkinter as tk
from tkinter import ttk, messagebox
#crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y doctores")
ventana_principal.geometry("400x600")

#crear contenedor Notebook (pestañas)
pestañas=ttk.Notebook(ventana_principal)

#PACIENTES
#crear frames (uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)

#agregarpestañas al notebook
pestañas.add(frame_pacientes, text="Pacientes")

#mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")

#DOCTORES
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores, text="Doctores")
pestañas.pack(expand=True, fill="both")

#nombre
labelnombre=tk.Label(frame_pacientes, text="Nombre Completo: ")
labelnombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", pady=5, padx=5)

#fecha de nacimiento
labelfechaN=tk.Label(frame_pacientes, text="Fecha de Nacimiento: ")
labelfechaN.grid(row=1, column=0, sticky="w", pady=5, padx=5)
fechaentry=tk.Entry(frame_pacientes)
fechaentry.grid(row=1, column=1, sticky="w", pady=5, padx=5 )

#edad (readonly)
labelEdad=tk.Label(frame_pacientes, text="Edad: ")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadentry=tk.Entry(frame_pacientes, state="readonly")
edadentry.grid(row=2, column=1, sticky="w", pady=5, padx=5 )

#genero
labelgenero=tk.Label(frame_pacientes, text="Genero: ")
labelgenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino") #valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk. Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)

#grupo sanguineo
labelgruposanguineo=tk.Label(frame_pacientes, text="Grupo Sanguineo: ")
labelgruposanguineo.grid(row=5, column=0, sticky="w", pady=5, padx=5)
entrygruposanguineo=tk.Entry(frame_pacientes)
entrygruposanguineo.grid(row=5, column=1, sticky="w", pady=5, padx=5)

#tipo de seguro
labeltiposanguineo=tk.Label(frame_pacientes, text="Tipo de seguro: ")
labeltiposanguineo.grid(row=6, column=0, sticky="w", pady=5, padx=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")  #valor por defecto
combotiposeguro=ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
combotiposeguro.grid(row=6, column=1, sticky="w", pady=5, padx=5)

#centro medico
labelcentromedico=tk.Label(frame_pacientes, text="Centro de salud: ")
labelcentromedico.grid(row=7, column=0, sticky="w", pady=5, padx=5)
centromedico=tk.StringVar()
centromedico.set("Hospital Central") #valor por defecto
combocentromedico=ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centromedico)
combocentromedico.grid(row=7, column=1, sticky="w", pady=5, padx=5)

ventana_principal.mainloop()