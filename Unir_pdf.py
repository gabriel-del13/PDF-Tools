import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os
from PIL import Image, ImageTk
import sys

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

def seleccionar_pdf(entry, index):
    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:
        entry.config(state=tk.NORMAL)
        entry.delete(0, tk.END)
        entry.insert(0, os.path.basename(file))
        entry.config(state='readonly')
        pdf_paths[index] = file

def borrar_pdf(entry, index):
    entry.config(state=tk.NORMAL)
    entry.delete(0, tk.END)
    entry.config(state='readonly')
    pdf_paths[index] = ""

def guardar_pdf_combinado():
    selected_pdfs = [pdf for pdf in pdf_paths if pdf]
    if len(selected_pdfs) < 2:
        messagebox.showwarning("Advertencia", "Por favor, selecciona al menos dos PDFs.")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile="PDF_combinado.pdf", filetypes=[("PDF files", "*.pdf")])
    if not output_file:
        return

    if combinar_pdfs(selected_pdfs, output_file):
        messagebox.showinfo("Realizado", f"PDFs combinados exitosamente en '{output_file}'")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = tk.Tk()
root.title("Combinar PDFs")
root.geometry("700x400")
root.resizable(False, False)

icon_path = resource_path('icon.ico')
root.iconbitmap(icon_path)

background_path = resource_path('background.jpg')
background_image = Image.open(background_path)
background_image = background_image.resize((700, 400), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='lightgrey', bd=5)
frame.place(relx=0.5, rely=0.2, relwidth=0.65, relheight=0.5, anchor='n')

pdf_paths = [""] * 5

labels = ["PDF Base", "Archivo PDF", "Archivo PDF", "Archivo PDF", "Archivo PDF"]
entries = []
buttons_select = []
buttons_clear = []

for i in range(5):
    label = tk.Label(frame, text=labels[i], bg='gold' if i == 0 else 'lightgrey')
    label.grid(row=i, column=0, padx=10, pady=5)
    
    entry = tk.Entry(frame, width=35, state='readonly')
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)
    
    button_select = tk.Button(frame, text="Seleccionar", command=lambda e=entry, idx=i: seleccionar_pdf(e, idx))
    button_select.grid(row=i, column=2, padx=10, pady=5)
    buttons_select.append(button_select)

    button_clear = tk.Button(frame, text="X", fg="red", command=lambda e=entry, idx=i: borrar_pdf(e, idx))
    button_clear.grid(row=i, column=3, padx=5, pady=5)
    buttons_clear.append(button_clear)

btn_save = tk.Button(root, text="Guardar", command=guardar_pdf_combinado, width=10, height=2, font=("Helvetica", 10))
btn_save.place(relx=0.5, rely=0.75, anchor='n')

label_leyenda = tk.Label(root, text="© 2024 Gabriel", font=("Arial", 8), fg="white", bg="black")
label_leyenda.place(relx=0.02, rely=0.95)

root.mainloop()
