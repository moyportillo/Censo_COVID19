from tkinter import * 
from tkinter import messagebox
import os
from BaseLogin import insertar_Datos, buscar_usuario


#Aquí se crea la ventana principal.
def v_inicio():
    global ventanaPrincipal
    color="DarkGrey"
    ventanaPrincipal = Tk()
    ventanaPrincipal.geometry("300x300") #Dimensiones de ventana.
    ventanaPrincipal.title("LOGIN") #Titulo ventana
    Label(text="Seleccione", background="#90EE90", width="30", height="2", font=("Calibri", 14)).pack()
    Label(text="").pack()
    Button(text="Ingresar", height="2", width="30", background=color, command=login).pack() # .pack() = Organiza los widgets en bloques antes de colocarlos en el widget principal.
    Label(text="").pack()
    Button(text="Registrar", height="2", width="30", background=color, command=registro).pack()
    Label(text="").pack()
    ventanaPrincipal.mainloop()

#Aquí creamos ventana de Registro
def registro():
    global ventanaRegistro
    ventanaRegistro = Toplevel(ventanaPrincipal)
    ventanaRegistro.title("REGISTRO")
    ventanaRegistro.geometry("300x250")
 
    global nombreUsuario
    global contrasena
    global entradaombre
    global entradaContrasena
    nombreUsuario= StringVar() 
    contrasena = StringVar() 
 
    Label(ventanaRegistro, text="Ingrese sus datos\n", bg="LightGreen").pack()
    nombre = Label(ventanaRegistro, text="Usuario * ")
    nombre.pack()
    entradaNombre = Entry(ventanaRegistro, textvariable=nombreUsuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entradaNombre.pack()
    contra = Label(ventanaRegistro, text="Contraseña * ")
    contra.pack()
    entradaContrasena = Entry(ventanaRegistro, textvariable=contrasena, show='*') #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entradaContrasena.pack()
    Label(ventanaRegistro, text="").pack()

    def agregar_Usuario():
        if entradaNombre.get()!="" and entradaContrasena.get()!="":
            vector = {"usuario": entradaNombre.get(), "contra": entradaContrasena.get()}
            insertar_Datos(vector)
            messagebox.showinfo(title="Registro", message="Guadordado Exitosamente en Registro")
            ventanaRegistro.destroy()
        else:
            messagebox.showerror(title="Registro", message="Falta de informacion en Registro")
            ventanaRegistro.destroy()

    Button(ventanaRegistro, text="Registrarse", width=10, height=1, bg="LightGreen", command = agregar_Usuario).pack() #Este botón se dirigira a la funcion registroUsuario

#Aquí creamos Ventana de Login
def login():
    global ventanaLogin
    global verificarUsuario
    global verificarContra
    global entLoginUsuario
    global entLoginContra

    ventanaLogin = Toplevel(ventanaPrincipal)
    ventanaLogin.title("INGRESO A LA CUENTA")
    ventanaLogin.geometry("300x250")
    Label(ventanaLogin, text="Ingrese Nombre de Usuario y Contraseña").pack()
    Label(text="").pack()

    verificarUsuario = StringVar()
    verificarContra = StringVar()

    Label(ventanaLogin, text="Usuario * ").pack()
    entLoginUsuario = Entry(ventanaLogin, textvariable= verificarUsuario)
    entLoginUsuario.pack()
    Label(ventanaLogin, text="").pack()
    Label(ventanaLogin, text="Contraseña * ").pack()
    entLoginContra = Entry(ventanaLogin, textvariable= verificarContra, show= '*')
    entLoginContra.pack()
    Label(ventanaLogin, text="").pack()
    def verificacion_Login():
        usr = buscar_usuario(entLoginUsuario.get())
        if  usr != None:
            if usr["contra"] == entLoginContra.get():
                ventanaLogin.destroy()
                ventanaPrincipal.destroy()
                os.system('python menu.py')
            else:
                messagebox.showerror(title="Registro", message="Error en ingresar a la sesion")
                ventanaLogin.destroy()
        else:
            messagebox.showerror(title="Registro", message="Error en ingresar a la sesion")
            ventanaLogin.destroy()
            
    Button(ventanaLogin, text="Ingresar", width=10, height=1, command = verificacion_Login).pack()
v_inicio()