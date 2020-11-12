from tkinter import * 
import os

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
    Button(ventanaRegistro, text="Registrarse", width=10, height=1, bg="LightGreen", command = registroUsuario).pack() #Este botón se dirigira a la funcion registroUsuario

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
    Button(ventanaLogin, text="Ingresar", width=10, height=1, command = verificarLogin).pack()

#Aquí creamos ventana de verificación de Login
def verificarLogin():
    usuario1 = verificarUsuario.get()
    contrasena1 = verificarContra.get()
    entLoginUsuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entLoginContra.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lstArchivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lstArchivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if clave1 in verifica:
            exitoLogin() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        else:
            noContrasena() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    else:
        noUsuario() #..EJECUTA "no_usuario()".    

#---------------------------------------------------------------------------------
#Ventana de Login finalizado Exitosamente
def exitoLogin():
    global ventanaExito
    ventanaExito = Toplevel(ventanaLogin)
    ventanaExito.title("Exito")
    ventanaExito.geometry("150x150")
    Label(ventanaExito, text="Login finalizado exitosamente.").pack()
    Button(ventanaExito, text="OK", command=ventanaExito.destroy()).pack() #.destroy() Cierre de Ventana

#---------------------------------------------------------------------------------
#VENTANA DE "Contraseña incorrecta". 
def noContrasena():
    global ventanaNoContrasena
    ventanaNoContrasena = Toplevel(ventanaLogin)
    ventanaNoContrasena.title("¡ERROR!")
    ventanaNoContrasena.geometry("150x150")
    Label(ventanaNoContrasena, text = "Contraseña inválida.").pack()
    Button(ventanaNoContrasena, text="OK", command = ventanaNoContrasena.destroy()).pack() #.destroy() Cierre de Ventana
#---------------------------------------------------------------------------------
#VENTANA DE "Usuario no encontrado".
 
def noUsuario():
    global ventanaNoUsuario
    ventananoUsuario = Toplevel(ventanaLogin)
    ventananoUsuario.title("¡ERROR!")
    ventananoUsuario.geometry("150x150")
    Label(ventananoUsuario, text="Usuario no encontrado").pack()
    Button(ventananoUsuario, text="OK", command = ventanaNoUsuario.destroy()).pack() #.destroy() Cierre de Ventana

#REGISTRO USUARIO
def registroUsuario():
 
    usuarioInfo = nombreUsuario.get()
    contrasenaInfo = contrasena.get()
 
    file = open(usuario_info, "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(usuarioInfo + "\n")
    file.write(contrasenaInfo)
    file.close()
 
    entradaNombre.delete(0, END)
    entradaContrasena.delete(0, END)
 
    Label(ventanaRegistro, text="Registro completado con éxito", fg="green", font=("Microsft Sans Serif", 12)).pack()
 
#EJECUCIÓN DE LA VENTANA DE INICIO. 
v_inicio()