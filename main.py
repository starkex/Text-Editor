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

#buttons
bold_icon=tk.PhotoImage(file='icons/bolds.png')
ita_icon=tk.PhotoImage(file='icons./italic.png')
under_icon=tk.PhotoImage(file='icons/underline.png')
fo_color=tk.PhotoImage(file='icons/Untitled.png')

#pallete
wheel_icon=tk.PhotoImage(file='icons/cwheel.png')

#aligns
left_icon=tk.PhotoImage(file='icons/left.png')
center_icon=tk.PhotoImage(file='icons/center.png')
right_icon=tk.PhotoImage(file='icons/right.png')

#fonts
toolbar=ttk.Label(win)
toolbar.pack(side=tk.TOP,fill=tk.X)

font_fam=tk.font.families()
font_var=tk.StringVar()
font_box=ttk.Combobox(toolbar,width=20,textvariable=font_var,state='readonly',background='lightblue')
font_box['values']=font_fam
font_box.current(4)
font_box.grid(row=0,column=0,pady=10,padx=5)

#fontsize
size_var=tk.StringVar()
size_box=ttk.Combobox(toolbar,width=10,textvariable=size_var)
size_box['values']=tuple(range(2,72,2))
size_box.current(3)
size_box.grid(row=0,column=1,padx=5,pady=10)

#stylebuttons
bold=ttk.Button(toolbar,width=5,image=bold_icon)
bold.grid(row=0,column=2,padx=5,pady=10)
italic=ttk.Button(toolbar,width=5,image=ita_icon)
italic.grid(row=0,column=3,padx=5,pady=10)
underline=ttk.Button(toolbar,width=5,image=under_icon)
underline.grid(row=0,column=4,padx=5,pady=10)
fontcolor=ttk.Button(toolbar,width=5,image=fo_color)
fontcolor.grid(row=0,column=5,pady=10,padx=5)

#wheelbutton
wheel=ttk.Button(toolbar,width=5,image=wheel_icon)
wheel.grid(row=0,column=9,pady=10,padx=5)

#alignbuttons
left=ttk.Button(toolbar,width=5,image=left_icon)
left.grid(row=0,column=6,pady=10,padx=5)
center=ttk.Button(toolbar,width=5,image=center_icon)
center.grid(row=0,column=7,pady=10,padx=5)
right=ttk.Button(toolbar,width=5,image=right_icon)
right.grid(row=0,column=8,pady=10,padx=5)

#TextAreaToEdit
textedit=tk.Text(win)
textedit.config(wrap="word",relief=tk.FLAT)
scroll=tk.Scrollbar(win)
textedit.focus_set()
scroll.pack(side=tk.RIGHT,fill=tk.Y)
textedit.pack(fill=tk.BOTH, expand=True)
scroll.config(command=textedit.yview)
textedit.config(yscrollcommand=scroll.set)

#statusbar
status= ttk.Label(win,text="Status Bar")
status.pack(side=tk.BOTTOM)

#fonts Functions
initial_font='Consolas'
initial_size=10

def change_font(win):
    global initial_font
    initial_font=font_var.get()
    textedit.configure(font=(initial_font,initial_size))

textedit.configure(font=('Consolas',10))

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