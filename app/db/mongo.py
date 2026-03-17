from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"


client = MongoClient(MONGO_URL)
# Mi base de dato
db = client["mydatabase"]
# Mi "Tabla"
users_collection = db["users"]
