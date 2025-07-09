
from tkinter import filedialog, messagebox, font
from tkinter.scrolledtext import ScrolledText
from word_finder import finder, tk

def buscar():
    carpeta = entry_carpeta.get()
    palabra = entry_palabra.get()
    output_text_foud.delete("1.0", tk.END)
    
    if not carpeta or not palabra:
        messagebox.showwarning("Error", "Por favor ingresa carpeta y palabra.")
        return
    output_text_foud.delete("1.0", tk.END)
    output_text_not.delete("1.0", tk.END)
    finder_.find_word_in_file(carpeta, palabra)

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if carpeta:
        entry_carpeta.delete(0, tk.END)
        entry_carpeta.insert(0, carpeta)

# Crear ventana principal


root = tk.Tk()
root.geometry("1000x600") 
root.title("Word Finder")
# Etiqueta y entrada para carpeta
tk.Label(root, text="Carpeta a buscar:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_carpeta = tk.Entry(root, width=40)
entry_carpeta.grid(row=0, column=0, padx=5, pady=5)
btn_carpeta = tk.Button(root, text="Seleccionar", command=seleccionar_carpeta)
btn_carpeta.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y entrada para palabra/frase
tk.Label(root, text="Palabra o frase:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_palabra = tk.Entry(root, width=40)
entry_palabra.grid(row=1, column=0, padx=5, pady=5)

# Botón de buscar
btn_buscar = tk.Button(root, text="Buscar", command=buscar)
btn_buscar.grid(row=2, column=1, pady=10)

tk.Label(root, text= "Encontrado").grid(row=3, column= 0, padx=5, pady=5, sticky="w")
tk.Label(root, text= "No Encontrado").grid(row=3, column= 1, padx=5, pady=5, sticky="w")
output_text_foud = ScrolledText(root, width=100, height=40)
output_text_foud.grid(row=4, column=0, padx=10, pady=10)
output_text_not = ScrolledText(root, width=100, height=40)
output_text_not.grid(row=4, column=1, padx=10, pady=10)


negrita = font.Font(output_text_foud, output_text_foud.cget("font"))
negrita.configure(weight="bold")

output_text_foud.tag_configure("negrita", font=negrita)

negrita = font.Font(output_text_not, output_text_not.cget("font"))
negrita.configure(weight="bold")

# Crear una tag con esa fuente
output_text_not.tag_configure("negrita", font=negrita)

label_firma = tk.Label(root, text="Por Rodrigo García (RGARC450)", fg="gray", font=("Arial", 10, "italic"))
label_firma.grid(row=99, column=99, sticky="se", padx=10, pady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(99, weight=1)

finder_ = finder(output_text_foud, output_text_not)
root.mainloop()
