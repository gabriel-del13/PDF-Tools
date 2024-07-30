
from docx2pdf import convert
from tkinter import messagebox
import os

def funconvertir_docx_a_pdf(doc_path, output_file):
    try:
        convert(doc_path, output_file)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error al convertir el documento: {e}")
        return False
