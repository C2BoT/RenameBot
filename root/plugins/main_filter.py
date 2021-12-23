'''
Renam_eBot
This file is a part of us6a02 rename repo 
Dont kang !!!
© us6a02
'''
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

@Client.on_message(filters.document | filters.video | filters.audio | filters.voice | filters.video_note | filters.animation) 
async def rename_filter(c,m):
  media = m.document or m.video or m.audio or m.voice or m.video_note or m.animation
  ## couldn't add photo bcoz i want all photos to use as thumb..
  
  text = ""
  button = []
  try:
    filename = media.file_name
    text += f"𝒇𝒊𝒍𝒆𝒏𝒂𝒎𝒆:\n{filename}\n"
  except:
    # some files dont gib name ..
    filename = 𝒏𝒐𝒏𝒆 
    
  text += "𝒔𝒆𝒍𝒆𝒄𝒕 𝒕𝒉𝒆 𝒅𝒆𝒔𝒊𝒓𝒆𝒅 𝒐𝒑𝒕𝒊𝒐𝒏"
  button.append([InlineKeyboardButton("𝒓𝒆𝒏𝒂𝒎𝒆 𝒂𝒔 𝒇𝒊𝒍𝒆", callback_data="rename_file")])
  # Thanks to albert for mime_type suggestion 
  if media.mime_type.startswith("video/"):
    ## how the f the other formats can be uploaded as video 
    button.append([InlineKeyboardButton("𝒓𝒆𝒏𝒂𝒎𝒆 𝒂𝒔 𝒗𝒊𝒅𝒆𝒐",callback_data="rename_video")])
    button.append([InlineKeyboardButton("𝒄𝒐𝒏𝒗𝒆𝒓𝒕 𝒂𝒔 𝒇𝒊𝒍𝒆",callback_data="convert_file")])
    button.append([InlineKeyboardButton("𝒄𝒐𝒏𝒗𝒆𝒓𝒕 𝒂𝒔 𝒗𝒊𝒅𝒆𝒐",callback_data="convert_video")])
  button.append([InlineKeyboardButton("𝒄𝒂𝒏𝒄𝒆𝒍 ❌",callback_data="cancel")])
 
  markup = InlineKeyboardMarkup(button)
  try:
    await m.reply_text(text,quote=True,reply_markup=markup,parse_mode="markdown",disable_web_page_preview=True)
  except Exception as e:
    log.info(str(e))
