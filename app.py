import tkinter as tk

from tkinter import ttk
from app2 import *

LARGE_FONT= ("Verdana", 12)



class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self,default='@/home/usuario/Documentos/python/app/mario.ico')
        tk.Tk.wm_title(self, "Sea of BTC Client")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def teste(self):
        print ('oi')

        

        


app = SeaofBTCapp()
app.mainloop()
