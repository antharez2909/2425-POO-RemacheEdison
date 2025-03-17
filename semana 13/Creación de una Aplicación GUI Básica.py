import tkinter as tk
from tkinter import messagebox


# Función para agregar una tarea
def agregar_tarea():
    tarea = campo_texto.get()  # Obtener el texto del campo de entrada
    if tarea:  # Verificar que el campo no esté vacío
        lista_tareas.insert(tk.END, tarea)  # Agregar la tarea a la lista
        campo_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa una tarea antes de agregar.")

# Función para marcar una tarea como completada
def completar_tarea():
    try:
        seleccionado = lista_tareas.curselection()  # Obtener el índice de la tarea seleccionada
        if seleccionado:
            tarea = lista_tareas.get(seleccionado)  # Obtener el texto de la tarea
            lista_tareas.delete(seleccionado)  # Eliminar la tarea de la lista
            lista_tareas.insert(tk.END, f"✓ {tarea}")  # Agregar la tarea marcada como completada
    except:
        messagebox.showwarning("Error", "Selecciona una tarea para completar.")

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        seleccionado = lista_tareas.curselection()  # Obtener el índice de la tarea seleccionada
        if seleccionado:
            lista_tareas.delete(seleccionado)  # Eliminar la tarea de la lista
    except:
        messagebox.showwarning("Error", "Selecciona una tarea para eliminar.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("To-Do List")  # Título de la ventana
ventana.geometry("400x400")  # Tamaño de la ventana

# Crear y colocar los componentes en la ventana
etiqueta = tk.Label(ventana, text="Ingresa una tarea:")  # Etiqueta descriptiva
etiqueta.pack(pady=10)

campo_texto = tk.Entry(ventana, width=40)  # Campo de texto para ingresar tareas
campo_texto.pack(pady=10)

boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)  # Botón para agregar tareas
boton_agregar.pack(pady=5)

boton_completar = tk.Button(ventana, text="Completar Tarea", command=completar_tarea)  # Botón para completar tareas
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)  # Botón para eliminar tareas
boton_eliminar.pack(pady=5)

lista_tareas = tk.Listbox(ventana, width=50, height=15)  # Lista para mostrar las tareas
lista_tareas.pack(pady=20)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
