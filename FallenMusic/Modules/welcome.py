import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram import Client, emoji 
from FallenMusic import app
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ChatPermissions
from pyrogram import filters

@app.on_message(filters.new_chat_members)
async def wel__come(client: Client, message: Message):
	chatid= message.chat.id
	await client.send_message(text=f"- نورت ياا فرتكهه😘🤝️ {message.from_user.mention}\n│ \n└ʙʏ في {message.chat.title}",chat_id=chatid)
	
@app.on_message(filters.left_chat_member)
async def good_bye(client: Client, message: Message):
	chatid= message.chat.id
	await client.send_message(text=f"- مشيت ليه يوحش يلا بسلامات🥲👋\n│ \n└ʙʏ  {message.from_user.mention} ",chat_id=chatid)
	
	
	
	
	
	
	
@app.on_message(
    command(["اوفا","يوسف","جو"])
    & filters.group
  
)
async def kkpp(client, message):
    usr = await client.get_chat("J3_oo")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━𓍹𓋹𓍻⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 🦋⌯⊶𓍹𓋹𓍻━⩺\n\n🧞‍♂️ ¦OMAR :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━𓍹𓋹𓍻⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 🦋⌯⊶𓍹𓋹𓍻━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
