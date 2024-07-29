# Interfaz.py
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import sys
from PDF_funciones import *
from DOCX_funciones import *

# Pedazo de codigo sacado de stackoverflow, solo asi pude exportar el fondo y el icono cuando cree el .exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
###--------------------------------------------------------###

def mostrar_combinador_PDF():
    for widget in window.winfo_children():
        widget.destroy()
    frame_combinador_PDF()

def mostrar_convertidor_DOC():
    for widget in window.winfo_children():
        widget.destroy()
    frame_convertidor_DOC()

    
def frame_combinador_PDF():
    window.title("Combinar PDFs")
    
    background_label = tk.Label(window, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    label_titulo_PDF = tk.Label(window, text="Seleccione los PDF a combinar", font=("Arial Black", 16), fg="tomato", bg="snow")
    label_titulo_PDF.place(relx=0.24, rely=0.15)
    
    frame_PDF = tk.Frame(window, bg='lightgrey', bd=5)
    frame_PDF.place(relx=0.5, rely=0.25, relwidth=0.65, relheight=0.5, anchor='n')
    
    labels_PDF = ["PDF Base", "PDF #2", "PDF #3", "PDF #4", "PDF #5"]
    entries = []
    acumula_PDF = [""] * 5
    
    for i in range(5):
        label = tk.Label(frame_PDF, text=labels_PDF[i], bg='gold' if i == 0 else 'lightgrey')
        label.grid(row=i, column=0, padx=10, pady=5)

        entry_campoentrada_PDF = tk.Entry(frame_PDF, width=35, state='readonly')
        entry_campoentrada_PDF.grid(row=i, column=1, padx=1, pady=5)
        entries.append(entry_campoentrada_PDF)

        Button_seleccionar_PDF = tk.Button(frame_PDF, text="Seleccionar", command=lambda e=entry_campoentrada_PDF, idx=i: seleccionar_PDF(e, idx, acumula_PDF))
        Button_seleccionar_PDF.grid(row=i, column=2, padx=10, pady=5)

        button_borrar_PDF = tk.Button(frame_PDF, text="X", fg="red", command=lambda e=entry_campoentrada_PDF, idx=i: borrar_PDF(e, idx, acumula_PDF))
        button_borrar_PDF.grid(row=i, column=3, padx=5, pady=5)
        
    button_guardar_PDF = tk.Button(window, text="Guardar", command=lambda: guardar_PDF_combinado(acumula_PDF), width=10, height=2, font=("Helvetica", 10))
    button_guardar_PDF.place(relx=0.5, rely=0.77, anchor='n')
    
    label_copyright = tk.Label(window, text="© 2024 Gabriel", font=("Arial", 8), fg="white", bg="black")
    label_copyright.place(relx=0.02, rely=0.95)
    
    button_cambiar_ventana_DOC = tk.Button(window, text="Convertir DOC a PDF", command=mostrar_convertidor_DOC)
    button_cambiar_ventana_DOC.place(relx=0.02, rely=0.02)
    

def frame_convertidor_DOC():
    window.title("Convertir DOC a PDF")

    background_label = tk.Label(window, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
    
    label_titulo_DOC1 = tk.Label(window, text="Convertir de DOC a PDF", font=("Arial Black", 16), fg="tomato", bg="snow")
    label_titulo_DOC1.place(relx=0.31, rely=0.15)
    
    label_titulo_DOC2 = tk.Label(window, text="Convertir de PDF a DOC", font=("Arial Black", 16), fg="tomato", bg="snow")
    label_titulo_DOC2.place(relx=0.31, rely=0.57)

    frame_DOC = tk.Frame(window, bg='lightgrey', bd=5)
    frame_DOC.place(relx=0.5, rely=0.25, relwidth=0.65, relheight=0.15, anchor='n')
    
    frame_PDF = tk.Frame(window, bg='lightgrey', bd=5)
    frame_PDF.place(relx=0.5, rely=0.67, relwidth=0.65, relheight=0.15, anchor='n')

    label_DOC = tk.Label(frame_DOC, text="Documento .DOC:", bg='gold')
    label_DOC.grid(row=0, column=0, padx=10, pady=15)

    entry_campoentrada_DOC = tk.Entry(frame_DOC, width=30, state='readonly')
    entry_campoentrada_DOC.grid(row=0, column=1, padx=10, pady=5)   

    button_seleccionar_DOC = tk.Button(frame_DOC, text="Seleccionar", command=lambda: seleccionar_DOC(entry_campoentrada_DOC))
    button_seleccionar_DOC.grid(row=0, column=2, padx=10, pady=5)
    
    button_borrar_DOC = tk.Button(frame_DOC, text="X", fg="red", command=lambda: borrar_DOC(entry_campoentrada_DOC))
    button_borrar_DOC.grid(row=0, column=3, padx=5, pady=5)

    button_convertir_DOC = tk.Button(window, text="Convertir", command=guardar_DOC_como_PDF, width=10, height=2, font=("Helvetica", 10))
    button_convertir_DOC.place(relx=0.5, rely=0.42, anchor='n')


    label_PDF = tk.Label(frame_PDF, text="Documento .PDF:", bg='gold')
    label_PDF.grid(row=0, column=0, padx=10, pady=15)
    
    entry_campoentrada_PDF = tk.Entry(frame_PDF, width=30, state='readonly')
    entry_campoentrada_PDF.grid(row=0, column=1, padx=10, pady=5)   

    button_seleccionar_PDF = tk.Button(frame_PDF, text="Seleccionar", command=lambda: seleccionar_PDF_De_DOCX(entry_campoentrada_PDF))
    button_seleccionar_PDF.grid(row=0, column=2, padx=10, pady=5)
    
    button_borrar_PDF = tk.Button(frame_PDF, text="X", fg="red", command=lambda: borrar_PDF_De_DOCX(entry_campoentrada_PDF))
    button_borrar_PDF.grid(row=0, column=3, padx=5, pady=5)

    button_convertir_PDF = tk.Button(window, text="Convertir", command=guardar_PDF_como_DOC, width=10, height=2, font=("Helvetica", 10))
    button_convertir_PDF.place(relx=0.5, rely=0.84, anchor='n')
    
    label_copyright = tk.Label(window, text="© 2024 Gabriel", font=("Arial", 8), fg="white", bg="black")
    label_copyright.place(relx=0.02, rely=0.95)

    button_cambiar_ventana_PDF = tk.Button(window, text="Combinar PDFs", command=mostrar_combinador_PDF, )
    button_cambiar_ventana_PDF.place(relx=0.02, rely=0.02)
    borrar_DOC(entry_campoentrada_DOC)
    borrar_PDF(entry_campoentrada_PDF)


window = tk.Tk()
window.geometry("700x400")
window.resizable(False, False)

icono = resource_path('icon.ico')
window.iconbitmap(icono)

background_path = resource_path('background.jpg')
background_image = Image.open(background_path)
background_image = background_image.resize((700, 400), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

mostrar_combinador_PDF()
window.mainloop()
