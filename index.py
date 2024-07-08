from pymongo import MongoClient

# Reemplaza los valores de la URI con los correctos
uri = "mongodb+srv://ConexionMdb:12345@primercluster.e3mfhgr.mongodb.net/?retryWrites=true&w=majority&appName=PrimerCluster"

# Conexión a MongoDB Atlas
client = MongoClient(uri)

# Crear una base de datos
db = client['provincias_dominicanas']

# Crear una colección
collection = db['provincias']

# Datos de las provincias de la República Dominicana
provincias = [
    {"nombre": "Azua"},
    {"nombre": "Bahoruco"},
    {"nombre": "Barahona"},
    {"nombre": "Dajabón"},
    {"nombre": "Distrito Nacional"},
    {"nombre": "Duarte"},
    {"nombre": "Elías Piña"},
    {"nombre": "El Seibo"},
    {"nombre": "Espaillat"},
    {"nombre": "Hato Mayor"},
    {"nombre": "Hermanas Mirabal"},
    {"nombre": "Independencia"},
    {"nombre": "La Altagracia"},
    {"nombre": "La Romana"},
    {"nombre": "La Vega"},
    {"nombre": "María Trinidad Sánchez"},
    {"nombre": "Monseñor Nouel"},
    {"nombre": "Monte Cristi"},
    {"nombre": "Monte Plata"},
    {"nombre": "Pedernales"},
    {"nombre": "Peravia"},
    {"nombre": "Puerto Plata"},
    {"nombre": "Samaná"},
    {"nombre": "Sánchez Ramírez"},
    {"nombre": "San Cristóbal"},
    {"nombre": "San José de Ocoa"},
    {"nombre": "San Juan"},
    {"nombre": "San Pedro de Macorís"},
    {"nombre": "Santiago"},
    {"nombre": "Santiago Rodríguez"},
    {"nombre": "Santo Domingo"},
    {"nombre": "Valverde"},
]

# Insertar las provincias en la colección
collection.insert_many(provincias)

print("Provincias insertadas Con exito")

# Consultar todas las provincias
provincias = collection.find()

# Imprimir las provincias
print("Listado de Provincias de la República Dominicana:")
for provincia in provincias:
    print(provincia)

