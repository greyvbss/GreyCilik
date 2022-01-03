import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from GreyCilik.events import register
from GreyCilik import telethn as tbot


PHOTO = "https://telegra.ph/file/760e7c0afaf6ba3df8ce7.jpg"

@register(pattern=("/alive"))
async def awake(event):
  GREY = f"**Hai [{event.sender.first_name}](tg://user?id={event.sender.id}), Aku Grey Cilik.** \n\n"
  GREY += "⚪ **Saya Akan Bekerja untuk Grup Anda** \n\n"
  GREY += f"⚪ **Tuan Saya : [Lord](https://t.me/reyyvbss)** \n\n"
  GREY += f"⚪ **Library Version :** `{telever}` \n\n"
  GREY += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  GREY += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  GREY += "**Terima Kasih Telah Menambahkan Saya Di Sini❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/GreyCilik_bot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://CilikSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=GREY,  buttons=BUTTON)
