import tkinter as tk
from tkinter import messagebox
def nuevoDoctor():
    ventanaRegistro = tk.Toplevel(ventanaprincipal)
    ventanaRegistro.title("Registro de Doctor")
    ventanaRegistro.geometry("500x500")
    ventanaRegistro.configure(bg="steelBlue")
 
    # Nombre
    nombreLabel = tk.Label(ventanaRegistro, text="Nombre: ", bg="steelBlue")
    nombreLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entryNombre = tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
 
    # Dirección
    direccionLabel = tk.Label(ventanaRegistro, text="Dirección: ", bg="steelBlue")
    direccionLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entryDireccion = tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
 
    # Teléfono
    telefonoLabel = tk.Label(ventanaRegistro, text="Teléfono: ", bg="steelBlue")
    telefonoLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entryTelefono = tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
 
    # especialidad (RadioButton)
    espLabel = tk.Label(ventanaRegistro, text="Especialidad: ", bg="steelBlue")
    espLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    especialidad = tk.StringVar(value="Pediatria")
    rbpediatria = tk.Radiobutton(ventanaRegistro, text="Pediatria", variable=especialidad, value="Pediatria", bg="steelBlue")
    rbpediatria.grid(row=3, column=1, sticky="w")
    rbcardiologia = tk.Radiobutton(ventanaRegistro, text="Cardiologia", variable=especialidad, value="Cardiologia", bg="steelBlue")
    rbcardiologia.grid(row=4, column=1, sticky="w")
    rbneurologia = tk.Radiobutton(ventanaRegistro, text="Neurologia", variable=especialidad, value="Neurologia", bg="steelBlue")
    rbneurologia.grid(row=5, column=1, sticky="w")
    
    #disponibilidad
    displabel=tk.Label(ventanaRegistro, text="Disponibilidad: ", bg="steelblue")
    displabel.grid(row=6, column=0, padx=10, pady=5, sticky="w")
    mañana=tk.BooleanVar()
    Tarde=tk.BooleanVar()
    noche=tk.BooleanVar()
    cbmañana= tk.Checkbutton(ventanaRegistro,text="Mañana", variable=mañana, bg="steelblue")
    cbmañana.grid(row=6, column=1, sticky="w")
    cbtarde= tk.Checkbutton(ventanaRegistro,text="Tarde", variable=Tarde, bg="steelblue")
    cbtarde.grid(row=7,column=1,sticky="w")
    cbnoche=tk.Checkbutton(ventanaRegistro,text="Noche",variable=noche,bg="steelblue")
    cbnoche.grid(row=8,column=1,sticky="w")
    
    
    # Función para registrar datos
    def registrarDatos():
        disponibilidad=[]
        if mañana.get():
            disponibilidad.append("Mañana")
        if Tarde.get():
            disponibilidad.append("Tarde")
        if noche.get():
            disponibilidad.append("Noche")
        if len(disponibilidad)>0:
            disponibilidadTexto=','.join(disponibilidad)
        else:
            disponibilidadTexto='Ninguna'
        info = (
            f"Nombre: {entryNombre.get()}\n"
            f"Dirección: {entryDireccion.get()}\n"
            f"Teléfono: {entryTelefono.get()}\n"
            f"Especialidad: {especialidad.get()}\n"
            f"Disponibilidad: {disponibilidadTexto}"
            
        )
        messagebox.showinfo("Datos Registrados", info)
        ventanaRegistro.destroy()  # cierra la ventana tras mostrar la info
 
    # Botón para registrar
    botonRegistrar = tk.Button(ventanaRegistro, text="Registrar", command=registrarDatos)
    botonRegistrar.grid(row=14, column=0, columnspan=2, pady=10)
 
def buscarDoctor():
    messagebox.showinfo("Buscar Doctor", "Función para buscar doctor")
 
def eliminarDoctor():
    messagebox.showinfo("Eliminar Doctor", "Función para eliminar doctor")
   
ventanaprincipal = tk.Tk()
ventanaprincipal.title("Sistema de registro de doctores")
ventanaprincipal.geometry("400x400")
ventanaprincipal.configure(bg="skyblue")
 
# barra de menú
barraMenu = tk.Menu(ventanaprincipal)
ventanaprincipal.config(menu=barraMenu)
 
# menú de doctores
menudoctores = tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menudoctores)
menudoctores.add_command(label="Nuevo Doctor", command=nuevoDoctor)
menudoctores.add_command(label="Buscar Doctor", command=buscarDoctor)
menudoctores.add_command(label="Eliminar Doctor", command=eliminarDoctor)
 
ventanaprincipal.mainloop()