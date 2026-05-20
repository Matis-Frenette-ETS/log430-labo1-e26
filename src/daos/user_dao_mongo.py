"""
User DAO Mongo (Data Access Object)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from models.user import User
from bson import ObjectId

class UserDAOMongo:
    def __init__(self):
        try:
            env_path = ".env"
            print(os.path.abspath(env_path))
            load_dotenv(dotenv_path=env_path)

            db_host = os.getenv("MONGODB_HOST")
            db_port = int(os.getenv("MONGO_PORT"))
            db_name = os.getenv("MONGO_DB_NAME")
            db_user = os.getenv("DB_USERNAME")
            db_pass = os.getenv("DB_PASSWORD")

            uri = f"mongodb://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}?authSource=admin"

            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            self.users_collection = self.db["users"] 
        except FileNotFoundError:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))
    
    def select_all(self):
        """Return a list of users matching the filter"""
        users = []
        for u in self.users_collection.find({}):
            users.append(User((u["_id"]), u["name"], u["email"]))
        
        return users

    def insert(self, user):
        """Insert a new user document"""
        result = self.users_collection.insert_one({
            "name": user.name,
            "email": user.email
        })
        return str(result.inserted_id)

    def update(self, user):
        """Update a user by _id"""
        result = self.users_collection.update_one(
            {"_id": ObjectId(user.id)},
            {"$set": {"name": user.name, "email": user.email}}
        )
        pass

    def delete(self, user_id):
        """Delete a user by _id"""
        result = self.users_collection.delete_one({"_id": ObjectId(user_id)})
        pass

    def delete_all(self):
        pass

