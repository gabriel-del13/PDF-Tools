#IMG_funciones.py
from tkinter import filedialog, messagebox
from PIL import Image
from pdf2image import convert_from_path
import img2pdf
import os
import logging
import sys

#IMG A PDF
comprueba_IMG = []
def funconvertir_IMG_a_PDF(entrada_IMG, salida_PDF):
    try:
        images = [Image.open(img).convert("RGB") for img in entrada_IMG]
        
        if images:
            images[0].save(salida_PDF, save_all=True, append_images=images[1:])
        else:
            raise ValueError("No se encontraron imágenes para convertir.")
        
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error al convertir las imágenes: {e}")
        return False

def seleccionar_IMG(entrada_IMG):
    archivos_IMG = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if archivos_IMG:
        entrada_IMG.config(state='normal')
        entrada_IMG.delete(0, 'end')
        entrada_IMG.insert(0, ", ".join([os.path.basename(archivo) for archivo in archivos_IMG]))
        entrada_IMG.config(state='readonly')
        global comprueba_IMG
        comprueba_IMG = archivos_IMG

def borrar_IMG(entrada_IMG):
    entrada_IMG.config(state='normal')
    entrada_IMG.delete(0, 'end')
    entrada_IMG.config(state='readonly')
    global comprueba_IMG
    comprueba_IMG = []

def guardar_IMG_como_PDF():
    global comprueba_IMG
    if not comprueba_IMG:
        messagebox.showwarning("Advertencia", "Por favor, selecciona imágenes.")
        return
    try:
        salida_PDF = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile="Imagenes_convertidas.pdf", filetypes=[("PDF files", "*.pdf")])
        if not salida_PDF:
            return
        if funconvertir_IMG_a_PDF(comprueba_IMG, salida_PDF):
            messagebox.showinfo("Realizado", f"Imágenes convertidas exitosamente en '{salida_PDF}'")
    finally:
        sys.stdout.close()
        sys.stderr.close()
        logging.shutdown()
        


#PDF A IMG
comprueba_PDF = []

def funconvertir_PDF_a_IMG(entrada_PDF, salida_IMG):
    try:
        poppler_path = os.path.join(os.path.dirname(__file__), 'poppler-24.07.0/Library/bin')

        paginas = convert_from_path(entrada_PDF, dpi=300, poppler_path=poppler_path)
        for i, pagina in enumerate(paginas):
            imagen_path = f"Imagen_{i + 1}.png"
            pagina.save(salida_IMG, 'PNG')

        return True
    except Exception as e:
        print(f"Error al convertir el PDF: {e}")
        return False

def seleccionar_PDF_a_IMG(entrada_PDF):
    archivo_PDF = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if archivo_PDF:
        entrada_PDF.config(state='normal')
        entrada_PDF.delete(0, 'end')
        entrada_PDF.insert(0, os.path.basename(archivo_PDF))
        entrada_PDF.config(state='readonly')
        global comprueba_PDF
        comprueba_PDF = archivo_PDF

def borrar_PDF_a_IMG(entrada_PDF):
    entrada_PDF.config(state='normal')
    entrada_PDF.delete(0, 'end')
    entrada_PDF.config(state='readonly')
    global comprueba_PDF
    comprueba_PDF = ""

def guardar_PDF_como_IMG():
    global comprueba_PDF
    if not comprueba_PDF:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un archivo PDF.")
        return
    try:
        salida_IMG_file = filedialog.asksaveasfilename(defaultextension=".png", initialfile="Imagen.png", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if not salida_IMG_file:
            return

        if funconvertir_PDF_a_IMG(comprueba_PDF, salida_IMG_file):
            messagebox.showinfo("Realizado", f"PDF convertido exitosamente en imágenes en '{salida_IMG_file}'")
    finally:
        sys.stdout.close()
        sys.stderr.close()
        logging.shutdown()

