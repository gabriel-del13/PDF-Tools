# PDF_funciones.py
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os

def combinar_PDFs(acumula_PDF, salida_PDF_combinado):
    try:
        merger = PdfMerger()
        for pdf in acumula_PDF:
            if pdf:
                merger.append(pdf)
        merger.write(salida_PDF_combinado)
        merger.close()
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error al combinar los PDFs: {e}")
        return False

def seleccionar_PDF(entrada_PDF, index, acumula_PDF):
    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:
        entrada_PDF.config(state='normal')
        entrada_PDF.delete(0, 'end')
        entrada_PDF.insert(0, os.path.basename(file))
        entrada_PDF.config(state='readonly')
        acumula_PDF[index] = file

def borrar_PDF(entrada_PDF, index, acumula_PDF):
    entrada_PDF.config(state='normal')
    entrada_PDF.delete(0, 'end')
    entrada_PDF.config(state='readonly')
    acumula_PDF[index] = ""

def guardar_PDF_combinado(acumula_PDF):
    if not acumula_PDF[0]:
        messagebox.showwarning("Advertencia", "Por favor, selecciona el PDF Base.")
        return False

    seleccionados_PDFs = [pdf for pdf in acumula_PDF if pdf]
    if len(seleccionados_PDFs) < 2:
        messagebox.showwarning("Advertencia", "Por favor, selecciona al menos dos PDFs.")
        return False

    salida_PDF_combinado_file = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile="PDF_combinado.pdf", filetypes=[("PDF files", "*.pdf")])
    if not salida_PDF_combinado_file:
        return False

    if combinar_PDFs(seleccionados_PDFs, salida_PDF_combinado_file):
        messagebox.showinfo("Realizado", f"PDFs combinados exitosamente en '{salida_PDF_combinado_file}'")
        return True
    else:
        return False
