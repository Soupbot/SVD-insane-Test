from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from YukkiMusic import app

def blast_markup():
    upl = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=("Blast!"),callback_data=f"blast")]
        ]
    )
    return upl

def open_me_markup():
    dei = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=("🌻 • ⃤•  ᴏᴘᴇɴ ᴍᴇ ! • ⃤• 🌞"),callback_data=f"open_me")]            
        ]
    )
    return dei

def surprise_markup():
    oi = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=("🥱 • ⃤•  Sυɾ-Pɾιȥҽ ! • ⃤• 🥴"),callback_data=f"surprise")]
        ]
    )
    return oi

def click_me_markup():
    hey = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=("☕️ •̴ ⃤̴•̴  C̴l̴i̴c̴k̴-̴M̴e̴ ! •̴ ⃤̴•̴  🍔"),callback_data=f"click_me")]
        ]
    )
    return hey

def close_me_markup():
    oii = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=("🌜• ⃤•  ｃĻ𝕠รє-Μ𝐞 ! • ⃤• 🌝"),callback_data=f"close_me")]
        ]
    )
    return oii
