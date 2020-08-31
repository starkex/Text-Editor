import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os 

win=tk.Tk()

win.title('Neutron Editor')
win.geometry('1000x800')

main_menu = tk.Menu()

file = tk.Menu(main_menu,tearoff=False)
Edit = tk.Menu(main_menu,tearoff=False) 
view = tk.Menu(main_menu,tearoff=False)
color_theme = tk.Menu(main_menu,tearoff=False) 

main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=Edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Theme',menu=color_theme)


win.config(menu=main_menu)
win.mainloop()