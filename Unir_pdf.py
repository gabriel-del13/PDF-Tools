import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os
from PIL import Image, ImageTk
import sys

def merge_pdfs(pdf1, pdf2, output):
    try:
        merger = PdfMerger()
        merger.append(pdf1)
        merger.append(pdf2)
        merger.write(output)
        merger.close()
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error al combinar los PDFs: {e}")
        return False

def select_pdf1():
    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:
        entry_pdf1.config(state=tk.NORMAL)
        entry_pdf1.delete(0, tk.END)
        entry_pdf1.insert(0, os.path.basename(file))
        entry_pdf1.config(state='readonly')
        global pdf1_path
        pdf1_path = file

def select_pdf2():
    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:
        entry_pdf2.config(state=tk.NORMAL)
        entry_pdf2.delete(0, tk.END)
        entry_pdf2.insert(0, os.path.basename(file))
        entry_pdf2.config(state='readonly')
        global pdf2_path
        pdf2_path = file

def save_combined_pdf():
    if not pdf1_path or not pdf2_path:
        messagebox.showwarning("Advertencia", "Por favor, selecciona ambos PDFs.")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not output_file:
        return

    if merge_pdfs(pdf1_path, pdf2_path, output_file):
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
frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.3, anchor='n')

pdf1_path = ""
pdf2_path = ""

label_pdf1 = tk.Label(frame, text="PDF Base:", bg='gold')
label_pdf1.grid(row=0, column=0, padx=10, pady=20)
entry_pdf1 = tk.Entry(frame, width=40, state='readonly')
entry_pdf1.grid(row=0, column=1, padx=10, pady=5)
btn_pdf1 = tk.Button(frame, text="Seleccionar", command=select_pdf1)
btn_pdf1.grid(row=0, column=2, padx=10, pady=5)

label_pdf2 = tk.Label(frame, text="PDF a Combinar:", bg='lightgrey')
label_pdf2.grid(row=1, column=0, padx=10, pady=5)
entry_pdf2 = tk.Entry(frame, width=40, state='readonly')
entry_pdf2.grid(row=1, column=1, padx=10, pady=5)
btn_pdf2 = tk.Button(frame, text="Seleccionar", command=select_pdf2)
btn_pdf2.grid(row=1, column=2, padx=10, pady=5)

btn_save = tk.Button(root, text="Guardar", command=save_combined_pdf)
btn_save.place(relx=0.5, rely=0.7, anchor='n')

label_leyenda = tk.Label(root, text="© 2024 Gabriel", font=("Arial", 8), fg="white", bg="black")
label_leyenda.place(relx=0.02, rely=0.95)

root.mainloop()
