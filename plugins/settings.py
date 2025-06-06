from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from plugins.database.settings_db import save_dump_channel, get_dump_channel
from pyromod import listen

@Client.on_message(filters.command("settings"))
async def settings_menu(client, message: Message):
    buttons = [
        [InlineKeyboardButton("🎯 Set Dump Channel", callback_data="set_dump")],
        [
            InlineKeyboardButton("🎬 Sample Video", callback_data="sample_video"),
            InlineKeyboardButton("❌", callback_data="disable_sample")
        ],
        [
            InlineKeyboardButton("📸 Screenshot", callback_data="screenshot"),
            InlineKeyboardButton("❌", callback_data="disable_screenshot")
        ],
        [
            InlineKeyboardButton("🎀 Dump Mode", callback_data="dump_mode"),
            InlineKeyboardButton("❌", callback_data="disable_dump")
        ],
        [InlineKeyboardButton("✖️ Close ✖️", callback_data="close")]
    ]

    await message.reply_photo(
        photo="https://graph.org/file/53bab5e049a9b0133c354-b8767e238320087219.jpg",
        caption=f"Hey ➤ `{message.from_user.first_name}`\n\nHere You Can Change Or Configure Your Settings",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query()
async def settings_callback(client, query: CallbackQuery):
    data = query.data

    if data == "set_dump":
        await query.message.edit_text("Send me the dump channel ID (like `-1001234567890`).")
    elif data == "sample_video":
        await query.message.edit_text("Send the sample video you want to set.")
    elif data == "disable_sample":
        await query.message.edit_text("Sample Video Disabled.")
    elif data == "screenshot":
        await query.message.edit_text("Screenshot feature enabled.")
    elif data == "disable_screenshot":
        await query.message.edit_text("Screenshot Disabled.")
    elif data == "dump_mode":
        await query.message.edit_text("Choose Dump Mode:\n- Private\n- Public")
    elif data == "disable_dump":
        await query.message.edit_text("Dump Mode Disabled.")
    elif data == "close":
        await query.message.delete()
    else:
        await query.answer("Unknown option selected.", show_alert=True)

@Client.on_message(filters.text & filters.private)
async def receive_dump_channel(client, message: Message):
    if message.reply_to_message and "Send me the dump channel ID" in message.reply_to_message.text:
        channel_id = message.text.strip()
        await save_dump_channel(message.from_user.id, channel_id)
        await message.reply_text(f"✅ Dump Channel set to `{channel_id}`")
