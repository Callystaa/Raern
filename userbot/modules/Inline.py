from userbot import tgbot
from telethon import Button, events

rtext = """
🔥 **XBOT REMIX USERBOT** 🔥

   `Running with telethon modules`

**• XBOT version:** X-01
**• Branch:** sql-extended
**• License:** [Raphielscape](https://github.com/ximfine/XBot-Remix/blob/alpha/LICENSE)

__Klik button below to use my repo__
"""


@tgbot.on(events.NewMessage(pattern="/repo"))
async def xrepo(repo):
    await tgbot.send_message(repo.chat_id, rtext,
                             buttons=[[Button.url(text="GITHUB REPO",
                                                  url="https://github.com/ximfine/XBot-Remix")]])
