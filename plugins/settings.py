
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

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
        photo="",  # Replace with actual image URL if needed
        caption=f"Hey ➤ `{message.from_user.first_name}`\n\nHere You Can Change Or Configure Your Settings",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query()
async def callback_handler(client, callback_query):
    data = callback_query.data

    if data == "set_dump":
        await callback_query.answer("Send me the channel username (with @)", show_alert=True)
    elif data == "sample_video":
        await callback_query.answer("Sample Video Enabled!", show_alert=True)
    elif data == "disable_sample":
        await callback_query.answer("Sample Video Disabled!", show_alert=True)
    elif data == "screenshot":
        await callback_query.answer("Screenshot Enabled!", show_alert=True)
    elif data == "disable_screenshot":
        await callback_query.answer("Screenshot Disabled!", show_alert=True)
    elif data == "dump_mode":
        await callback_query.answer("Dump Mode Enabled!", show_alert=True)
    elif data == "disable_dump":
        await callback_query.answer("Dump Mode Disabled!", show_alert=True)
    elif data == "close":
        await callback_query.message.delete()
