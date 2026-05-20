from tkinter import *
from tkinter import messagebox
vent= Tk()
vent.geometry("900x600")

class CreateElements:
    def __init__(self):
        print("Esta es la primera clase CreateElements")
        label = Label(vent, text="se a creado una nueva etiqueta con la clase", fg="green")
        label.pack()
        
    def createNewElement(self):
        label = Label(vent, text="se a creado una nueva etiqueta con la clase", fg="red")
        label.pack()
        
        btn = Button(vent,text="Boton", command=self.message)
        btn.pack(padx=20, pady=10)

    def message(self):
        messagebox.showinfo("mostrar info","Haz precionado el boton creada con la clase")

obj_of_CreateElements = CreateElements()

btn = Button(vent,text='Click',command=obj_of_CreateElements.createNewElement)
btn.pack(padx=20, pady=10)

vent.mainloop()