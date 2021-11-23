from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

import requests 

import os


API = "https://apis.xditya.me/lyrics?song="




@Ek.on_message(filters.private & filters.command(["lyrics"]))
async def sng(bot, message):
        hy = await message.reply_text("`🔍Searching 🔎`")
        song = message.text
        chat_id = message.from_user.id
        rpl = lyrics(song) 
        try:
                await hy.delete()
                await Ek.send_message(chat_id, text = rpl, reply_to_message_id = message.message_id
        except requests.ConnectionError as exception:
        	await hy.delete()
        	await message.reply_text(f"I Can't Find A Song With `{song}`", quote = True


def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 Successfully Extracted Lyrics Of {song} 🎶**\n\n\n\n'
        text += f'`{fin["lyrics"]}`'
        text += '\n\n\n**Made With ❤️ By @EKBOTZ_UPDATE**'
        return text


Ek.run()
