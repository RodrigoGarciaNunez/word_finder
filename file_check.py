from word_finder import finder
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
import sys
import platform
import subprocess
from scrollable_frame import scrollable_frame as s_frm
from scrollable_frame import tk

class file_check():
    def __init__(self):
        self.frame = None


    def ruta_recurso(self, rel_path): #relative path
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, rel_path) #en exe
        return os.path.join(os.path.abspath("."), rel_path) # en py


    def file_check_method(self,root, finder:finder):
        if self.frame is None:
            self.frame = s_frm(root)
            self.frame.pack(fill = "both", expand= 1)
            #self.scrollable = s_frm(root)
            #self.scrollable.pack(fill = "both", expand=1)
            #self.frame = self.scrollable.scrolling_frame
        else: 
            for children in self.frame.winfo_children(): #si ya existe contenido, se "limpia"
                children.destroy()

        #emergent.title("File Check")

        #print(f"dir: {os.listdir(path='.')}")
        img_ok =  self.cargar_img(path = self.ruta_recurso("images/palomita.png"))
        img_not = self.cargar_img(path = self.ruta_recurso("images/tache.png"))
        files = finder.file_check
        num_columns =  2
        
        # for i, file in enumerate(files):
        #     print(f"{i}, {file}, {files[file]}") 
        #label = tk.Label()
        for i, archivo in enumerate(files):

            rows = (i // num_columns ) * 2
            columns = i % num_columns

            img = img_ok if files[archivo] else img_not
            
            btn = tk.Button(self.frame.scrolling_frame, image=img, command=lambda n=archivo: self.click_file(n))
            btn.image = img  # Referencia para evitar que se borre
            #btn.pack()
            btn.grid(row=rows, column = columns, padx=5, pady=5)
            
            label = tk.Label(self.frame.scrolling_frame, text=archivo, wraplength = 250)
            #label.pack()
            label.grid(row= rows+1, column=columns)
            #label.pack()
        
    
        for column in range(num_columns):
            self.frame.grid_columnconfigure(column, weight=1)
        #self.frame.grid_columnconfigure(1, weight=1)



    def click_file(self,n):
        if platform.system() == 'Windows':
            os.startfile(n)
        elif platform.system() == 'Darwin':  # macOS
            subprocess.call(['open', n])
        else:  # Linux y otros Unix
            subprocess.call(['xdg-open', n])


    def cargar_img(self,path, size=(40, 40)):
            img = Image.open(path)
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
