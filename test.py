from customtkinter import *
import os

##Usé este archivo para probar la app sin necesidad de iniciar sesión, por lo mismo no tiene un botón para cerrar sesión

root = CTk()
root.title("UI (Nombre temporal, favor cambiar)")
root.resizable(False, False)
root.geometry("1280x720")

set_appearance_mode("system")
set_default_color_theme("dark-blue")

listframe = CTkFrame(root, width=880, height=640, border_width=5)
listframe.place(x= 20, y = 70)

temaVar = StringVar(value="Sistema")

def seleccionarTema(*args):
    if temaVar.get() == "Sistema":
        set_appearance_mode("system")
    elif temaVar.get() == "Claro":
        set_appearance_mode("light")
    elif temaVar.get() == "Oscuro":
               set_appearance_mode("dark")

temaLabel = CTkLabel(root, text="Tema:", font=('Arial', 12))
temaLabel.place(x=1080, y=20)
tema = CTkComboBox(root, values=["Sistema", "Claro", "Oscuro"], command=seleccionarTema, variable=temaVar, font=('Arial', 12))
tema.place(x=1120, y=20)

nameVar = StringVar()

idVar = StringVar()

cantVar = IntVar()

nameLabel = CTkLabel(root, text="Nombre del Medicamento:", font=('Arial', 12))
nameLabel.place(x=920, y=180)
nameTB = CTkEntry(root, textvariable=nameVar, font=('Arial', 12))
nameTB.place(x=1080, y=180)

idLabel = CTkLabel(root, text="ID del Medicamento:", font=('Arial', 12))
idLabel.place(x=950, y=230)
idTB = CTkEntry(root, textvariable=idVar, font=('Arial', 12))
idTB.place(x=1080, y=230)

cantidadLabel = CTkLabel(root, text="Cantidad:", font=('Arial', 12))
cantidadLabel.place(x=1010, y=280)
cantidadTB = CTkEntry(root, textvariable=cantVar, font=('Arial', 12))
cantidadTB.place(x=1080, y=280)

def compCommand():
    pass

def añaCommand():
    pass

def vendCommand():
    pass

def usermCommand():
     ruta = 'Manual de usuario.txt'
     os.startfile('Manual de usuario.txt')

comprar = CTkButton(root, text="Comprar Medicamento", command=compCommand, font=('Arial', 12))
comprar.place(x=20, y=20)
añadir = CTkButton(root, text="Añadir Medicamento a la Lista", command=añaCommand, font=('Arial', 12))
añadir.place(x=380, y=20)
vender = CTkButton(root, text="Vender Medicamento", command=vendCommand, font=('Arial', 12))
vender.place(x=200, y=20)
usermanual = CTkButton(root, text="Manual de Usuario", command=usermCommand, font=('Arial', 12))
usermanual.place(x=600, y=20)

root.mainloop()