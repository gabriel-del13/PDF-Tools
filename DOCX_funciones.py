from docx2pdf import convert
from tkinter import filedialog, messagebox
import os

def funconvertir_docx_a_pdf(entry_doc, output_file):
    try:
        convert(entry_doc, output_file)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error al convertir el documento: {e}")
        return False

def seleccionar_doc(entry_doc):
    file = filedialog.askopenfilename(filetypes=[("Word files", "*.doc *.docx")])
    if file:
        entry_doc.config(state='normal')
        entry_doc.delete(0, 'end')
        entry_doc.insert(0, os.path.basename(file))
        entry_doc.config(state='readonly')
        global doc_path
        doc_path = file

def borrar_docx(entry_doc):
    entry_doc.config(state='normal')
    entry_doc.delete(0, 'end')
    entry_doc.config(state='readonly')
    global doc_path
    doc_path = ""

def guardar_doc_como_pdf():
    global doc_path
    if not doc_path:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un documento.")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile="Documento_convertido.pdf", filetypes=[("PDF files", "*.pdf")])
    if not output_file:
        return

    if funconvertir_docx_a_pdf(doc_path, output_file):
        messagebox.showinfo("Realizado", f"Documento convertido exitosamente en '{output_file}'")

