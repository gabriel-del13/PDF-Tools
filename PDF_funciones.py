# pdf_functions.py
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os

def combinar_pdfs(pdf_paths, output):
    try:
        merger = PdfMerger()
        for pdf in pdf_paths:
            if pdf:
                merger.append(pdf)
        merger.write(output)
        merger.close()
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error al combinar los PDFs: {e}")
        return False

def seleccionar_pdf(entry_pdf, index, pdf_paths):
    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:
        entry_pdf.config(state='normal')
        entry_pdf.delete(0, 'end')
        entry_pdf.insert(0, os.path.basename(file))
        entry_pdf.config(state='readonly')
        pdf_paths[index] = file

def borrar_pdf(entry_pdf, index, pdf_paths):
    entry_pdf.config(state='normal')
    entry_pdf.delete(0, 'end')
    entry_pdf.config(state='readonly')
    pdf_paths[index] = ""

def guardar_pdf_combinado(pdf_paths):
    if not pdf_paths[0]:
        messagebox.showwarning("Advertencia", "Por favor, selecciona el PDF Base.")
        return False

    selected_pdfs = [pdf for pdf in pdf_paths if pdf]
    if len(selected_pdfs) < 2:
        messagebox.showwarning("Advertencia", "Por favor, selecciona al menos dos PDFs.")
        return False

    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile="PDF_combinado.pdf", filetypes=[("PDF files", "*.pdf")])
    if not output_file:
        return False

    if combinar_pdfs(selected_pdfs, output_file):
        messagebox.showinfo("Realizado", f"PDFs combinados exitosamente en '{output_file}'")
        return True
    else:
        return False
