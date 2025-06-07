from config import Config
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(Config.DB_URL)

client = MongoClient(Config.DB_URL)
db = client[Config.DB_NAME]
settings_collection = db["UserSettings"]

async def save_dump_channel(user_id: int, channel_id: str):
    settings_collection.update_one(
        {"user_id": user_id},
        {"$set": {"dump_channel": channel_id}},
        upsert=True
    )

async def get_dump_channel(user_id: int):
    data = settings_collection.find_one({"user_id": user_id})
    return data.get("dump_channel") if data else None
