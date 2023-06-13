from bson.objectid import ObjectId
from pymongo.database import Database


class ShanyraksRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_shanyrak(self, user_id: str, shanyrak: dict):
        payload = {
            "user_id": ObjectId(user_id),
            "type": shanyrak["type"],
            "price": shanyrak["price"],
            "address": shanyrak["address"],
            "area": shanyrak["area"],
            "rooms_count": shanyrak["rooms_count"],
            "description": shanyrak["description"],
        }
        newShanyrak = self.database["shanyraks"].insert_one(payload)
        return newShanyrak.inserted_id

    def get_shanyrak_by_id(self, shanyrak_id):
        return self.database["shanyraks"].find_one({"_id": ObjectId(shanyrak_id)})

    def update_shanyrak(self, shanyrak_id: str, input: dict):
        payload = {
            "type": input["type"],
            "price": input["price"],
            "address": input["address"],
            "area": input["area"],
            "rooms_count": input["rooms_count"],
            "description": input["description"],
        }
        self.database["shanyraks"].update_one(
            {"_id": ObjectId(shanyrak_id)},
            {"$set": payload},
        )

    def delete_shanyrak(self, shanyrak_id):
        self.database["shanyraks"].delete_one({"_id": ObjectId(shanyrak_id)})
