from customtkinter import *
import os

#UI

#placeholder

user = "Potato"
passw = "1234"

set_appearance_mode("system")
set_default_color_theme("dark-blue")

root = CTk()
root.title("UI (Nombre temporal, favor cambiar)")
root.resizable(False, False)
root.geometry("1280x720")

listframe = CTkFrame(root, width=880, height=640, border_width=5)
listframe.place_forget()

userVar = StringVar()
passVar = StringVar()

userLabel = CTkLabel(root, text="Usuario:", font=('Arial', 12))
userLabel.place(x=527, y=250)
passLabel = CTkLabel(root, text="Contraseña:", font=('Arial', 12))
passLabel.place(x=507, y=290)

userTextBox = CTkEntry(root, textvariable=userVar, font=('Arial', 12))
userTextBox.place(x=600, y=250)
passTextBox = CTkEntry(root, textvariable=passVar, font=('Arial', 12), show="*")
passTextBox.place(x=600, y=290)

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
nameLabel.place_forget()
nameTB = CTkEntry(root, textvariable=nameVar, font=('Arial', 12))
nameTB.place_forget()

idLabel = CTkLabel(root, text="ID del Medicamento:", font=('Arial', 12))
idLabel.place_forget()
idTB = CTkEntry(root, textvariable=idVar, font=('Arial', 12))
idTB.place_forget()

cantidadLabel = CTkLabel(root, text="Cantidad:", font=('Arial', 12))
cantidadLabel.place_forget()
cantidadTB = CTkEntry(root, textvariable=cantVar, font=('Arial', 12))
cantidadTB.place_forget()

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
comprar.place_forget()
añadir = CTkButton(root, text="Añadir Medicamento a la Lista", command=añaCommand, font=('Arial', 12))
añadir.place_forget()
vender = CTkButton(root, text="Vender Medicamento", command=vendCommand, font=('Arial', 12))
vender.place_forget()
usermanual = CTkButton(root, text="Manual de Usuario", command=usermCommand, font=('Arial', 12))
usermanual.place(x=20, y=20)

#En listframe va la lista del inventario, no supe como implementar un ejemplo
#Por lo mismo, no sé hacer que al hacer click en un elemento de la lista, se copien y peguen el nombre y el id, tampoco sé como hacer que los botones funcionen
#Podriamos cambiar las palabras comprar y vender por añadir y eliminar, lo dejo a su gusto
#También se podría agregar un historial de sesiones pero ya es mucho pedir imo xd

def logoutCommand():
        listframe.place_forget()
        comprar.place_forget()
        añadir.place_forget()
        vender.place_forget()
        nameLabel.place_forget()
        nameTB.place_forget()
        idLabel.place_forget()
        idTB.place_forget()
        cantidadLabel.place_forget()
        cantidadTB.place_forget()
        logout.place_forget()
        toplevel = CTkToplevel()
        toplevel.grab_set()
        toplevel.title("UI (Nombre temporal, favor cambiar)")
        toplevel.resizable(False, False)
        toplevel.geometry("426x240")
        tlLabel = CTkLabel(toplevel, text=("Se ha cerrado sesión"), font=('Arial', 12))
        tlLabel.place(x=158, y=90)
        def destro():
            toplevel.destroy()
        tlButton = CTkButton(toplevel, text="Aceptar", font=("Arial", 12), command=destro)
        tlButton.place(x=145, y=150)
        userLabel.place(x=527, y=250)
        passLabel.place(x=507, y=290)
        userTextBox.place(x=600, y=250)
        passTextBox.place(x=600, y=290)
        access.place(x=580, y=370)
        usermanual.place(x=20, y=20)
        
logout = CTkButton(root, text="Cerrar Sesión", command=logoutCommand, font=('Arial', 12))
logout.place_forget()

def accessCommand():
    if user == userTextBox.get() and passw == passTextBox.get():
        userLabel.place_forget()
        passLabel.place_forget()
        userTextBox.place_forget()
        userTextBox.delete(0, 'end')
        passTextBox.place_forget()
        passTextBox.delete(0, 'end')
        access.place_forget()
        listframe.place(x= 20, y = 70)
        comprar.place(x=20, y=20)
        añadir.place(x=380, y=20)
        vender.place(x=200, y=20)
        usermanual.place(x=600, y=20)
        nameLabel.place(x=920, y=180)
        nameTB.place(x=1080, y=180)
        idLabel.place(x=950, y=230)
        idTB.place(x=1080, y=230)
        cantidadLabel.place(x=1010, y=280)
        cantidadTB.place(x=1080, y=280)
        logout.place(x=1130 ,y= 680)
    else: 
        toplevel = CTkToplevel()
        toplevel.grab_set()
        toplevel.title("Error")
        toplevel.resizable(False, False)
        toplevel.geometry("426x240")
        tlLabel = CTkLabel(toplevel, text=("Usuario o contraseña erroneos, por favor intente nuevamente"), font=('Arial', 12))
        tlLabel.place(x=45, y=77)
        def destro():
            toplevel.destroy()
        tlButton = CTkButton(toplevel, text="Aceptar", font=("Arial", 12), command=destro)
        tlButton.place(x=145, y=137)

access = CTkButton(root, text="Acceder", command=accessCommand, font=('Arial', 12))
access.place(x=580, y=370)

root.mainloop()