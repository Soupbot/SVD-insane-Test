from InsaneMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions, Message
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from InsaneMusic.utils.inline.blast import blast_markup


spam_chats = []

TAGMES = ["hi", "hello", "good morning", "good evening", "good night", "yellarum yenna pandringa","vetiya iruntha vc ku vanga work la irrunthalum vanga😉"]
EMOJI = ["😊", "👋", "🌞", "🌙","❤️", "💚", "💙", "💜", "🖤"]


@app.on_message(filters.command(["tagus"], prefixes=["/", "@", "!"]))
async def tagme_handler(client, message: Message):
    chat_id = message.chat.id
    if chat_id in spam_chats:
        await message.reply("The tagme command is already running in this chat.")
        return

    if message.reply_to_message and message.text:
        return await message.reply("/tagus ** ᴛʀʏ ᴛʜɪs ɴᴇxᴛ ᴛɪᴍᴇ ғᴏʀ ᴛᴀɢɢɪɴɢ...*")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagus **ᴛʀʏ ᴛʜɪs ᴏʀ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ...**")
    else:
        return await message.reply("/tagus **ᴛʀʏ ᴛʜɪs ᴏʀ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ...**")
              
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""

    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break

        if usr.user.is_bot:
            continue

        usrnum += 1
        #usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "
        usrtxt += f"{usr.user.mention}"

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                markup = blast_markup()                    
                await message.reply_text(
                          txt, 
                          reply_markup=markup
                )
            elif mode == "text_on_reply":
                markup = InlineKeyboardMarkup(
                       [
                              [InlineKeyboardButton(text="Blast!",callback_data="blast")]
                       ]
                )
                await msg.reply(f"{random.choice(EMOJI)} {usrtxt}", reply_markup=markup)

            # Generate a random sleep time between 10 and 30 seconds(0 and 5 seconds)
            sleep_time = random.randint(0, 5)
            await asyncio.sleep(sleep_time)

            usrnum = 0
            usrtxt = ""

    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_callback_query()
async def on_callback_query(client, event):
    print("Callback query received:", event.data)
    if event.data == "blast":
              print("Blast button clicked!")
              morning_quote = f"Good morning {event.from_user.mention}! Here's a beautiful quote to start your day:\n\n""Life is what happens when you're busy making other plans. - John Lennon"                             
              await event.answer()
              await event.message.edit_text(morning_quote)
