import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Requiere instalación: pip install tkcalendar


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Configurar frames para organización
        self.list_frame = ttk.Frame(root)
        self.list_frame.pack(pady=10, padx=10, fill='both', expand=True)

        self.input_frame = ttk.Frame(root)
        self.input_frame.pack(pady=5, fill='x', padx=10)

        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=5, fill='x', padx=10)

        # Configurar TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.list_frame, columns=('Fecha', 'Hora', 'Descripción'), show='headings')
        self.tree.heading('Fecha', text='Fecha')
        self.tree.heading('Hora', text='Hora')
        self.tree.heading('Descripción', text='Descripción')
        self.tree.pack(side='left', fill='both', expand=True)

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(self.list_frame, orient='vertical', command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Campos de entrada
        ttk.Label(self.input_frame, text="Fecha:").grid(row=0, column=0, padx=5)
        self.date_entry = DateEntry(self.input_frame, date_pattern='dd/mm/y')
        self.date_entry.grid(row=0, column=1, padx=5)

        ttk.Label(self.input_frame, text="Hora:").grid(row=0, column=2, padx=5)
        self.time_entry = ttk.Entry(self.input_frame)
        self.time_entry.grid(row=0, column=3, padx=5)
        self.time_entry.insert(0, "HH:MM")  # Sugerencia de formato

        ttk.Label(self.input_frame, text="Descripción:").grid(row=0, column=4, padx=5)
        self.desc_entry = ttk.Entry(self.input_frame, width=30)
        self.desc_entry.grid(row=0, column=5, padx=5)

        # Botones
        self.add_btn = ttk.Button(self.button_frame, text="Agregar Evento", command=self.agregar_evento)
        self.add_btn.pack(side='left', padx=5)

        self.del_btn = ttk.Button(self.button_frame, text="Eliminar Evento", command=self.eliminar_evento)
        self.del_btn.pack(side='left', padx=5)

        self.exit_btn = ttk.Button(self.button_frame, text="Salir", command=self.root.quit)
        self.exit_btn.pack(side='right', padx=5)

    def agregar_evento(self):
        # Obtener datos de los campos
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        desc = self.desc_entry.get().strip()

        # Validar campos obligatorios
        if not fecha or not hora or not desc:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        # Insertar en el TreeView
        self.tree.insert('', 'end', values=(fecha, hora, desc))

        # Limpiar campos
        self.time_entry.delete(0, 'end')
        self.desc_entry.delete(0, 'end')

    def eliminar_evento(self):
        # Obtener elemento seleccionado
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Información", "Seleccione un evento para eliminar")
            return

        # Diálogo de confirmación (opcional)
        if messagebox.askyesno("Confirmar", "¿Eliminar el evento seleccionado?"):
            self.tree.delete(seleccionado)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()