import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

def mark_completed():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        if not task.startswith("✔ "):
            listbox.delete(selected)
            listbox.insert(selected, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def close_app():
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x300")

# Campo de entrada y botones
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.bind("<Return>", add_task)

frame_buttons = tk.Frame(root)
frame_buttons.pack()

btn_add = tk.Button(frame_buttons, text="Añadir", command=add_task)
btn_add.pack(side=tk.LEFT, padx=5)

btn_complete = tk.Button(frame_buttons, text="Completar", command=mark_completed)
btn_complete.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(frame_buttons, text="Eliminar", command=delete_task)
btn_delete.pack(side=tk.LEFT, padx=5)

# Lista de tareas
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Configuración de atajos de teclado
root.bind("<c>", mark_completed)
root.bind("<d>", delete_task)
root.bind("<Delete>", delete_task)
root.bind("<Escape>", close_app)

# Iniciar la aplicación
root.mainloop()
