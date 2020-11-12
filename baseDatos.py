#incorporar las librerias de la base de datos
import pymongo
#Conectar a la base de datos

connection = pymongo.MongoClient("mongodb://localhost:27017/")

# Crear nueva base de datos

database = connection["miCliente"]

#Crear un nueva coleccion

miTabla = database["persona"]

#Funcion para insertar datos en la tabla

#print(miTabla.count_documents({}))

for documento in miTabla.find({}):
	print(documento)

def insertar_Datos(data):
	json_Completo = miTabla.insert_one(data)
	return json_Completo.inserted_id

#funcion para actualizar datos de la tabla

def actualizar_Datos(id, data):
	json_Completo = miTabla.update_one({'identidad': id}, {"$set": data}, upsert=True)
	return json_Completo.acknowledged

#funcion para eliminar datos de la tabla

def eliminar_Datos(id):
	json_Completo = miTabla.delete_one({'identidad': id})
	return json_Completo.acknowledged

#funcion para buscar una fila

def buscar_Dato(id):
	data = miTabla.find_one({'identidad': id})
	return data

#Cerrar la Base de Datos

connection.close()