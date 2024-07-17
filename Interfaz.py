# main.py
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
def mostrar_combinador_pdfs():
    for widget in root.winfo_children():
        widget.destroy()
    frame_combinador_pdfs()

def mostrar_convertidor_docs():
    for widget in root.winfo_children():
        widget.destroy()
    frame_convertidor_docs()

    
def frame_combinador_pdfs():
    root.title("Combinar PDFs")
    
    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
    
    frame = tk.Frame(root, bg='lightgrey', bd=5)
    frame.place(relx=0.5, rely=0.2, relwidth=0.65, relheight=0.5, anchor='n')
    
    labels = ["PDF Base", "PDF #2", "PDF #3", "PDF #4", "PDF #5"]
    entries = []
    pdf_paths = [""] * 5
    
    for i in range(5):
        label = tk.Label(frame, text=labels[i], bg='gold' if i == 0 else 'lightgrey')
        label.grid(row=i, column=0, padx=10, pady=5)
        
        entry_pdf = tk.Entry(frame, width=35, state='readonly')
        entry_pdf.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry_pdf)
        
        button_select = tk.Button(frame, text="Seleccionar", command=lambda e=entry_pdf, idx=i: seleccionar_pdf(e, idx, pdf_paths))
        button_select.grid(row=i, column=2, padx=10, pady=5)
    
        button_clear = tk.Button(frame, text="X", fg="red", command=lambda e=entry_pdf, idx=i: borrar_pdf(e, idx, pdf_paths))
        button_clear.grid(row=i, column=3, padx=5, pady=5)
    
    btn_save = tk.Button(root, text="Guardar", command=lambda: guardar_pdf_combinado(pdf_paths), width=10, height=2, font=("Helvetica", 10))
    btn_save.place(relx=0.5, rely=0.75, anchor='n')
    
    label_leyenda = tk.Label(root, text="© 2024 Gabriel", font=("Arial", 8), fg="white", bg="black")
    label_leyenda.place(relx=0.02, rely=0.95)
    
    btn_switch = tk.Button(root, text="Convertir DOC a PDF", command=mostrar_convertidor_docs)
    btn_switch.place(relx=0.02, rely=0.02)
    

def frame_convertidor_docs():
    root.title("Convertir DOC a PDF")

    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    frame = tk.Frame(root, bg='lightgrey', bd=5)
    frame.place(relx=0.5, rely=0.2, relwidth=0.65, relheight=0.15, anchor='n')

    
    label_doc = tk.Label(frame, text="Documento:", bg='gold')
    label_doc.grid(row=0, column=0, padx=10, pady=15)

    entry_doc = tk.Entry(frame, width=35, state='readonly')
    entry_doc.grid(row=0, column=1, padx=10, pady=5)   

    
    button_select_doc = tk.Button(frame, text="Seleccionar", command=lambda: seleccionar_doc(entry_doc))
    button_select_doc.grid(row=0, column=2, padx=10, pady=5)
    
    button_clear = tk.Button(frame, text="X", fg="red", command=lambda: borrar_docx(entry_doc))
    button_clear.grid(row=0, column=3, padx=5, pady=5)

    btn_convertir = tk.Button(root, text="Convertir", command=guardar_doc_como_pdf, width=10, height=2, font=("Helvetica", 10))
    btn_convertir.place(relx=0.5, rely=0.5, anchor='n')

    label_leyenda = tk.Label(root, text="© 2024 Gabriel", font=("Arial", 8), fg="white", bg="black")
    label_leyenda.place(relx=0.02, rely=0.95)

    btn_switch = tk.Button(root, text="Combinar PDFs", command=mostrar_combinador_pdfs, )
    btn_switch.place(relx=0.02, rely=0.02)
    borrar_docx(entry_doc)


root = tk.Tk()
root.geometry("700x400")
root.resizable(False, False)

icon_path = resource_path('icon.ico')
root.iconbitmap(icon_path)

background_path = resource_path('background.jpg')
background_image = Image.open(background_path)
background_image = background_image.resize((700, 400), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)


mostrar_combinador_pdfs()
root.mainloop()
