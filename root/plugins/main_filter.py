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
    text += f"𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘:\n{filename}\n"
  except:
    # some files dont gib name ..
    filename = None 
    
  text += "𝗦𝗘𝗟𝗘𝗖𝗧 𝗧𝗛𝗘 𝗗𝗘𝗦𝗜𝗥𝗘𝗗 𝗢𝗣𝗧𝗜𝗢𝗡"
  button.append([InlineKeyboardButton("𝗥𝗘𝗡𝗔𝗠𝗘 𝗔𝗦 𝗙𝗜𝗟𝗘", callback_data="rename_file")])
  # Thanks to albert for mime_type suggestion 
  if media.mime_type.startswith("video/"):
    ## how the f the other formats can be uploaded as video 
    button.append([InlineKeyboardButton("𝗥𝗘𝗡𝗔𝗠𝗘 𝗔𝗦 𝗩𝗜𝗗𝗘𝗢",callback_data="rename_video")])
    button.append([InlineKeyboardButton("𝗖𝗢𝗡𝗩𝗘𝗥𝗧 𝗔𝗦 𝗙𝗜𝗟𝗘",callback_data="convert_file")])
    button.append([InlineKeyboardButton("𝗖𝗢𝗡𝗩𝗘𝗥𝗧 𝗔𝗦 𝗩𝗜𝗗𝗘𝗢",callback_data="convert_video")])
  button.append([InlineKeyboardButton("𝗖𝗔𝗡𝗖𝗘𝗟 ❌",callback_data="cancel")])
 
  markup = InlineKeyboardMarkup(button)
  try:
    await m.reply_text(text,quote=True,reply_markup=markup,parse_mode="markdown",disable_web_page_preview=True)
  except Exception as e:
    log.info(str(e))
