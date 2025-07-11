import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

pdf_files = []

def add_file():
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if filepath:
        pdf_files.append(filepath)
        listbox.insert(tk.END, filepath.split("/")[-1])

def merge_pdfs():
    if len(pdf_files) < 2:
        messagebox.showerror("Error", "Add at least 2 PDFs to merge.")
        return

    merger = PyPDF2.PdfMerger()
    for file in pdf_files:
        merger.append(file)

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                               filetypes=[("PDF Files", "*.pdf")])
    if output_path:
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Success", "PDFs merged successfully!")

# UI
root = tk.Tk()
root.title("PDF Merger by Asif")
root.geometry("400x300")

tk.Button(root, text="Add PDF", command=add_file).pack(pady=10)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=5)

tk.Button(root, text="Merge PDFs", command=merge_pdfs).pack(pady=20)

root.mainloop()

