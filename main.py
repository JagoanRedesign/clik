import os
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery,
)
from pyrogram import Client, filters
from pyrogram.errors import MessageNotModified
from dotenv import load_dotenv
from pyromod import listen 

load_dotenv()


Bot = Client(
    name="confess",
    bot_token=os.environ.get("BOT_TOKEN", "5626754813:AAEQD6i4If1huN3Na_Fk5kF61phaTK5k7Wo"),
    api_id=int(os.environ.get("API_ID", "23693414")),  # type: ignore
    api_hash=os.environ.get("API_HASH", "7886b6a15d0a1a06c7feeaeeb6ad6210"),
)
KR=-1001847941518
Start_text = """<i>Hallo! [Official Fantasy](https://t.me/officialfantasybot) akan membantumu untuk mengirimkan pesan secara anonim ke channel @fvconfess,Silakan Klik tombol <b>🔰 Menu 🔰</b> Untuk Melakunkan Menfes/Biro jodoh.

Sebelum menggunakan silakan baca rules terlebih dahulu ya🥰</i>

<b>Butuh bantuan? Hubungi</b> @phobiakaliann"""
KONTOL = "https://telegra.ph/file/1075382996efe8d8dcb15.jpg"

@Bot.on_message(filters.command(["start"]))
async def start(_, update: Message):
    await update.reply_photo(
        photo=KONTOL,
        caption=Start_text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⛔️ Rules", callback_data="rules"),
                    InlineKeyboardButton("Penjelasan 📝", callback_data="penjelasan"),
                ],
                [
                    InlineKeyboardButton("🔰 Menu 🔰", callback_data="home_ban"),
                ],
            ]
        )
    )
@Bot.on_callback_query(filters.regex("home_ban"))
async def home_ban(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
                       photo=KONTOL,
                       caption=HOME_TEXT,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("🗣 Kritik", callback_data="cbkritik"),
                             InlineKeyboardButton("Confess 📪", callback_data="cbstart"),
                           ],
                           [
                             InlineKeyboardButton("💞 Biro Jodoh 💞", callback_data="cbstart"),
                           ],
                         ]
                       ),
                      ) 
LOG=-1001593451768

@Bot.on_message(filters.command(["confes"]))
async def confess(client: Client, update: Message):
    user_id = update.chat.id
    nama = await client.ask(user_id, '🗣 <b>Ketik Nama kamu</b>\n\n<b>Informasi :</b> __Pakai nama kamu,Jika ingin privasi nama silakan gunakan `Anonim` saja__', filters=filters.text, timeout=30)
    if (nama.text == "/confes"
        or nama.text == "/start"
        or nama.text == "/kritik"
       ):
        name = await client.ask(user_id, '<b>⚠️ Terjadi kesalahan.</b>\n__Jika kamu ingin menyembunyikan identitas kamu silakan ketik__ /secret', filters=filters.text, timeout=30)
        if name.text == "/secret":
            name = "secret"
        else:
            name = name
    if nama.text == "/secret":
        name = "secret"
    else:
        name = nama       
    tujuan = await client.ask(user_id, '🗣 <b>Ketik Nama Crush kamu</b>\n\n<b>Informasi :</b> __Wajib pakai username/nama__', filters=filters.text, timeout=30)
    if (tujuan.text == "/confes"
        or tujuan.text == "/start"
        or tujuan.text == "/kritik"
       ):
        to = await client.ask(user_id, '<b>⚠️ Terjadi kesalahan.</b>\n__Ketik nama crush kamu__', filters=filters.text, timeout=30)
    else:
        to = tujuan
    isi = await client.ask(user_id, f"🗣 <b>Ketik apa yang ingin kamu sampaikan kepada {to.text}</b>", filters=filters.text, timeout=30)
    if (isi.text == "/confes"
        or isi.text == "/start"
        or isi.text == "/kritik"
       ):
        confesss = await client.ask(user_id, '<b>⚠️ Terjadi kesalahan.</b>\n__Ketik apa yang kamu ingin sampaikan kepada crush__', filters=filters.text, timeout=30)
    else:
        confesss = isi
    report = await client.send_message(LOG, f"<b>From :</b> <i>{name.text}</i>\n<b>To :</b> <i>{to.text}</i>\n<b>Isi :</b> <i>{confesss.text}</i>", disable_web_page_preview=True)
    await client.send_message(user_id, f"✅ **Sudah terkirim**", 
                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡ View", url=f"https://t.me/fvconfess/{report.id}")]]),
                              disable_web_page_preview=True,
                             )
        
    
KR=-1001847941518

    
Bot.run()
