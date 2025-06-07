from config import Config
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(Config.DB_URL)
db = client[Config.DB_NAME]
settings_col = db["settings"]

async def save_dump_channel(user_id: int, channel_id: str):
    await settings_col.update_one(
        {"_id": user_id},
        {"$set": {"dump_channel": channel_id}},
        upsert=True
    )

async def get_dump_channel(user_id: int):
    user_data = await settings_col.find_one({"_id": user_id})
    return user_data.get("dump_channel") if user_data else None
