from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

# Your MongoDB connection URI
uri = "mongodb+srv://manaskhatri75_db_user:khatri123@cluster0.rf8r2gi.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server securely
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)