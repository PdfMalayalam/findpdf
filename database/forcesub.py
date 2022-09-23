import os
import datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied

FORCE_SUB = "Pdfmalayalam" # os.environ.get("FORCE_SUB", "Pdfmalayalam") if os.environ.get("FORCE_SUB", "") else None
  
#@Client.on_message(filters.private & filters.incoming)
@Client.on_message(filters.command('start') & filters.private)
async def force_sub(c, m):
    if FORCE_SUB:
        try:
            chat = await c.get_chat_member(FORCE_SUB, m.from_user.id)
            if chat.status=='kicked':
                return await m.reply_text('Hai you are kicked from my updates channel. So, you are not able to use me',  quote=True)

        except UserNotParticipant:
            button = [[InlineKeyboardButton('join Updates channel', url=f'https://t.me/Pdfmalayalam')]]
            markup = InlineKeyboardMarkup(button)
            return await m.reply_text(text="Hey join in my updates channel to use me.", parse_mode='markdown', reply_markup=markup, quote=True)

        except ChatAdminRequired:
            #logger.warning(f"Make me admin in @{FORCE_SUB}")
            if m.from_user.id in Config.AUTH_USERS:
                return await m.reply_text(f"Make me admin in @{FORCE_SUB}")

        except UsernameNotOccupied:
            #logger.warning("The forcesub username was Incorrect. Please give the correct username.")
            if m.from_user.id in Config.AUTH_USERS:
                return await m.reply_text("The forcesub username was Incorrect. Please give the correct username.")

        except Exception as e:
            if "belongs to a user" in str(e):
                #logger.warning("Forcesub username must be a channel username Not yours or any other users username")
                if m.from_user.id in Config.AUTH_USERS:
                    return await m.reply_text("Forcesub username must be a channel username Not yours or any other users username")
            #logger.error(e)
            return await m.reply_text("Some thing went wrong. Try again and if same issue occur contact [Him](https://t.me/vipinpkd)", disable_web_page_preview=True, quote=True)
