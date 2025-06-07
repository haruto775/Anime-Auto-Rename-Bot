from motor.motor_asyncio import AsyncIOMotorClient
from config import DB_URL, DB_NAME

client = AsyncIOMotorClient(DB_URL)
db = client[DB_NAME]
settings_collection = db["UserSettings"]

async def save_dump_channel(user_id: int, channel_id: str):
    await settings_collection.update_one(
        {"user_id": user_id},
        {"$set": {"dump_channel": channel_id}},
        upsert=True
    )

async def get_dump_channel(user_id: int):
    data = await settings_collection.find_one({"user_id": user_id})
    return data.get("dump_channel") if data else None
