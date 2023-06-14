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
            "image_url": "",
        }
        newShanyrak = self.database["shanyraks"].insert_one(payload)
        return newShanyrak.inserted_id

    def get_shanyrakObj_by_id(self, shanyrak_id):
        return self.database["shanyraks"].find_one({"_id": ObjectId(shanyrak_id)})

    def get_shanyrak_info(self, shanyrak_id):
        item = self.database["shanyraks"].find_one({"_id": ObjectId(shanyrak_id)})
        media = []
        media = item["image_url"].strip().split(" ")
        print(media)
        payload = {
            "type": item["type"],
            "price": item["price"],
            "address": item["address"],
            "area": item["area"],
            "rooms_count": item["rooms_count"],
            "description": item["description"],
            "user_id": item["user_id"],
            "media": media,
        }
        return payload

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

    def add_image_to_shanyrak(self, shanyrak_id: str, image_url: str):
        curr = ShanyraksRepository.get_shanyrakObj_by_id(self, shanyrak_id)
        currStr = curr["image_url"]
        if image_url in currStr:
            return -1
        payload = {"image_url": str(currStr + " " + image_url)}
        self.database["shanyraks"].update_one(
            {"_id": ObjectId(shanyrak_id)}, {"$set": payload}
        )
        return 0
