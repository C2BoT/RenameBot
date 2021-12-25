from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello!",
                    buttons=[
                        [Button.url("ButtonUrl", url="https://t.me/us7a5")],
                        [Button.inline("Inline Button",data="example")]
                    ])

@BotzHub.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You clicked a button!")
