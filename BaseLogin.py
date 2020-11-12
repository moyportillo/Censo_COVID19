
import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27017/")

database = connection["miCliente"]

miTabla = database["Login"]

def insertar_Datos(data):
	json_Completo = miTabla.insert_one(data)
	return json_Completo.inserted_id

def buscar_usuario(id):
	data = miTabla.find_one({'usuario': id})
	return data