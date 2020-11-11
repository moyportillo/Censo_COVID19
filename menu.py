#Importamos la libreria que nos proporciona para la parte grafica
from tkinter import *
from tkinter import ttk, messagebox
from baseDatos import insertar_Datos, buscar_Dato, actualizar_Datos, eliminar_Datos

#Contruimos la raiz o el objeto
raiz=Tk()

#Aqui le agragamos un titulo a la ventana
raiz.title("Censo 2020 - Combatiendo el Covid19 Juntos")

#Aqui de ofrecemos el permiso de redimencionar la ventana 
raiz.resizable(0,0)

#Aqui cambiamos el tamanio de la ventana ancho por alto
raiz.geometry("650x720")

#Crear el frame
miFrame=Frame(raiz)

#El frame tenemos que empaquetarlo
#Aqui unimos el Frame con la raiz
miFrame.pack()

miImagen = PhotoImage(file="Image/rompecabezas.png")

#Aqui agregamos un label para el menu
Label(miFrame, image=miImagen).grid(row=0, column=0)
Label(miFrame, text="Menu Principal", font=("Comic Sans MS", 26)).grid(row=0, column=1)

#aqui damos tamanio al frame no a la raiz
#miFrame.config(width="650", height="720")
ancho=25
alto=5

#Funcion para Agragar Censo
def Agregar_Censo():
	miFrame = Toplevel(raiz)
	miFrame.geometry("550x500")
	miFrame.resizable(0,0)
	Label(miFrame, image=miImagen).grid(row=0, column=0)
	Label(miFrame, text="Nuevo Censo", font=("Comic Sans MS", 26)).grid(row=0, column=1)

	#Parte de TextBox
	Label(miFrame, text="Identidad", font=("Comic Sans MS", 18)).grid(row=1, column=0, padx=5)
	identidad=ttk.Entry(miFrame,font=('arial',20,'bold'),width=15)
	identidad.grid(row=1, column=1)


	Label(miFrame, text="Nombre Completo", font=("Comic Sans MS", 18)).grid(row=2, column=0, padx=5)
	nombre =Entry(miFrame,font=('arial',20,'bold'),width=15)
	nombre.grid(row=2, column=1)

	Label(miFrame, text="Direccion: ", font=("Comic Sans MS", 18)).grid(row=3, column=0, padx=5)
	direccion =Entry(miFrame,font=('arial',20,'bold'),width=15)
	direccion.grid(row=3, column=1)

	Label(miFrame, text="Correo", font=("Comic Sans MS", 18)).grid(row=4, column=0, padx=5)
	correo =Entry(miFrame,font=('arial',20,'bold'),width=15)
	correo.grid(row=4, column=1)

	Label(miFrame, text="Telefono", font=("Comic Sans MS", 18)).grid(row=5, column=0, padx=5)
	telefono =Entry(miFrame,font=('arial',20,'bold'),width=15)
	telefono.grid(row=5, column=1)

	Label(miFrame, text="Preguntas", font=("Comic Sans MS", 26)).grid(row=6, column=1)
	Label(miFrame, text="A Presentado Sintomas?", font=("Comic Sans MS", 18)).grid(row=7, column=0, padx=5)

	#Parte de Radio Boton
	var = IntVar()

	R1 = Radiobutton(miFrame, text="Si", variable=var, value=1, font=('arial',18,'bold'), width=5, height=3)
	R1.grid(row=8, column=0, padx=5)
	R2 = Radiobutton(miFrame, text="No", variable=var, value=2, font=('arial',18,'bold'), width=5, height=3)
	R2.grid(row=8, column=1, padx=5)

	if R1 == 1:
		resp = "Si"
	else:
		resp = "No"

	#Parte de ComboBox
	Label(miFrame, text="Seleccione Triaje mas cerca: ", font=("Comic Sans MS", 18)).grid(row=9, column=0, padx=5)
	num = StringVar()
	cbTriaje = ttk.Combobox(miFrame, values=["INFOP", "UNAH", "La Mayangle", "Centro Civico", "UNICAH", "Iglesia CCI"], font=('Comic Sans MS', 12),width=30, textvariable=num)
	cbTriaje.grid(row=9, column=1, padx=5)
	cbTriaje.current()



	#entrada = {"identidad":identidad.get(), "nombre":nombre.get(), "direccion":direccion.get(), "correo":correo.get(), "telefono":telefono.get(), "sintomas": radio, "triaje":cbTriaje.get()}
	def press_Send():
		if identidad.get() != "":
			vector = {"identidad": identidad.get(), "nombre": nombre.get(), "direccion": direccion.get(), "correo": correo.get(), "telefono": telefono.get(), "sintomas": resp, "triaje": cbTriaje.get()}
			insertar_Datos(vector)
			miFrame.destroy()
		else:
			Label(miFrame, text="No se pudo Ingresar la informacion por falta de Datos", font=("Comic Sans MS", 12)).grid(row=11, column=1, padx=5)
	#botones
	enviar = Button(miFrame, text="Enviar",fg='black', bg='#DCEDC8', font=("Comic Sans MS", 18), width=10, command=press_Send).grid(row=10, column=1, padx=5, pady=25)

	#Button(miFrame, text="Salir",fg='black', bg='#B3E5FC', font=("Comic Sans MS", 18), width=10).grid(row=10, column=0, padx=5, pady=25)



#Funcion para buscar censo
def Buscar_Censo():
	miFrame = Toplevel(raiz)
	miFrame.geometry("550x500")
	miFrame.resizable(0,0)
	Label(miFrame, image=miImagen).grid(row=0, column=0)
	Label(miFrame, text="Buscar Censo", font=("Comic Sans MS", 26)).grid(row=0, column=1)

	#Parte de TextBox
	Label(miFrame, text="Ingrese Identidad", font=("Comic Sans MS", 18)).grid(row=1, column=0, padx=5)
	identidad=Entry(miFrame,font=('arial',20,'bold'),width=15)
	identidad.grid(row=1, column=1)

	def press_Seach():
		if identidad.get() != "":
			busqueda = buscar_Dato(identidad.get())
			if busqueda != None:
				Label(miFrame, text="Datos de censo", font=("Comic Sans MS", 26, 'bold')).grid(row=2, column=1, padx=5)
				Label(miFrame, text="Nombre Completo", font=("Comic Sans MS", 18, 'bold')).grid(row=3, column=0, padx=5)
				Label(miFrame, text=busqueda['nombre'], font=("Comic Sans MS", 18)).grid(row=3, column=1, padx=5)
				Label(miFrame, text="Direccion", font=("Comic Sans MS", 18, 'bold')).grid(row=4, column=0, padx=5)
				Label(miFrame, text=busqueda['direccion'], font=("Comic Sans MS", 18)).grid(row=4, column=1, padx=5)
				Label(miFrame, text="Correo", font=("Comic Sans MS", 18, 'bold')).grid(row=5, column=0, padx=5)
				Label(miFrame, text=busqueda['correo'], font=("Comic Sans MS", 18)).grid(row=5, column=1, padx=5)
				Label(miFrame, text="Telefono", font=("Comic Sans MS", 18, 'bold')).grid(row=6, column=0, padx=5)
				Label(miFrame, text=busqueda['telefono'], font=("Comic Sans MS", 18)).grid(row=6, column=1, padx=5)
				Label(miFrame, text="Sintomas", font=("Comic Sans MS", 18, 'bold')).grid(row=7, column=0, padx=5)
				Label(miFrame, text=busqueda['sintomas'], font=("Comic Sans MS", 18)).grid(row=7, column=1, padx=5)
				Label(miFrame, text="Triaje Cercano", font=("Comic Sans MS", 18, 'bold')).grid(row=8, column=0, padx=5)
				Label(miFrame, text=busqueda['triaje'], font=("Comic Sans MS", 18)).grid(row=8, column=1, padx=5)

				Button(miFrame, text="Menu",fg='black', bg='#B3E5FC', font=("Comic Sans MS", 18), width=10, command=miFrame.destroy).grid(row=9, column=1, padx=5, pady=25)
			else:
			 	Label(miFrame, text="Error: Registro No encontrado", fg="red", font=("Comic Sans MS", 14, 'bold')).grid(row=3, column=1, padx=5)
		else:
			Label(miFrame, text="Error: Campo vacio", fg="red", font=("Comic Sans MS", 14, 'bold')).grid(row=3, column=1, padx=5)

	Button(miFrame, text="Buscar",fg='black', bg='#B3E5FC', font=("Comic Sans MS", 18), width=10, command=press_Seach).grid(row=1, column=2, padx=5, pady=25)

#Funcion para Modificar Censo
def Modificar_Censo():
	miFrame = Toplevel(raiz)
	miFrame.geometry("600x600")
	miFrame.resizable(0,0)

	Label(miFrame, image=miImagen).grid(row=0, column=0)
	Label(miFrame, text="Modificar Censo", font=("Comic Sans MS", 26)).grid(row=0, column=1)

	#Parte de TextBox
	Label(miFrame, text="Ingrese Identidad", font=("Comic Sans MS", 18)).grid(row=1, column=0, padx=5)
	modificar=Entry(miFrame,font=('arial',20,'bold'),width=15)
	modificar.grid(row=1, column=1)
	
	def mostrar_Datos():
		if modificar.get() != "":
			vector = buscar_Dato(modificar.get())	
			if vector != None:
			
				#Parte de TextBox
				Label(miFrame, text="Identidad", font=("Comic Sans MS", 18)).grid(row=2, column=0, padx=5)
				Label(miFrame, text=vector["identidad"], font=("Comic Sans MS", 18)).grid(row=2, column=1, padx=5)

				Label(miFrame, text="Nombre Completo", font=("Comic Sans MS", 18)).grid(row=3, column=0, padx=5)
				nombre =Entry(miFrame,font=('arial',20,'bold'),width=15)
				nombre.insert(0, vector["nombre"])
				nombre.grid(row=3, column=1)

				Label(miFrame, text="Direccion: ", font=("Comic Sans MS", 18)).grid(row=4, column=0, padx=5)
				direccion =Entry(miFrame,font=('arial',20,'bold'),width=15)
				direccion.insert(0, vector["direccion"])
				direccion.grid(row=4, column=1)

				Label(miFrame, text="Correo", font=("Comic Sans MS", 18)).grid(row=5, column=0, padx=5)
				correo =Entry(miFrame,font=('arial',20,'bold'),width=15)
				correo.insert(0, vector["correo"])
				correo.grid(row=5, column=1)

				Label(miFrame, text="Telefono", font=("Comic Sans MS", 18)).grid(row=6, column=0, padx=5)
				telefono =Entry(miFrame,font=('arial',20,'bold'),width=15)
				telefono.insert(0, vector["telefono"])
				telefono.grid(row=6, column=1)

				Label(miFrame, text="Preguntas", font=("Comic Sans MS", 26)).grid(row=7, column=1)
				Label(miFrame, text="A Presentado Sintomas?", font=("Comic Sans MS", 18)).grid(row=8, column=0, padx=5)

				#Parte de Radio Boton
				var = IntVar()

				R1 = Radiobutton(miFrame, text="Si", variable=var, value=1, font=('arial',18,'bold'), width=5, height=3)
				R1.grid(row=9, column=0, padx=5)
				R2 = Radiobutton(miFrame, text="No", variable=var, value=2, font=('arial',18,'bold'), width=5, height=3)
				R2.grid(row=9, column=1, padx=5)

				if R1 == 1:
					resp = "Si"
				else:
					resp = "No"

				#Parte de ComboBox
				Label(miFrame, text="Seleccione Triaje mas cerca: ", font=("Comic Sans MS", 18)).grid(row=10, column=0, padx=5)
				num = StringVar()
				cbTriaje = ttk.Combobox(miFrame, values=["INFOP", "UNAH", "La Mayangle", "Centro Civico", "UNICAH", "Iglesia CCI"], font=('Comic Sans MS', 18), width=25, state='readonly')
				cbTriaje.grid(row=10, column=1, padx=5)
				cbTriaje.set(vector["triaje"])

				def modificar_Data():
					vector = {"identidad": modificar.get(), "nombre": nombre.get(), "direccion": direccion.get(), "correo": correo.get(), "telefono": telefono.get(), "sintomas": resp, "triaje": cbTriaje.get()}
					actualizar_Datos(modificar.get(), vector)
					miFrame.destroy()

				btnModificar = Button(miFrame, text="modificar",fg='black', bg='#FFE0B2', font=("Comic Sans MS", 18), width=10, command=modificar_Data).grid(row=12, column=1, padx=1, pady=25)
			else:
				modificar.insert(0,"")
		else:
			Label(miFrame, text="Error: Campo vacio", fg="red", font=("Comic Sans MS", 14, 'bold')).grid(row=3, column=1, padx=5)


	btnBuscar = Button(miFrame, text="Buscar",fg='black', bg='#FFE0B2', font=("Comic Sans MS", 18), width=10, command=mostrar_Datos).grid(row=1, column=2, padx=1, pady=25)

def eliminar_data():
	miFrame = Toplevel(raiz)
	miFrame.geometry("650x200")
	miFrame.resizable(0,0)

	Label(miFrame, image=miImagen).grid(row=0, column=0)
	Label(miFrame, text="Eliminar Censo", font=("Comic Sans MS", 26)).grid(row=0, column=1)

	#Parte de TextBox
	Label(miFrame, text="Ingrese Identidad", font=("Comic Sans MS", 18)).grid(row=1, column=0, padx=5)
	eliminar=Entry(miFrame,font=('arial',20,'bold'),width=15)
	eliminar.grid(row=1, column=1)

	Label(miFrame, text="Desea Realmente eliminar los datos del Registro", font=("Comic Sans MS", 14)).grid(row=2, column=1)

	def delete_Datos_Censo():
		if eliminar.get() != "" and buscar_Dato(eliminar.get()) != None:
			eliminar_Datos(eliminar.get())
			miFrame.destroy()
		else:
			Label(miFrame, text="Error: Datos no encontrados", fg="red", font=("Comic Sans MS", 14, 'bold')).grid(row=3, column=1, padx=5)

	btnBuscar = Button(miFrame, text="Eliminar",fg='black', bg='#FFCDD2', font=("Comic Sans MS", 18), width=10, command=delete_Datos_Censo).grid(row=1, column=2, padx=1, pady=25)
	

Button(miFrame, text="Nuevo Censo",fg='black', bg='#DCEDC8', font=("Comic Sans MS", 18), width=ancho, height=alto, command=Agregar_Censo).grid(row=1, column=0, padx=10, pady=15)
Button(miFrame, text="Buscar Censo",fg='black', bg='#B3E5FC', font=("Comic Sans MS", 18), width=ancho, height=alto, command=Buscar_Censo).grid(row=1, column=1, padx=10, pady=15)
Button(miFrame, text="Modificar Censo",fg='black', bg='#FFE0B2', font=("Comic Sans MS", 18), width=ancho, height=alto, command=Modificar_Censo).grid(row=2, column=0, padx=10, pady=15)
Button(miFrame, text="Eliminar Censo",fg='black', bg='#FFCDD2', font=("Comic Sans MS", 18), width=ancho, height=alto, command=eliminar_data).grid(row=2, column=1, padx=10, pady=15)
Button(miFrame, text="Salir",fg='black', bg='white', font=("Comic Sans MS", 18), width=ancho, height=alto, command=miFrame.quit).grid(row=3, column=0, padx=10, pady=15)

#Utilizamos un metodo de la libreria para hacer un bucle infinito para poder mantener ejecutando la ventana
raiz.mainloop()


