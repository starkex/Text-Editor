import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os 

win=tk.Tk()

win.title('Neutron Editor')
win.geometry('1000x800')

main_menu = tk.Menu()

new_icon=tk.PhotoImage(file='icons/folder.png')
open_icon=tk.PhotoImage(file='icons/open.png')
save_icon=tk.PhotoImage(file='icons/save.png')
saveas_icon=tk.PhotoImage(file='icons/saveas.png')
exit_icon=tk.PhotoImage(file='icons/exit.png')

file = tk.Menu(main_menu,tearoff=False)

file.add_command(label='   New',image=new_icon,compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label='   Open',image=open_icon,compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label='   Save',image=save_icon,compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label='   SaveAs',image=saveas_icon,compound=tk.LEFT, accelerator='Ctrl+Shift+S')
file.add_command(label='   Exit',image=exit_icon,compound=tk.LEFT)


Edit = tk.Menu(main_menu,tearoff=False) 
view = tk.Menu(main_menu,tearoff=False)
color_theme = tk.Menu(main_menu,tearoff=False) 

main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=Edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Theme',menu=color_theme)


win.config(menu=main_menu)
win.mainloop()