import tkinter as tk
from tkinter import Canvas

class scrollable_frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg = "light gray")
        self.canvas = Canvas(self, bg = "white")
        self.canvas.pack(side="left", fill = "both", expand =1)

        self.y_scrollbar=tk.Scrollbar(self, command = self.canvas.yview)
        self.y_scrollbar.pack(side = "right", fill = "y")
        self.scrolling_frame = tk.Frame(self.canvas, bg= "light gray")

        #se usa create window para poner el frame
        self.canvas_window = self.canvas.create_window((0,0), window = self.scrolling_frame, anchor= "nw")

        self.canvas.configure(yscrollcommand=self.y_scrollbar.set)
        
        self.scrolling_frame.bind("<Configure>", self.update_scrolling_region)
        self.canvas.bind("<Configure>", self.resize_frame)

    def update_scrolling_region(self, event = None):
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def resize_frame(self, event:tk.Event= None):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width= canvas_width)

