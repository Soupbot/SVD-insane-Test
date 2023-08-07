from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from YukkiMusic import app

def blast_markup():
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=("Blast!"),
                    callback_data=f"blast",
                ),

            ]
        ]
    )
    return upl

def open_me_markup():
    dei = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=("Open me!"),
                    callback_data=f"open_me",
                )
            ]
        ]
    )
    return dei
