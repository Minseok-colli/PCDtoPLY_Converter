from faulthandler import disable
from msilib.schema import Directory
from re import L
import tkinter as tk
from tkinter import Button, Label, filedialog
from tkinter.font import BOLD
from click import command, style
import os
from matplotlib.pyplot import close, text

import open3d as o3d
from sympy import sieve

def inputfile():
    file = filedialog.askopenfilename(

        title = 'Select file',
        filetypes=(('pcd files', '*.pcd'), ('all files', "*.*"))
    )
    root.filename = file
    root.pcd = o3d.io.read_point_cloud(file)
    label.configure(text=file)

def convertfile():
    print(root.pcd)
    plyfilename =""

    for i in root.filename:
        if i == ".":
            break
        plyfilename = plyfilename + i

    print(plyfilename)
    o3d.io.write_point_cloud(plyfilename+".ply", root.pcd)
    done.configure(text="Convert Succeed")

def exit():
    root.destroy()


root = tk.Tk()
root.title("Pcd file to Ply")
root.geometry("380x240")

label0 = Label(root, text="Convert PCD to PLY",font=(15))
label = Label(root, text="")
copyright = Label(root, text="https://github.com/Minseok-colli/PCDtoPLY_Converter")
email = Label(root,text= "E-mail : nadogoyang2@gmail.com")
done = Label(root,text="")
btn1 = Button(root,text="Select Pcd file",command=inputfile)
btn2 = Button(root,text="convert to Ply",command=convertfile)
Close = Button(root,text="Close",command=exit)


#Title
label0.pack(side="top")

#PCD file select
btn1.pack()
label.pack()

#Convert Button
btn2.pack()
done.pack()

#Close Button
Close.pack()

email.pack(side="bottom")
copyright.pack(side="bottom")

root.mainloop()
