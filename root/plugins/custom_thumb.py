'''
Renam_eBot
Thanks to Spechide Unkle as always fot the concept  ♥️
This file is a part of TE_GitHub rename repo 
Dont kang !!!
© TE_GitHub
'''

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

import numpy
import os
from PIL import Image
import time
import pyrogram
from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from root.config import Config
from root.messages import Translation
from root.utils.database import *
logging.getLogger("pyrogram").setLevel(logging.WARNING)



@Client.on_message(filters.photo)
async def save_photo(c,m):
    v = await m.reply_text("okay",True)
    if m.from_user.id is not None:
        # album is sent
        download_location = Config.DOWNLOAD_LOCATION + "/thumb/" + str(m.media_group_id) + "/" + str(m.from_user.id) + "/"
        if not os.path.isdir(download_location):
            os.mkdir(download_location)
        await df_thumb(m.from_user.id, m.message_id)
        await c.download_media(
            message=m,
            file_name=download_location
        )
    else:
        # received single photo
        download_location = Config.DOWNLOAD_LOCATION + "/thumb/" + str(m.from_user.id) + ".jpg"
        await df_thumb(m.from_user.id, m.message_id)
        await c.download_media(
            message=m,
            file_name=download_location
        ) 
        try:
           await v.edit_text("✅ Custom thumbnail Saved. \n This thumbnail will be Permanent for all \n future uploads \n Do /deletethumb to clear your thumbnail!")
        except Exception as e:
          log.info(f"#Error {e}")

@Client.on_message(filters.command(["deletethumb"]))
async def delete_thumbnail(c,m):
    download_location = Config.DOWNLOAD_LOCATION + "/thumb/" + str(m.from_user.id)
    try:
        os.remove(download_location + ".jpg")
        await del_thumb(m.from_user.id)
    except:
        pass
    await m.reply_text("𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝘄𝗮𝘀 𝗿𝗲𝗺𝗼𝘃𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 😋",quote=True)

@Client.on_message(filters.command(["showthumb"]))
async def show_thumbnail(c,m):
    thumb_image_path = Config.DOWNLOAD_LOCATION + "/thumb/" + str(m.from_user.id) + ".jpg"
    msgg = await m.reply_text("𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹",quote=True)

    if not os.path.exists(thumb_image_path):
        mes = await thumb(m.from_user.id)
        if mes is not None:
            msgg = await c.get_messages(m.chat.id, mes.msg_id)
            await msgg.download(file_name=thumb_image_path)
            thumb_image_path = thumb_image_path
        else:
            thumb_image_path = None

    if thumb_image_path is None:
        try:
            await msgg.edit_text("𝗡𝗼 𝗦𝗮𝘃𝗲𝗱 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗙𝗼𝘂𝗻𝗱")
        except:
              pass               
    else:
        try:
           await msgg.delete()

        except:
            pass

        await m.reply_photo(
        photo=thumb_image_path,
        caption="𝗧𝗵𝗶𝘀 𝗶𝘀 𝘁𝗵𝗲 𝗦𝗮𝘃𝗲𝗱 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 \n𝗬𝗼𝘂 𝗖𝗮𝗻 𝗱𝗲𝗹𝗲𝘁𝗲 𝘁𝗵𝗶𝘀 𝗯𝘆 𝘂𝘀𝗶𝗻𝗴 \n/deletethumb 𝗖𝗼𝗺𝗺𝗮𝗻𝗱",
        quote=True
    )
