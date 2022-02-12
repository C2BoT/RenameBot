from pyrogram import filters
from pyrogram import Client as Client
from Client.Translation import Translation
from Client.Config import Config
from Client.Commands.Buttons import START_BUTTON, HELP_BUTTON, ABOUT_BUTTON
from Client.Commands.Commands import developer, co_developer, source, mt_chat, mt_bot

BOT_USERNAME=Config.BOT_USERNAME # ReStart Option 

@Client.on_callback_query()
async def cb_handler(client, query):

    if query.data == "start":
        await query.answer()

        await query.message.edit_text(
            Translation.START_MSG.format(query.from_user.mention),
            reply_markup=START_BUTTON,
            disable_web_page_preview=True
        )
        return

    elif query.data == "help":
        await query.answer()

        await query.message.edit_text(
            Translation.HELP_MSG,
            reply_markup=HELP_BUTTON,
            disable_web_page_preview=True
