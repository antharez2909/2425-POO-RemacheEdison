import tkinter as tk
from tkinter import messagebox


# Funciones para manejar las acciones del usuario
def añadir_tarea():
    """Añade una nueva tarea a la lista desde el campo de entrada."""
    tarea = entrada.get().strip()
    if not tarea:
        messagebox.showerror("Error", "La tarea no puede estar vacía.")
        return
    # Insertar tarea en la Listbox con fondo blanco (no completada)
    lista_tareas.insert(tk.END, tarea)
    lista_tareas.itemconfig(lista_tareas.size() - 1, bg='white')
    entrada.delete(0, tk.END)  # Limpiar campo de entrada


def marcar_completada():
    """Cambia el estado visual de la tarea seleccionada a completada/no completada."""
    try:
        indice = lista_tareas.curselection()[0]
    except IndexError:
        messagebox.showerror("Error", "Selecciona una tarea.")
        return

    # Obtener color actual y alternar entre estados
    color_actual = lista_tareas.itemcget(indice, 'bg')
    nuevo_color = 'light green' if color_actual == 'white' else 'white'
    lista_tareas.itemconfig(indice, bg=nuevo_color)


def eliminar_tarea():
    """Elimina la tarea seleccionada de la lista."""
    try:
        indice = lista_tareas.curselection()[0]
    except IndexError:
        messagebox.showerror("Error", "Selecciona una tarea para eliminar.")
        return
    lista_tareas.delete(indice)


# Configuración inicial de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Campo de entrada para nuevas tareas
entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=10)
entrada.bind('<Return>', lambda evento: añadir_tarea())  # Enter para añadir

# Marco para organizar los botones
marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=5)

# Botones de acciones
boton_añadir = tk.Button(marco_botones, text="Añadir Tarea", command=añadir_tarea)
boton_marcar = tk.Button(marco_botones, text="Marcar Completada", command=marcar_completada)
boton_eliminar = tk.Button(marco_botones, text="Eliminar Tarea", command=eliminar_tarea)

boton_añadir.pack(side=tk.LEFT, padx=5)
boton_marcar.pack(side=tk.LEFT, padx=5)
boton_eliminar.pack(side=tk.LEFT, padx=5)

# Componente Listbox para mostrar las tareas
lista_tareas = tk.Listbox(ventana, width=60, selectmode=tk.BROWSE)
lista_tareas.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Evento de doble clic para marcar como completada
lista_tareas.bind('<Double-Button-1>', lambda evento: marcar_completada())

# Iniciar la aplicación
ventana.mainloop()