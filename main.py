import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os 

win=tk.Tk()

win.title('Neutron Editor')
win.geometry('1000x800')

main_menu = tk.Menu()
#file
new_icon=tk.PhotoImage(file='icons/folder.png')
open_icon=tk.PhotoImage(file='icons/open.png')
save_icon=tk.PhotoImage(file='icons/save.png')
saveas_icon=tk.PhotoImage(file='icons/saveas.png')
exit_icon=tk.PhotoImage(file='icons/exit.png')
#edit
copy_icon=tk.PhotoImage(file='icons/copy.png')
cut_icon=tk.PhotoImage(file='icons/cut.png')
find_icon=tk.PhotoImage(file='icons/find.png')
clear_icon=tk.PhotoImage(file='icons/clearall.png')
paste_icon=tk.PhotoImage(file='icons/paste.png')
#view
tool_icon=tk.PhotoImage(file='icons/toolbar.png')
status_icon=tk.PhotoImage(file='icons/status.png')
#theme
light_icon=tk.PhotoImage(file='icons/light.png')
dark_icon=tk.PhotoImage(file='icons/dark.png')

file = tk.Menu(main_menu,tearoff=False)

file.add_command(label='   New',image=new_icon,compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label='   Open',image=open_icon,compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label='   Save',image=save_icon,compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label='   SaveAs',image=saveas_icon,compound=tk.LEFT, accelerator='Ctrl+Shift+S')
file.add_command(label='   Exit',image=exit_icon,compound=tk.LEFT)


Edit = tk.Menu(main_menu,tearoff=False) 

Edit.add_command(label='   Copy',image=copy_icon,compound=tk.LEFT, accelerator='Ctrl+C')
Edit.add_command(label='   Cut',image=cut_icon,compound=tk.LEFT, accelerator='Ctrl+X')
Edit.add_command(label='   Paste',image=paste_icon,compound=tk.LEFT, accelerator='Ctrl+V')
Edit.add_command(label='   Find',image=find_icon,compound=tk.LEFT, accelerator='Ctrl+F')
Edit.add_command(label='   Clear All',image=clear_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+C')

view = tk.Menu(main_menu,tearoff=False)
view.add_checkbutton(label='   ToolBar',image=tool_icon,compound=tk.LEFT,accelerator='')
view.add_checkbutton(label='   StatusBar',image=status_icon,compound=tk.LEFT,accelerator='')

color_theme = tk.Menu(main_menu,tearoff=False) 
color_theme.add_checkbutton(label='   Light Mode',compound=tk.LEFT,image=light_icon)
color_theme.add_checkbutton(label='   Dark Mode',compound=tk.LEFT,image=dark_icon)

main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=Edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Theme',menu=color_theme)


win.config(menu=main_menu)
win.mainloop()