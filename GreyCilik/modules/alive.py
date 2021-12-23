import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from GreyCilik.events import register
from GreyCilik import telethn as tbot


PHOTO = "https://telegra.ph/file/09f3f39dd43de5b66d538.jpg"

@register(pattern=("/alive"))
async def awake(event):
  GREY = f"**Hai [{event.sender.first_name}](tg://user?id={event.sender.id}), Aku Grey Cilik.** \n\n"
  GREY += "⚪ **Saya Akan Bekerja untuk Grup Anda** \n\n"
  GREY += f"⚪ **Tuan Saya : [Lord](https://t.me/greyvbss)** \n\n"
  GREY += f"⚪ **Library Version :** `{telever}` \n\n"
  GREY += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  GREY += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  GREY += "**Terima Kasih Telah Menambahkan Saya Di Sini❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/GreyCilikbot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/greynihsupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=GREY,  buttons=BUTTON)
