import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox

#"crear ventana principal"
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Libro pacientes y doctores")
ventanaPrincipal.geometry("950x900")
#crear contenedores notebook(pestañas)
pestañas=ttk.Notebook(ventanaPrincipal)
#mostrar las pestañas en la ventana
pestañas.pack(expand=True,fill="both")
#_-_-_FRAME DOCTORES-_-_-_
#crear frame doctores
frame_doctores=ttk.Frame(pestañas)
#añadir a la ventana principal 
pestañas.add(frame_doctores,text="Doctores")
#titulo registro doctores
tituloLabelD=tk.Label(frame_doctores,text="Registro Doctores",font=("Candara",18,"bold"))
tituloLabelD.grid(row=0,column=1,padx=10,pady=10)

#funcion guardar archivo 
def guardar_en_archivoDoc():
    with open ("doctores.txt","w",encoding="utf-8")as archivo: 
        for doctor in doctores_data:
            archivo.write(
                f"{doctor['Nombre']}|"
                f"{doctor['Especialidad']}|"
                f"{doctor['Años de Experiencia']}|"
                f"{doctor['Genero']}|"
                f"{doctor['Hospital']}|"
                f"{doctor['Telefono']}\n"
            )

#lista doctores
doctores_data=[]

#funcion doctores
def registrarDoctores ():
    #crear un diccionario con los datos ingresados
    doctor={
        "Nombre": nombreD.get(),
        "Especialidad":tipo_especialidad.get(),
        "Años de Experiencia":spin.get(),
        "Genero":genero.get(),
        "Hospital":hospital.get(),
        "Telefono":telefonoD.get()
    }
    #agregar a la lista
    doctores_data.append(doctor)
    guardar_en_archivoDoc()
    #Cargar el treeview
    cargar_treeview1()

def cargar_treeview1():
    #limpiar el treeview
    for doctor in treeview1.get_children():
        treeview1.delete(doctor)
    #insertar cada paciente
    for i, itemm in enumerate(doctores_data):
        treeview1.insert(
            "","end",iid=str(i),
            values=(
                itemm["Nombre"],
                itemm["Especialidad"],
                itemm["Años de Experiencia"],
                itemm["Genero"],
                itemm["Hospital"],
                itemm["Telefono"]
            )
        )

#CARGAR DESDE ARCHIVO 
def cargar_desde_archivo_doctores():
    try:
        with open("doctores.txt","r",encoding="utf-8") as archivo:
            doctores_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==6:
                    doctor={
                        "Nombre":datos[0],
                        "Especialidad":datos[1],
                        "Años de Experiencia":datos[2],
                        "Genero":datos[3],
                        "Hospital":datos[4],
                        "Telefono":datos[5]
                    }
                    doctores_data.append(doctor)
        cargar_treeview1()
    except FileNotFoundError:
        open("doctores.txt","w",encoding="utf-8").close()

#Funcion para eliminar doctor
def eliminarDoctor():
    seleccionado1=treeview1.selection()
    if seleccionado1:
        indice=int(seleccionado1[0])
        id_item1=seleccionado1[0]
        if messagebox.askyesno("Eliminar Doctor", f"¿Esta seguro de eliminar el doctor '{treeview1.item(id_item1,'values')[0]}'?"):
            del doctores_data[indice]
            guardar_en_archivoDoc() #guardar los cambios en el archivo
            cargar_treeview1()
            messagebox.showinfo("Eliminar Doctor","Doctor eliminado exitosamente.")
    else:
        messagebox.showwarning("Eliminar Doctor","No se ha seleccionado ningun doctor.")
        return

#---------------------------------------------------DOCTORES---------------------------------------------------
#nombre
labelNombreD=tk.Label(frame_doctores,text="Nombre:")
labelNombreD.grid(row=1,column=0,sticky="w",padx=5,pady=5)
nombreD=tk.Entry(frame_doctores)
nombreD.grid(row=1,column=1,padx=5,pady=5,sticky="w")

#especialidad
labelEspecialidad=tk.Label(frame_doctores,text="Especialidad")
labelEspecialidad.grid(row=2,column=0,sticky="w",padx=5,pady=5)
tipo_especialidad=tk.StringVar()
tipo_especialidad.set("Neurología")#valor por defecto
comboEspecialidad=ttk.Combobox(frame_doctores,values=["Neurología","Cardiología","Pediatría","Traumatología"],textvariable=tipo_especialidad)
comboEspecialidad.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#años de experiencia
añosExperienciaLabel=tk.Label(frame_doctores,text="Años de Experiencia:")
añosExperienciaLabel.grid(row=3,column=0,sticky="w",padx=5,pady=5)
spin=tk.Spinbox(frame_doctores,from_=1,to=99)
spin.grid(row=3,column=1,padx=3,pady=3,sticky="w")

#genero
labelGenero=tk.Label(frame_doctores,text="Genero")
labelGenero.grid(row=4,column=0,sticky="w",padx=5,pady=5)
genero=tk.StringVar()
genero.set("Masculino")#valor por defecto
radioMasculino=ttk.Radiobutton(frame_doctores,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=4,column=1,sticky="w",padx=5,pady=5)
radioFemenino=ttk.Radiobutton(frame_doctores,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=5,column=1,padx=5,pady=5,sticky="w")

#hospital
labelHospital=tk.Label(frame_doctores,text="Centro de salud")
labelHospital.grid(row=6,column=0,sticky="w",padx=5,pady=5)
hospital=tk.StringVar()
hospital.set("Hospital Central")#valor por defecto
combohospital=ttk.Combobox(frame_doctores,values=["Hospital Central","Hospital Norte","Clínica Santa Maria", "Clinica Vida"],textvariable=hospital)
combohospital.grid(row=6,column=1,sticky="w",padx=5,pady=5)

#telefono
labelTelefono=tk.Label(frame_doctores,text="Teléfono:")
labelTelefono.grid(row=7,column=0,sticky="w",padx=5,pady=5)
telefonoD=tk.Entry(frame_doctores)
telefonoD.grid(row=7,column=1,padx=5,pady=5,sticky="w")

#botones 
btn_frameD=tk.Frame(frame_doctores)
btn_frameD.grid(row=8,column=0,columnspan=2,padx=5,pady=5,sticky="w")

btn_registrarD=tk.Button(btn_frameD,text="Registrar",command=registrarDoctores)
btn_registrarD.grid(row=8,column=0,padx=5,pady=5)
btn_registrarD.configure(bg="#48FF68",fg="white")

btn_eliminarD=tk.Button(btn_frameD,text="Eliminar",command=eliminarDoctor)
btn_eliminarD.grid(row=8,column=1,padx=5)
btn_eliminarD.configure(bg="#FF0014",fg="white")

#TREEVIEW
treeview1=ttk.Treeview(frame_doctores,columns=("Nombre","Especialidad","Años de Experiencia","Genero","Hospital","Telefono"),show="headings")

treeview1.heading("Nombre",text="Nombre")
treeview1.heading("Especialidad",text="Especialidad")
treeview1.heading("Años de Experiencia",text="Años de Experiencia")
treeview1.heading("Genero", text="Genero")
treeview1.heading("Hospital",text="Hospital")
treeview1.heading("Telefono",text="Teléfono")

treeview1.column("Nombre",width=120)
treeview1.column("Especialidad",width=120)
treeview1.column("Años de Experiencia",width=120,anchor="center")
treeview1.column("Genero",width=80,anchor="center")
treeview1.column("Hospital",width=120,anchor="center")
treeview1.column("Telefono",width=100,anchor="center")

treeview1.grid(row=9,column=0,columnspan=2,pady=10,sticky="nsew")

scroll_y=ttk.Scrollbar(frame_doctores,orient="vertical",command=treeview1.yview)
scroll_y.grid(row=9,column=2,sticky="ns")

#cargar datos desde el archivo al iniciar aplicacion
cargar_desde_archivo_doctores()

ventanaPrincipal.mainloop()