import tkinter as tk
import tkinter.ttk as ttk

def create_window():
    window = tk.Tk()
    window.title("Ventana con Tema xpnative")
    
    # Cambiar al tema xpnative
    s = ttk.Style()
    s.theme_use('alt')
    print(s.theme_names())

    # Crear widgets
    ttk.Label(window, text="Etiqueta").pack()
    ttk.Entry(window).pack()
    ttk.Button(window, text="Botón").pack()

    window.mainloop()

create_window()
