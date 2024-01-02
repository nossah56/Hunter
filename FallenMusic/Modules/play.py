# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio
import os

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError, UnMuteNeeded
from pytgcalls.types import AudioPiped, HighQualityAudio
from youtube_search import YoutubeSearch

from config import DURATION_LIMIT
from FallenMusic import (
    ASS_ID,
    ASS_MENTION,
    ASS_NAME,
    ASS_USERNAME,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    app,
    app2,
    fallendb,
    pytgcalls,
)
from FallenMusic.Helpers.active import add_active_chat, is_active_chat, stream_on
from FallenMusic.Helpers.downloaders import audio_dl
from FallenMusic.Helpers.errors import DurationLimitError
from FallenMusic.Helpers.gets import get_file_name, get_url
from FallenMusic.Helpers.inline import buttons
from FallenMusic.Helpers.queue import put
from FallenMusic.Helpers.thumbnails import gen_qthumb, gen_thumb


@app.on_message(command("رفع نمله"))
async def rf3nmla(client, message):
  if not message.reply_to_message.from_user.mention in nmla:
    nmla.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n نمله 😂♥️")


@app.on_message(command("تنزيل نمله"))
async def tnzelnmla(client, message):
  if message.reply_to_message.from_user.mention in nmla:
    nmla.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n نمله 😂♥️")


@app.on_message(command("المرفوعين نمل"))
async def nml(client, message):
  nq = ""
  for n in nmla:
      nq += n + "\n"
  await message.reply_text(nq)





@app.on_message(command("رفع صرصار"))
async def rf3srsar(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n صرصار 😂♥️")


@app.on_message(command("تنزيل صرصار"))
async def tnzelsrar(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n صرصار 😂♥️")


@app.on_message(command("رفع رقاصه"))
async def yasooo(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n رقاصه حد يرمي فلوس عليها 😂💃")


@app.on_message(command("تنزيل رقاصه"))
async def yaso(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n رقاصه تابت😂😔")
  
  
@app.on_message(command("رفع متناك"))
async def bjoiuyjk(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n متناك حد يركبو 😂♥️")


@app.on_message(command("تنزيل متناك"))
async def kamal(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n متناك اعرث تاب 😂♥️")
  
  
@app.on_message(command("رفع نجس"))
async def fdsa(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n نجس بنجاح  😂♥️")


@app.on_message(command("تنزيل نجس"))
async def kophvc(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n النجس استحمي 😂♥️")
  
  
@app.on_message(command("رفع عره"))
async def roky(client, message):
  await message.reply_text(f"تم رفع العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n عره عالمجتمع 😂♥️")


@app.on_message(command("تنزيل عره"))
async def zerso(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n عره خلاص 😂♥️")
  
  
@app.on_message(command("رفع بقره"))
async def vvvtyy(client, message):
  await message.reply_text(f"تم رفع العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n بقا بقر حديحلبو 🐄🤭")


@app.on_message(command("تنزيل بقره"))
async def tttryuh(client, message):
  await message.reply_text(f"تم تنزيل العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n خلاص خلص لبن 😂")
  
  
@app.on_message(command("رفع قرد"))
async def uiipppl(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n قرد حد يديلو موزه 😂🐒")


@app.on_message(command("تنزيل قرد"))
async def bjhupq(client, message):
  await message.reply_text(f"تم تنزيل العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n القرد بقا انسان🙊🧍")
  
  
@app.on_message(command("رفع قلبي"))
async def pooiejh(client, message):
  await message.reply_text(f"تم رفع العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n خلاص بقيت قلبو 😂♥️")


@app.on_message(command("تنزيل قلبي"))
async def ttrqew(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\nمبقتش قلبوو 😭💔")
  
  
@app.on_message(command("رفع خدام"))
async def qyui(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خدام تع خدم ع البار    😂🤓")


@app.on_message(command("تنزيل خدام"))
async def klhj(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n الخدام ساب الشغل  😢🚶")
  
  
@app.on_message(command("رفع معرص"))
async def wqew(client, message):
  await message.reply_text(f"تم رفع العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n معرص البار  😂🤓")


@app.on_message(command("تنزيل معرص"))
async def ohho(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n المعرص بقا راجل   😂🧔")
  
  
@app.on_message(command("رفع ارمله"))
async def drsss(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  بقيتي ارمله وجوزك مات 🥹")


@app.on_message(command("تنزيل ارمله"))
async def gkvdr(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خلاث متبقيش قموصه جوزك عايش اهو 😂🫶🏻")
  
  
@app.on_message(command("رفع مزه"))
async def cgfyu6f(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n يمزه خدي بالك من نفسك 🥹❤️")


@app.on_message(command("تنزيل مزه"))
async def hhhhug(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n انتي صدقتي انك مزه ولا اي انا كنت بطبل 😂😝")
  
  
@app.on_message(command("رفع ابني"))
async def cbky(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  بقيت ابنو وكل حياتو🥹🖤")


@app.on_message(command("تنزيل ابني"))
async def ccgy(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n حتي عيلتك مش طيقاك ورموك في الشارع ")
  
  
@app.on_message(command("رفع خاينه"))
async def mkloo(client, message):
  await message.reply_text(f"تم رفع العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n  ي خاينه ي مهزأه ")


@app.on_message(command("تنزيل خاينه"))
async def fkijbh(client, message):
  await message.reply_text(f"تم تنزيل العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n مين الاهبل للي كان مفكر القمر دا ممكن يبقي خاين 🥹🥹💕")  
  
  
@app.on_message(command("رفع بنتي"))
async def yuhhss(client, message):
  await message.reply_text(f"تم رفع العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n بقيتي بنتي وحته من قلبي 🥹❤️❤️❤️")


@app.on_message(command("تنزيل بنتي"))
async def hloih(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\nكنت بهزر انا مخلفتش لسه🤡😂  ")  
  
  
@app.on_message(command("رفع خاين"))
async def kloss(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خنتها كام مره قول متتكسفش يخاين")


@app.on_message(command("تنزيل خاين"))
async def fiihug(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n ايدا طلع سوء تفاهم انت اشرف من الشرف يسالك😂❤️")
  
  
@app.on_message(command("رفع خول"))
async def dadr(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n 😂 خول طول عمرك مش اول مره")


@app.on_message(command("تنزيل خول"))
async def hjj7gv(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  اهو يعم نزلتك 🙂💕")
  
  
@app.on_message(command("رفع حمار"))
async def cgfyu6f(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خلاص بقت حمار رسمي نظمي😹")


@app.on_message(command("تنزيل حمار"))
async def cxxv(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خلاث يعم كنا بنهزر معاك متبقاش قفوش 😂😝")
  
  



@app.on_message(command("رفع غبي"))
async def polkij(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n غبي و هتفضل غبي😹🤞")


@app.on_message(command("تنزيل غبي"))
async def nbvcc(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n غبي و بقي بيفهم😹🫶")
  
  
@app.on_message(command("رفع مراتي"))
async def ttttuhyp(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n مراتك خد و عملو واحد😹😽")


@app.on_message(command("تنزيل مراتي"))
async def xxxxt(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n طلقتها شوف غيرها 😂😝")  
  
  
@app.on_message(command("رفع زبال"))
async def oooph(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n زبال تع  نضف الجروب😹")


@app.on_message(command("تنزيل زبال"))
async def zzzas(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n زبال تعب و استقال 😂😝")  
  
  
@app.on_message(command("رفع خدامه"))
async def ggggop(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خدامه تع اغسلي رجلي 😹🤞")


@app.on_message(command("تنزيل خدامه"))
async def vvvuu(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\nخدامه نزلت اجازه😹🫶")  
  
  
@app.on_message(command("رفع كلبه"))
async def mmmuy(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n كلبه خدي عضمه😹🤞")


@app.on_message(command("تنزيل كلبه"))
async def dfrewq(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خلاث كلبه تحولت الانسان😿😹")  
  
  
@app.on_message(command("رفع طيز"))
async def ssoss(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n طيز و كبيره كمان😹🤞")


@app.on_message(command("تنزيل طيز"))
async def nobo(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n طيز متزعلش نزلتك😹🫶")  
  
  
@app.on_message(command("رفع حرامي"))
async def llok(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n حرامي وهبلغ عنه😹🚓")


@app.on_message(command("تنزيل حرامي"))
async def kaompj(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n حرامي ربنا تاب عليه😂😔")
  

@app.on_message(
    command(["الالعاب","العاب"])
  
)
async def zohary(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cde2b51203fbdab57fac5.jpg",
        caption= GAME_MESSAGE,
        reply_markup=InlineKeyboardMarkup(GAME_BUTTONS)
    )  
@app.on_callback_query()
async def callback_query(client, CallbackQuery):
          if CallbackQuery.data == "GAME1":
            
             GAME1_MESSAGE = "⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 ━⊶★━⩺\n\nمرحبا بك في قسم العاب هانتر 3D\n\n⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 ━⊶★━⩺"

             GAME1_BUTTONS = [
                 [
                    InlineKeyboardButton(
                        "°فلابي بيرد°", url=f"http://t.me/awesomebot?game=FlappyBird"), 
                    InlineKeyboardButton (
                        "°تبديل النجوم°", url=f"http://t.me/gamee?game=Switchy"),
                ],[
                    InlineKeyboardButton (
                        "°موتسيكلات°" , url=f"http://t.me/gamee?game=motofx"),
                    InlineKeyboardButton (
                        "°اطلاق النار°" , url=f"http://t.me/gamee?game=NeonBlaster"),
                ],[
                    InlineKeyboardButton (
                        "°كرة القدم°" , url=f"http://t.me/gamee?game=Footballstar"),
                    InlineKeyboardButton (
                        "°تجميع الالوان°" , url=f"http://t.me/awesomebot?game=Hextris"),
                ],[        
                    InlineKeyboardButton (
                        "°المجوهرات°" , url=f"http://t.me/gamee?game=DiamondRows"),
                    InlineKeyboardButton (
                        "°ركل الكرة°" , url=f"http://t.me/gamee?game=KeepitUP"),
                ],[        
                    InlineKeyboardButton (
                        "°بطولة السحق°" , url=f"http://t.me/gamee?game=SmashRoyale"),
                    InlineKeyboardButton (
                        "°2048°" , url=f"http://t.me/awesomebot?game=g2048"),
                ],[        
                    InlineKeyboardButton (
                        "°كرة السلة°" , url=f"http://t.me/gamee?game=BasketBoy"),
                    InlineKeyboardButton (
                        "°القط المجنون°" , url=f"http://t.me/gamee?game=CrazyCat"),
                ],[
                    InlineKeyboardButton (
                        "◁" , callback_data= 'GAME')
                  ],
             ]
             await CallbackQuery.edit_message_text( 
                 GAME1_MESSAGE ,
                 reply_markup = InlineKeyboardMarkup(GAME1_BUTTONS) 
              )
          elif CallbackQuery.data == "GAME":
               
               RETURN_GAME = "⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 ━⊶★━⩺\n\n★¦مرحبا بك في قسم العاب هانتر\n★¦اختار ما تشاء من الالعاب مسليه وستمتع بها\n\n⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 ━⊶★━⩺" 

               RETURN_BUTTON = [
                    [ 
                      InlineKeyboardButton ('★¦العاب 3D', callback_data= 'GAME1'),
                      InlineKeyboardButton ('★¦العاب هانتر', callback_data= 'GAME2')
                      ],[
        InlineKeyboardButton ('𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 ⚡️', url =f"https://t.me/huntersource")              
                 ],[
                InlineKeyboardButton(
                        "◁", callback_data="close"),
               ],
          ]
     
               await CallbackQuery.edit_message_text( 
                 RETURN_GAME ,
                 reply_markup = InlineKeyboardMarkup(RETURN_BUTTON) 
                    )
          elif CallbackQuery.data == "GAME2":
               
               SOURCE_GAME = "⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 ━⊶★━⩺\n\n★¦العاب هانتر\n★¦كت\n★¦تويت\n★¦اسال\n★¦اصراحه\n\n⩹━★⊷━𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 ━⊶★━⩺." 

               SORGAM_BUTTON = [
                    [ 
                      InlineKeyboardButton ('𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 ⚡️', url =f"https://t.me/huntersource")
                      ],[
                         InlineKeyboardButton ('◁', callback_data= 'GAME')
                    ]
               ]    
               await CallbackQuery.edit_message_text( 
                 SOURCE_GAME ,
                 reply_markup = InlineKeyboardMarkup(SORGAM_BUTTON) 
                    )

@app.on_message(
    filters.command(["play", "شغل", "تشغيل"]) | filters.command(["تشغيل","شغل","ش"],prefixes= ["/", "!","","#"])
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    fallen = await message.reply_text("✘ جارٍ التحميل ⚡")
    try:
        await message.delete()
    except:
        pass

    try:
        try:
            get = await app.get_chat_member(message.chat.id, ASS_ID)
        except ChatAdminRequired:
            return await fallen.edit_text(
                f"✘ اديني صلاحية الاضافة علشان اضيف المساعد {BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴛᴏ {message.chat.title}."
            )
        if get.status == ChatMemberStatus.BANNED:
            unban_butt = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=f"الغاء حظر {ASS_NAME}",
                            callback_data=f"unban_assistant {message.chat.id}|{ASS_ID}",
                        ),
                    ]
                ]
            )
            return await fallen.edit_text(
                text=f"✘ {BOT_NAME} الحساب المساعد محظور في {message.chat.title}\n\n✘ الايدي : `{ASS_ID}`\n✘ آلآسم : {ASS_MENTION}\n✘ اليوزر : @{ASS_USERNAME}\n\n✘ الغي حظر الحساب المساعد...",
                reply_markup=unban_butt,
            )
    except UserNotParticipant:
        if message.chat.username:
            invitelink = message.chat.username
            try:
                await app2.resolve_peer(invitelink)
            except Exception as ex:
                LOGGER.error(ex)
        else:
            try:
                invitelink = await app.export_chat_invite_link(message.chat.id)
            except ChatAdminRequired:
                return await fallen.edit_text(
                    f"✘ اديني صلاحية الاضافة علشان اضيف المساعد {BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴛᴏ {message.chat.title}."
                )
            except Exception as ex:
                return await fallen.edit_text(
                    f"فشلت الدعوة {BOT_NAME} المساعد {message.chat.title}.\n\n**آلسبب :** `{ex}`"
                )
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
        anon = await fallen.edit_text(
            f"✘ انتظر من فضلك يتم اضافة حساب المساعد\n\n {ASS_NAME} في {message.chat.title}."
        )
        try:
            await app2.join_chat(invitelink)
            await asyncio.sleep(2)
            await fallen.edit_text(
                f"{ASS_NAME} ✘ تم الانضمام ✅,\n\n✘ بدء التشغيل..."
            )
        except UserAlreadyParticipant:
            pass
        except Exception as ex:
            return await fallen.edit_text(
                f"فشلت الدعوة {BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴛᴏ {message.chat.title}.\n\n**السبب :** `{ex}`"
            )
        try:
            await app2.resolve_peer(invitelink)
        except:
            pass

    ruser = message.from_user.first_name
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"✘ فشل التشغيل بسبب ان السوره طويلة {DURATION_LIMIT} شغل سوره تانية {BOT_NAME}."
            )

        file_name = get_file_name(audio)
        title = file_name
        duration = round(audio.duration / 60)
        file_path = (
            await message.reply_to_message.download(file_name)
            if not os.path.isfile(os.path.join("downloads", file_name))
            else f"downloads/{file_name}"
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            title = results[0]["title"]
            duration = results[0]["duration"]
            videoid = results[0]["id"]

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            return await fallen.edit_text(f"هناك خطأ\n\n**ايرور :** `{e}`")

        if (dur / 60) > DURATION_LIMIT:
            return await fallen.edit_text(
                f"✘ فشل التشغيل بسبب ان السوره طويلة {DURATION_LIMIT} شغل سوره تانية {BOT_NAME}.."
            )
        file_path = audio_dl(url)
    else:
        if len(message.command) < 2:
            return await fallen.edit_text("✘ اكتب اسم السوره اللي عايز تشغلها")
        await fallen.edit_text("✘ جارٍ التشغيل ⚡")
        query = message.text.split(None, 1)[1]
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
            videoid = results[0]["id"]
            duration = results[0]["duration"]

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            LOGGER.error(str(e))
            return await fallen.edit("✘ فشل في المعالجة جرب مرة أخرى...")

        if (dur / 60) > DURATION_LIMIT:
            return await fallen.edit(
                f"✘ فشل التشغيل بسبب ان الاغنية طويلة {DURATION_LIMIT} شغل اغنية تانية {BOT_NAME}.."
            )
        file_path = audio_dl(url)

    try:
        videoid = videoid
    except:
        videoid = "fuckitstgaudio"
    if await is_active_chat(message.chat.id):
        await put(
            message.chat.id,
            title,
            duration,
            videoid,
            file_path,
            ruser,
            message.from_user.id,
        )
        position = len(fallendb.get(message.chat.id))
        qimg = await gen_qthumb(videoid, message.from_user.id)
        await message.reply_photo(
            photo=qimg,
            caption=f"**✘ تمت الإضافة إلى قائمة الانتظار في {position}**\n\n✘ **العنوان :** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n✘ **المده :** `{duration}` دقيقه\n✘ **مطلوب بواسطة عم الحاج دا 🥰:** {ruser}",
            reply_markup=buttons,
        )
    else:
        stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
        try:
            await pytgcalls.join_group_call(
                message.chat.id,
                stream,
                stream_type=StreamType().pulse_stream,
            )

        except NoActiveGroupCall:
            return await fallen.edit_text(
                "**✘ افتح المكالمة الصوتية اولاً **\n**✘ يرجى التأكد من فتح محادثة الفيديو**"
            )
        except TelegramServerError:
            return await fallen.edit_text(
                "✘ حدثت مشكلة جرب اقفل الكول وافتح تاني"
            )
        except UnMuteNeeded:
            return await fallen.edit_text(
                f"✘ {BOT_NAME} الحساب المساعد مكتوم,\n\nالرجاء فك كتم الحساب المساعد {ASS_MENTION} و المحاوله مرة اخري"
            )

        imgt = await gen_thumb(videoid, message.from_user.id)
        await stream_on(message.chat.id)
        await add_active_chat(message.chat.id)
        await message.reply_photo(
            photo=imgt,
            caption=f"‌‌‏‌‌‏‌‌‏≪⊶⌯━‌‌‏♢ 𝑯𝑼𝑵𝑻𝑬𝑹| 𝑺𝑶𝑼𝑹𝑪𝑬 ♢━‌‌‏⌯⊷≫\n**✘ تـم الـتـشـغـيـل ✅**\n\n✘ **العنوان :** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n✘ **المده :** `{duration}` دقيقه\n✘ **بواسطه :** {ruser}\n‌‌‏‌‌‏‌‌‏≪⊶⌯━‌‌‏♢ 𝑯𝑼𝑵𝑻𝑬𝑹| 𝑺𝑶𝑼𝑹𝑪𝑬 ♢━‌‌‏⌯⊷≫",
            reply_markup=buttons,
        )

    return await fallen.delete()
