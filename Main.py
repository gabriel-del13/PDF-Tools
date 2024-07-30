# Interfaz.py
import tkinter as tk
import os
import sys
from PIL import Image, ImageTk
from PDF_funciones import *
from DOCX_funciones import *
from IMG_funciones import *

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
    
def mostrar_convertidor_IMG():
    for widget in window.winfo_children():
        widget.destroy()
    frame_convertidor_IMG()

  
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

        entry_campoentrada_PDF = tk.Entry(frame_PDF, width=40, state='readonly')
        entry_campoentrada_PDF.grid(row=i, column=1, padx=1, pady=5)
        entries.append(entry_campoentrada_PDF)

        Button_seleccionar_PDF = tk.Button(frame_PDF, text="Seleccionar", command=lambda e=entry_campoentrada_PDF, idx=i: seleccionar_PDF(e, idx, acumula_PDF))
        Button_seleccionar_PDF.grid(row=i, column=2, padx=10, pady=5)

        button_borrar_PDF = tk.Button(frame_PDF, text="X", relief="flat", bg="#f44336", fg="white", command=lambda e=entry_campoentrada_PDF, idx=i: borrar_PDF(e, idx, acumula_PDF))
        button_borrar_PDF.grid(row=i, column=3, padx=5, pady=5)
        
    button_guardar_PDF = tk.Button(window, text="Guardar", command=lambda: guardar_PDF_combinado(acumula_PDF), bg="#0df846", fg="black", width=10, height=2, font=("Helvetica", 10))
    button_guardar_PDF.bind("<Enter>", on_enter)
    button_guardar_PDF.bind("<Leave>", on_leave)
    button_guardar_PDF.place(relx=0.5, rely=0.77, anchor='n')
    
    label_copyright = tk.Label(window, text="© 2024 Gabriel", font=("Arial", 8), fg="white", bg="black")
    label_copyright.place(relx=0.02, rely=0.95)
    
    button_cambiar_ventana_DOC = tk.Button(window, text="Convertir DOC a PDF", command=mostrar_convertidor_DOC)
    button_cambiar_ventana_DOC.place(relx=0.02, rely=0.02)
    
    button_cambiar_ventana_IMG = tk.Button(window, text="Convertir IMG a PDF", command=mostrar_convertidor_IMG)
    button_cambiar_ventana_IMG.place(relx=0.2, rely=0.02)
    
def frame_convertidor_DOC():
    window.title("Convertir DOC a PDF")

    background_label = tk.Label(window, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
    
    label_titulo_DOC = tk.Label(window, text="Convertir de DOC a PDF", font=("Arial Black", 16), fg="tomato", bg="snow")
    label_titulo_DOC.place(relx=0.31, rely=0.15)
    
    label_titulo_PDF_DOC = tk.Label(window, text="Convertir de PDF a DOC", font=("Arial Black", 16), fg="tomato", bg="snow")
    label_titulo_PDF_DOC.place(relx=0.31, rely=0.57)

    frame_DOC = tk.Frame(window, bg='lightgrey', bd=5)
    frame_DOC.place(relx=0.5, rely=0.25, relwidth=0.65, relheight=0.15, anchor='n')
    
    frame_PDF_DOC = tk.Frame(window, bg='lightgrey', bd=5)
    frame_PDF_DOC.place(relx=0.5, rely=0.67, relwidth=0.65, relheight=0.15, anchor='n')

    label_DOC = tk.Label(frame_DOC, text="Documento .DOC:", bg='gold')
    label_DOC.grid(row=0, column=0, padx=10, pady=15)

    entry_campoentrada_DOC = tk.Entry(frame_DOC, width=30, state='readonly')
    entry_campoentrada_DOC.grid(row=0, column=1, padx=10, pady=5)   

    button_seleccionar_DOC = tk.Button(frame_DOC, text="Seleccionar", command=lambda: seleccionar_DOC(entry_campoentrada_DOC))
    button_seleccionar_DOC.grid(row=0, column=2, padx=10, pady=5)
    
    button_borrar_DOC = tk.Button(frame_DOC, text="X", relief="flat", bg="#f44336", fg="white", command=lambda: borrar_DOC(entry_campoentrada_DOC))
    button_borrar_DOC.grid(row=0, column=3, padx=5, pady=5)

    button_convertir_DOC = tk.Button(window, text="Convertir", command=guardar_DOC_como_PDF, bg="#0df846", fg="black", width=10, height=2, font=("Helvetica", 10))
    button_convertir_DOC.bind("<Enter>", on_enter)
    button_convertir_DOC.bind("<Leave>", on_leave)
    button_convertir_DOC.place(relx=0.5, rely=0.42, anchor='n')


    label_PDF_DOC = tk.Label(frame_PDF_DOC, text="Documento .PDF:", bg='gold')
    label_PDF_DOC.grid(row=0, column=0, padx=10, pady=15)
    
    entry_campoentrada_PDF_DOC = tk.Entry(frame_PDF_DOC, width=30, state='readonly')
    entry_campoentrada_PDF_DOC.grid(row=0, column=1, padx=10, pady=5)   

    button_seleccionar_PDF_DOC = tk.Button(frame_PDF_DOC, text="Seleccionar", command=lambda: seleccionar_PDF_De_DOCX(entry_campoentrada_PDF_DOC))
    button_seleccionar_PDF_DOC.grid(row=0, column=2, padx=10, pady=5)
    
    button_borrar_PDF_DOC = tk.Button(frame_PDF_DOC, text="X", relief="flat", bg="#f44336", fg="white", command=lambda: borrar_PDF_De_DOCX(entry_campoentrada_PDF_DOC))
    button_borrar_PDF_DOC.grid(row=0, column=3, padx=5, pady=5)

    button_convertir_PDF_DOC = tk.Button(window, text="Convertir", command=guardar_PDF_como_DOC, bg="#0df846", fg="black", width=10, height=2, font=("Helvetica", 10))
    button_convertir_PDF_DOC.bind("<Enter>", on_enter)
    button_convertir_PDF_DOC.bind("<Leave>", on_leave)
    button_convertir_PDF_DOC.place(relx=0.5, rely=0.84, anchor='n')
    
    label_copyright = tk.Label(window, text="© 2024 Gabriel", font=("Arial", 8), fg="white", bg="black")
    label_copyright.place(relx=0.02, rely=0.95)

    button_cambiar_ventana_PDF = tk.Button(window, text="Combinar PDFs", command=mostrar_combinador_PDF, )
    button_cambiar_ventana_PDF.place(relx=0.04, rely=0.02)
    
    button_cambiar_ventana_IMG = tk.Button(window, text="Convertir IMG a PDF", command=mostrar_convertidor_IMG)
    button_cambiar_ventana_IMG.place(relx=0.2, rely=0.02)
    borrar_DOC(entry_campoentrada_DOC)
    borrar_PDF_De_DOCX(entry_campoentrada_PDF_DOC)

def frame_convertidor_IMG():
    window.title("Convertir Imagen a PDF")

    background_label = tk.Label(window, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
    
    label_titulo_IMG = tk.Label(window, text="Convertir Imagen a PDF", font=("Arial Black", 16), fg="tomato", bg="snow")
    label_titulo_IMG.place(relx=0.31, rely=0.15)
    
    label_titulo_PDF_IMG = tk.Label(window, text="Convertir PDF a Imagen", font=("Arial Black", 16), fg="tomato", bg="snow")
    label_titulo_PDF_IMG.place(relx=0.31, rely=0.57)

    frame_IMG = tk.Frame(window, bg='lightgrey', bd=5)
    frame_IMG.place(relx=0.5, rely=0.25, relwidth=0.65, relheight=0.15, anchor='n')
    
    frame_PDF_IMG = tk.Frame(window, bg='lightgrey', bd=5)
    frame_PDF_IMG.place(relx=0.5, rely=0.67, relwidth=0.65, relheight=0.15, anchor='n')

    label_IMG = tk.Label(frame_IMG, text="Selecciona Imagen:", bg='gold')
    label_IMG.grid(row=0, column=0, padx=10, pady=15)

    entry_campoentrada_IMG = tk.Entry(frame_IMG, width=29, state='readonly')
    entry_campoentrada_IMG.grid(row=0, column=1, padx=10, pady=5)   

    button_seleccionar_IMG = tk.Button(frame_IMG, text="Seleccionar", command=lambda: seleccionar_IMG(entry_campoentrada_IMG))
    button_seleccionar_IMG.grid(row=0, column=2, padx=10, pady=5)
    
    button_borrar_IMG = tk.Button(frame_IMG, text="X", relief="flat", bg="#f44336", fg="white", command=lambda: borrar_IMG(entry_campoentrada_IMG))
    button_borrar_IMG.grid(row=0, column=3, padx=5, pady=5)

    button_convertir_IMG = tk.Button(window, text="Convertir", command=guardar_IMG_como_PDF, bg="#0df846", fg="black", width=10, height=2, font=("Helvetica", 10))
    button_convertir_IMG.bind("<Enter>", on_enter)
    button_convertir_IMG.bind("<Leave>", on_leave)
    button_convertir_IMG.place(relx=0.5, rely=0.42, anchor='n')
    
    
    label_PDF_IMG = tk.Label(frame_PDF_IMG, text="Documento .PDF:", bg='gold')
    label_PDF_IMG.grid(row=0, column=0, padx=10, pady=15)
    
    entry_campoentrada_PDF_IMG = tk.Entry(frame_PDF_IMG, width=30, state='readonly')
    entry_campoentrada_PDF_IMG.grid(row=0, column=1, padx=10, pady=5)   

    button_seleccionar_PDF_IMG = tk.Button(frame_PDF_IMG, text="Seleccionar", command=lambda: seleccionar_PDF_a_IMG(entry_campoentrada_PDF_IMG))
    button_seleccionar_PDF_IMG.grid(row=0, column=2, padx=10, pady=5)
    
    button_borrar_PDF_IMG = tk.Button(frame_PDF_IMG, text="X", relief="flat", bg="#f44336", fg="white", command=lambda: borrar_PDF_a_IMG(entry_campoentrada_PDF_IMG))
    button_borrar_PDF_IMG.grid(row=0, column=3, padx=5, pady=5)

    button_convertir_PDF_IMG = tk.Button(window, text="Convertir", command=guardar_PDF_como_IMG, bg="#0df846", fg="black", width=10, height=2, font=("Helvetica", 10))
    button_convertir_PDF_IMG.bind("<Enter>", on_enter)
    button_convertir_PDF_IMG.bind("<Leave>", on_leave)
    button_convertir_PDF_IMG.place(relx=0.5, rely=0.84, anchor='n')    

    label_copyright = tk.Label(window, text="© 2024 Gabriel", font=("Arial", 8), fg="white", bg="black")
    label_copyright.place(relx=0.02, rely=0.95)

    button_cambiar_ventana_PDF = tk.Button(window, text="Combinar PDFs", command=mostrar_combinador_PDF, )
    button_cambiar_ventana_PDF.place(relx=0.04, rely=0.02)
    
    button_cambiar_ventana_DOC = tk.Button(window, text="Convertir IMG a PDF", command=mostrar_convertidor_DOC)
    button_cambiar_ventana_DOC.place(relx=0.2, rely=0.02)

    borrar_IMG(entry_campoentrada_IMG)
    borrar_PDF_a_IMG(entry_campoentrada_PDF_IMG)



window = tk.Tk()
window.geometry("700x400")
window.resizable(False, False)

icono = resource_path('icon.ico')
window.iconbitmap(icono)

background_path = resource_path('background.jpg')
background_image = Image.open(background_path)
background_image = background_image.resize((700, 400), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

def on_enter(e):
    e.widget['background'] = '#FFFFFF'

def on_leave(e):
    e.widget['background'] = '#0df846'

  
mostrar_combinador_PDF()
window.mainloop()
