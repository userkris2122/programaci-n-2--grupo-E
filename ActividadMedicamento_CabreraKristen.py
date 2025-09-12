#importación de librerías necesarias
import tkinter as tk
from tkinter import ttk, messagebox

# Función para enmascarar fecha
def formato_fecha_keyrelease(event):
   # Esta función se ejecuta cada vez que el usuario escribe en el campo de fecha
   # Sirve para que la fecha siempre se muestre con el formato dd-mm-aaaa
   s = entry_fecha_var.get()
   digits = ''.join(ch for ch in s if ch.isdigit())[:8]  # solo dígitos, máximo 8 (ddmmaaaa)
   # según la cantidad de dígitos escritos, se agrega el guion en su lugar
   if len(digits) > 4:
       formatted = f"{digits[:2]}-{digits[2:4]}-{digits[4:]}"
   elif len(digits) > 2:
       formatted = f"{digits[:2]}-{digits[2:]}"
   else:
       formatted = digits
   # actualiza el campo si hay diferencia
   if formatted != s:
       entry_fecha_var.set(formatted)
   # coloca el cursor al final del texto
   entry_fecha.icursor(tk.END)

# Funciones de persistencia (guardar/cargar datos en archivo)
# lista global donde se almacenan los medicamentos en memoria
medicamento_data = []
def guardar_medicamentos():
   # Guarda la lista de medicamentos en un archivo de texto (medicamento.txt)
   with open("medicamento.txt", "w", encoding="utf-8") as archivo:
       for med in medicamento_data:
           archivo.write(f"{med['Nombre']}|{med['Presentacion']}|{med['Dosis']}|{med['Fecha']}\n")
def cargar_desde_archivo_medicamentos():
   # Carga los medicamentos desde el archivo a la lista en memoria y los muestra en el Treeview
   try:
       with open("medicamento.txt", "r", encoding="utf-8") as archivo:
           medicamento_data.clear()  # limpiar lista antes de cargar
           for linea in archivo:
               datos = linea.strip().split("|")
               if len(datos) == 4:  # aseguramos que la línea tiene todos los campos
                   medicamento = {
                       "Nombre": datos[0],
                       "Presentacion": datos[1],
                       "Dosis": datos[2],
                       "Fecha": datos[3]
                   }
                   medicamento_data.append(medicamento)
       cargar_treeview()
   except FileNotFoundError:
       # si el archivo no existe, lo crea vacío
       open("medicamento.txt", "w", encoding="utf-8").close()
def registrarMedicamento():
   # Toma los datos del formulario y registra un nuevo medicamento
   nombre = entry_nombre.get().strip()
   presentacion = combo_presentacion.get().strip()
   dosis = entry_dosis.get().strip()
   fecha = entry_fecha_var.get().strip()
   # Validación: no dejar campos vacíos
   if not nombre or not presentacion or not dosis or not fecha:
       messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")
       return
   # Guardamos el medicamento en memoria
   medicamento = {
       "Nombre": nombre,
       "Presentacion": presentacion,
       "Dosis": dosis,
       "Fecha": fecha
   }
   medicamento_data.append(medicamento)
   guardar_medicamentos()   # guardamos también en archivo
   cargar_treeview()        # actualizamos la tabla (Treeview)
   # Limpiar formulario después de registrar
   entry_nombre.delete(0, tk.END)
   combo_presentacion.set("")
   entry_dosis.delete(0, tk.END)
   entry_fecha_var.set("")
def eliminarMedicamento():
   # Elimina el medicamento seleccionado en el Treeview y lo borra del archivo
   seleccionado = treeview.selection()  # obtiene la selección en la tabla
   if seleccionado:
       indice = int(seleccionado[0])  # el índice corresponde al medicamento en la lista
       id_item = seleccionado[0]
       # confirmación antes de eliminar
       if messagebox.askyesno("Eliminar Medicamento",
                              f"¿Seguro que deseas eliminar {treeview.item(id_item, 'values')[0]}?"):
           del medicamento_data[indice]  # eliminar de la lista en memoria
           guardar_medicamentos()        # actualizar archivo
           cargar_treeview()             # refrescar tabla
           messagebox.showinfo("Eliminado", "Medicamento eliminado exitosamente")
   else:
       messagebox.showwarning("Eliminar Medicamento", "No se ha seleccionado ningún medicamento.")
def cargar_treeview():
   # Actualiza el Treeview con todos los medicamentos que hay en memoria
   # primero vaciamos el Treeview
   for item in treeview.get_children():
       treeview.delete(item)
   # luego insertamos los datos de la lista global
   for i, med in enumerate(medicamento_data):
       treeview.insert("", "end", iid=str(i),
                       values=(med["Nombre"], med["Presentacion"], med["Dosis"], med["Fecha"]))

# Interfaz gráfica (Tkinter)
ventana = tk.Tk()
ventana.title("Gestión de Medicamentos")
ventana.geometry("800x520")
ventana.minsize(700, 450)
# Frame del formulario (donde se ponen los inputs)
form_frame = ttk.Frame(ventana, padding=(12, 10))
form_frame.grid(row=0, column=0, sticky="ew")
form_frame.columnconfigure(0, weight=0)
form_frame.columnconfigure(1, weight=1)
# Campo Nombre
lbl_nombre = ttk.Label(form_frame, text="Nombre:")
lbl_nombre.grid(row=0, column=0, sticky="w", padx=6, pady=6)
entry_nombre = ttk.Entry(form_frame)
entry_nombre.grid(row=0, column=1, sticky="ew", padx=6, pady=6)
# Campo Presentación (desplegable)
lbl_present = ttk.Label(form_frame, text="Presentación:")
lbl_present.grid(row=1, column=0, sticky="w", padx=6, pady=6)
combo_presentacion = ttk.Combobox(form_frame, values=["Tabletas", "Jarabe", "Inyectable", "Cápsulas", "Otro"])
combo_presentacion.grid(row=1, column=1, sticky="ew", padx=6, pady=6)
# Campo Dosis
lbl_dosis = ttk.Label(form_frame, text="Dosis:")
lbl_dosis.grid(row=2, column=0, sticky="w", padx=6, pady=6)
entry_dosis = ttk.Entry(form_frame)
entry_dosis.grid(row=2, column=1, sticky="w", padx=6, pady=6)
# Campo Fecha de vencimiento con enmascarado
lbl_fecha = ttk.Label(form_frame, text="Fecha Vencimiento (dd-mm-yyyy):")
lbl_fecha.grid(row=3, column=0, sticky="w", padx=6, pady=6)
entry_fecha_var = tk.StringVar()
entry_fecha = ttk.Entry(form_frame, textvariable=entry_fecha_var)
entry_fecha.grid(row=3, column=1, sticky="w", padx=6, pady=6)
entry_fecha.bind("<KeyRelease>", formato_fecha_keyrelease)  # aplica la función de formato
# Botones
btn_frame = ttk.Frame(form_frame)
btn_frame.grid(row=4, column=0, columnspan=2, sticky="ew", padx=6, pady=(10, 2))
btn_frame.columnconfigure((0, 1), weight=1)
btn_registrar = ttk.Button(btn_frame, text="Registrar", command=registrarMedicamento)
btn_registrar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
btn_eliminar = ttk.Button(btn_frame, text="Eliminar", command=eliminarMedicamento)
btn_eliminar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
# Frame de la lista (tabla con los medicamentos)
list_frame = ttk.Frame(ventana, padding=(12, 6))
list_frame.grid(row=1, column=0, sticky="nsew")
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)
list_frame.rowconfigure(0, weight=1)
list_frame.columnconfigure(0, weight=1)
# Tabla (Treeview) para mostrar medicamentos
treeview = ttk.Treeview(list_frame,
                       columns=("nombre", "presentacion", "dosis", "fecha"),
                       show="headings")
treeview.grid(row=0, column=0, sticky="nsew")
treeview.heading("nombre", text="Nombre")
treeview.heading("presentacion", text="Presentación")
treeview.heading("dosis", text="Dosis")
treeview.heading("fecha", text="Fecha Vencimiento")
# ajustar tamaño de columnas
treeview.column("nombre", width=220)
treeview.column("presentacion", width=120, anchor="center")
treeview.column("dosis", width=100, anchor="center")
treeview.column("fecha", width=120, anchor="center")
# Scrollbar vertical para la tabla
scroll_y = ttk.Scrollbar(list_frame, orient="vertical", command=treeview.yview)
scroll_y.grid(row=0, column=1, sticky="ns")
treeview.configure(yscrollcommand=scroll_y.set)

# Cargar datos al iniciar
cargar_desde_archivo_medicamentos()
# Ejecutar la ventana principal
ventana.mainloop()