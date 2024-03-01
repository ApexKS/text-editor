#importing tkinter
from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import os

#main window
main_win = tk.Tk()
main_win.title('Text Editor')
main_win.geometry('800x600')

#heading text at the centre 
heading = tk.Label(main_win, text='Welcome to the Text Editor').pack()

#display scrollbar to the right
scrollbar1 = tk.Scrollbar(main_win)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)

#display scrollbar to the bottom
scrollbar2 = tk.Scrollbar(main_win, orient=HORIZONTAL)
scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)

#text box
editor = tk.Text(main_win, width=500, height=500)
editor.pack(fill=BOTH)

#making the scrollbar work
editor.config(yscrollcommand=scrollbar1.set, xscrollcommand=scrollbar2.set)
scrollbar1.config(command=editor.yview)
scrollbar2.config(command=editor.xview)

#how save works
def save():
    filepath = asksaveasfilename(defaultextension="txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = editor.get(1.0, tk.END)
        output_file.write(text)
    main_win.title(f"{os.path.basename(filepath)}")

#displaying save button
button = Button(main_win, text='Save', command=save)
button.place(x=390, y=520)


#let's run
main_win.mainloop()