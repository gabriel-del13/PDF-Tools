# DOCX_funciones.py
from docx2pdf import convert
from pdf2docx import Converter
from tkinter import filedialog, messagebox
import logging
import os
import sys

#DOC A PDF
def funconvertir_DOC_a_PDF(entrada_DOC, salida_PDF):
    try:
        convert(entrada_DOC, salida_PDF)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error al convertir el documento: {e}")
        return False

def seleccionar_DOC(entrada_DOC):
    archivo_DOC = filedialog.askopenfilename(filetypes=[("Word files", "*.doc *.docx")])
    if archivo_DOC:
        entrada_DOC.config(state='normal')
        entrada_DOC.delete(0, 'end')
        entrada_DOC.insert(0, os.path.basename(archivo_DOC))
        entrada_DOC.config(state='readonly')
        global comprueba_DOC
        comprueba_DOC = archivo_DOC

def borrar_DOC(entrada_DOC):
    entrada_DOC.config(state='normal')
    entrada_DOC.delete(0, 'end')
    entrada_DOC.config(state='readonly')
    global comprueba_DOC
    comprueba_DOC = ""

def guardar_DOC_como_PDF():

    global comprueba_DOC
    if not comprueba_DOC:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un documento.")
        return
    archivo_log_DOC = "conversion.log"
    logging.basicConfig(filename=archivo_log_DOC, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

    sys.stdout = open(archivo_log_DOC, 'a')
    sys.stderr = open(archivo_log_DOC, 'a')
    try:
        salida_PDF = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile="Documento_convertido.pdf", filetypes=[("PDF files", "*.pdf")])
        if not salida_PDF:
            return

        if funconvertir_DOC_a_PDF(comprueba_DOC, salida_PDF):
            messagebox.showinfo("Realizado", f"Documento convertido exitosamente en '{salida_PDF}'")
    finally:
        sys.stdout.close()
        sys.stderr.close()
        logging.shutdown()
        
        if os.path.exists(archivo_log_DOC):
            os.remove(archivo_log_DOC)
            
                    
# PDF A DOC
def funconvertir_PDF_a_DOC(entrada_PDF, salida_DOCX):
    try:
        convertir_PDF = Converter(entrada_PDF)  
        convertir_PDF.convert(salida_DOCX)   
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error al convertir el documento: {e}")
        return False

def seleccionar_PDF_De_DOCX(entrada_PDF):
    archivo_PDF = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if archivo_PDF:
        entrada_PDF.config(state='normal')
        entrada_PDF.delete(0, 'end')
        entrada_PDF.insert(0, os.path.basename(archivo_PDF))
        entrada_PDF.config(state='readonly')
        global comprueba_PDF
        comprueba_PDF = archivo_PDF

def borrar_PDF_De_DOCX(entrada_PDF):
    entrada_PDF.config(state='normal')
    entrada_PDF.delete(0, 'end')
    entrada_PDF.config(state='readonly')
    global comprueba_PDF
    comprueba_PDF = ""


def guardar_PDF_como_DOC():

    global comprueba_PDF
    if not comprueba_PDF:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un documento.")
        return

    salida_DOCX = filedialog.asksaveasfilename(defaultextension="*.docx", initialfile="Documento_convertido.docx", filetypes=[("DOCX Files", "*.doc *.docx")])
    if not salida_DOCX:
        return

    if funconvertir_PDF_a_DOC(comprueba_PDF, salida_DOCX):
        messagebox.showinfo("Realizado", f"Documento convertido exitosamente en '{salida_DOCX}'")
