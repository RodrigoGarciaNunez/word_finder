from word_finder import finder, tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
import platform
import subprocess


def file_check_window(root:tk, finder:finder):
    emergent = tk.Toplevel(root)
    emergent.title("File Check")

    img_ok =  cargar_img(path = "images/palomita.png")
    img_not = cargar_img(path = "images/tache.png")
    files = finder.file_check
    num_columns =  2
    
    for i, file in enumerate(files):
        print(f"{i}, {file}, {files[file]}") 

    for i, archivo in enumerate(files):

        rows = (i // num_columns ) * 2
        columns = i % num_columns

        img = img_ok if files[archivo] else img_not
        
        btn = tk.Button(emergent, image=img, command=lambda n=archivo: click_file(n))
        btn.image = img  # Referencia para evitar que se borre
        btn.grid(row=rows, column = columns, padx=5, pady=5)
        
        label = tk.Label(emergent, text=archivo, )
        label.grid(row= rows+1, column=columns)
    
    emergent.grid_columnconfigure(0, weight=1)
    emergent.grid_columnconfigure(1, weight=1)



def click_file(n):
    if platform.system() == 'Windows':
        os.startfile(n)
    elif platform.system() == 'Darwin':  # macOS
        subprocess.call(['open', n])
    else:  # Linux y otros Unix
        subprocess.call(['xdg-open', n])


def cargar_img(path, size=(40, 40)):
        img = Image.open(path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)