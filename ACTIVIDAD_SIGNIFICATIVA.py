#importacion de librerias
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
# Función para enmascarar fecha
def enmascarar_fecha(texto):
   limpio = "".join(filter(str.isdigit, texto))
   formato_final = ""
   if len(limpio) > 8:
       limpio = limpio[:8]
   if len(limpio) > 4:
       formato_final = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
   elif len(limpio) > 2:
       formato_final = f"{limpio[:2]}-{limpio[2:]}"
   else:
       formato_final = limpio
   if fechaP.get() != formato_final:
       fechaP.delete(0, tk.END)
       fechaP.insert(0, formato_final)
   if len(fechaP.get()) == 10:
       fecha_actual = datetime.now().date()
       fecha_nacimiento = datetime.strptime(fechaP.get(), "%d-%m-%Y").date()
       edad = fecha_actual.year - fecha_nacimiento.year
       edadVar.set(edad)
   else:
       edadVar.set("")
   return True
# Guardar/Cargar Pacientes
def guardar_pacientes():
   with open("paciente.txt", "w", encoding="utf-8") as archivo:
       for paciente in paciente_data:
           archivo.write(f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|{paciente['Edad']}|"
                         f"{paciente['Genero']}|{paciente['Grupo Sanguineo']}|"
                         f"{paciente['Tipo de Seguro']}|{paciente['Centro Medico']}|{paciente['Peso']}\n")
def cargar_desde_archivo_pacientes():
   try:
       with open("paciente.txt", "r", encoding="utf-8") as archivo:
           paciente_data.clear()
           for linea in archivo:
               datos = linea.strip().split("|")
               if len(datos) == 8:  # incluye peso
                   paciente = {
                       "Nombre": datos[0],
                       "Fecha de Nacimiento": datos[1],
                       "Edad": datos[2],
                       "Genero": datos[3],
                       "Grupo Sanguineo": datos[4],
                       "Tipo de Seguro": datos[5],
                       "Centro Medico": datos[6],
                       "Peso": datos[7]
                   }
                   paciente_data.append(paciente)
       cargar_treeview()
   except FileNotFoundError:
       open("paciente.txt", "w", encoding="utf-8").close()
def eliminarpaciente():
   seleccionado = treeview.selection()
   if seleccionado:
       indice = int(seleccionado[0])
       id_item = seleccionado[0]
       if messagebox.askyesno("Eliminar Paciente", f"¿Estas seguro de eliminar al paciente {treeview.item(id_item, 'values')[0]}?"):
           del paciente_data[indice]
           guardar_pacientes()
           cargar_treeview()
           messagebox.showinfo("Eliminar Paciente", "Paciente eliminado exitosamente")
   else:
       messagebox.showwarning("Eliminar Paciente", "No se ha seleccionado ningún paciente.")
# Lista de pacientes
paciente_data = []
def registrarPaciente():
   paciente = {
       "Nombre": nombreP.get(),
       "Fecha de Nacimiento": fechaP.get(),
       "Edad": edadVar.get(),
       "Genero": genero.get(),
       "Grupo Sanguineo": entryGrupoSanguineo.get(),
       "Tipo de Seguro": tipo_seguro.get(),
       "Centro Medico": centro_medico.get(),
       "Peso": entryPeso.get()
   }
   paciente_data.append(paciente)
   guardar_pacientes()
   cargar_treeview()
def cargar_treeview():
   for paciente in treeview.get_children():
       treeview.delete(paciente)
   for i, item in enumerate(paciente_data):
       treeview.insert(
           "", "end", iid=str(i),
           values=(
               item["Nombre"],
               item["Fecha de Nacimiento"],
               item["Edad"],
               item["Genero"],
               item["Grupo Sanguineo"],
               item["Tipo de Seguro"],
               item["Centro Medico"],
               item["Peso"]
           )
       )
# Ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Registro de Pacientes")
ventana_principal.geometry("950x700")
# Nombre
labelNombre = tk.Label(ventana_principal, text="Nombre Completo:")
labelNombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP = tk.Entry(ventana_principal)
nombreP.grid(row=0, column=1, sticky="w", pady=5, padx=5)
# Fecha de nacimiento
labelNacimiento = tk.Label(ventana_principal, text="Fecha de Nacimiento:")
labelNacimiento.grid(row=1, column=0, sticky="w", pady=5, padx=5)
validacion_fecha = ventana_principal.register(enmascarar_fecha)
fechaP = ttk.Entry(ventana_principal, validate="key", validatecommand=(validacion_fecha, "%P"))
fechaP.grid(row=1, column=1, sticky="w", pady=5, padx=5)
# Edad
labelEdad = tk.Label(ventana_principal, text="Edad:")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadVar = tk.StringVar()
edadP = tk.Entry(ventana_principal, textvariable=edadVar, state="readonly")
edadP.grid(row=2, column=1, sticky="w", pady=5, padx=5)
# Genero
labelGenero = tk.Label(ventana_principal, text="Genero:")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero = tk.StringVar()
genero.set("Masculino")
radioMasculino = ttk.Radiobutton(ventana_principal, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino = ttk.Radiobutton(ventana_principal, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)
# Grupo sanguineo
labelGrupoSanguineo = tk.Label(ventana_principal, text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=5, column=0, sticky="w", padx=5, pady=5)
entryGrupoSanguineo = tk.Entry(ventana_principal)
entryGrupoSanguineo.grid(row=5, column=1, sticky="w", padx=5, pady=5)
# Tipo de seguro
labelTipoSeguro = tk.Label(ventana_principal, text="Tipo de seguro:")
labelTipoSeguro.grid(row=6, column=0, sticky="w", pady=5, padx=5)
tipo_seguro = tk.StringVar()
tipo_seguro.set("Publico")
comboTipoSeguro = ttk.Combobox(ventana_principal, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6, column=1, sticky="w", pady=5, padx=5)
# Centro medico
labelCentroMedico = tk.Label(ventana_principal, text="Centro de salud:")
labelCentroMedico.grid(row=7, column=0, sticky="w", padx=5, pady=5)
centro_medico = tk.StringVar()
centro_medico.set("Hospital Central")
comboCentroMedico = ttk.Combobox(ventana_principal, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=7, column=1, sticky="w", padx=5, pady=5)
# Peso
labelPeso = tk.Label(ventana_principal, text="Peso (kg):")
labelPeso.grid(row=8, column=0, sticky="w", padx=5, pady=5)
entryPeso = tk.Entry(ventana_principal)
entryPeso.grid(row=8, column=1, sticky="w", padx=5, pady=5)
# Botones pacientes
btn_frame = tk.Frame(ventana_principal)
btn_frame.grid(row=18, column=0, columnspan=2, pady=5, sticky="w")
btn_registrar = tk.Button(btn_frame, text="Registrar", bg="green", command=registrarPaciente)
btn_registrar.grid(row=0, column=0, padx=5)
btn_eliminar = tk.Button(btn_frame, text="Eliminar", bg="red", command=eliminarpaciente)
btn_eliminar.grid(row=0, column=1, padx=5)
# Treeview pacientes
treeview = ttk.Treeview(ventana_principal, columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS", "TipoS", "CentroM", "Peso"), show="headings")
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Medico")
treeview.heading("Peso", text="Peso (kg)")
treeview.column("Nombre", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=70, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)
treeview.column("Peso", width=70, anchor="center")
treeview.grid(row=10, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
scroll_y = ttk.Scrollbar(ventana_principal, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=10, column=2, sticky="ns")
# Cargar datos al iniciar
cargar_desde_archivo_pacientes()
ventana_principal.mainloop()