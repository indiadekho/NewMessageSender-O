from pyrogram import Client, filters

API_ ID = 'YOUR API ID'
API_HASH = 'YOUR API HASH'
STRING_SESSION = 'USERBOT STING SESSION'
CHANNEL = 'PRIVATE CHANNEL USERNAME OR ID'

bot = Client(STRING_SESSION, API_ID, API_HASH)


@bot.on_message(filters.incoming & filters.channel & ~filters.chat(CHANNEL))
async def copy(bot, message):
    await message.copy(CHANNEL)


bot.run()
