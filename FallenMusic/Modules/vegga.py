import asyncio

import os
import time
import requests
from config import START_IMG
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from FallenMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين هانتر","المطورين","مطورين"])
  
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/efa394c06f92186cd5277.jpg",
        caption=f"""**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 🦋⌯⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين هانتر ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 🦋⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★᚜⎖᳒𝑺𝑨𝑺𝑨𐇲⌯‹♱᚛★", url=f"https://t.me/T_3_A"), 
                 ],[
                    InlineKeyboardButton(
                        "★᚜𝑴𝑨𝑵𝑫𝑶𝑶᚛★", url=f"https://t.me/M_2A_E_S"),
                ],[
                    InlineKeyboardButton(
                        "★𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 🦋⚡", url=f"https://t.me/huntersource"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["ديشا"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("U_7h1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 🦋⌯⊶★━⩺\n\n🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 🦋⌯⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
    
   



