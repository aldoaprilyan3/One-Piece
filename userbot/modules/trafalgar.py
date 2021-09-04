from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum")


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumussalam")


@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumussalam")


@register(outgoing=True, pattern='^.ig(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("[ɪɴꜱᴛᴀɢʀᴀᴍ](instagram.com/aldoaprilyan3)")


@register(outgoing=True, pattern='^.ian(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("[INSTAGRAM](instagram.com/ianjing_)")


@register(outgoing=True, pattern='^.tutor(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("[TUTORIAL](https://t.me/tutorbotx)")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "potek":

        await event.edit(input_str)

        animation_chars = [

            "❤️",

            "💔",

            "❤️",

            "💔"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


CMD_HELP.update({
    "fitur":
    "`P`\
\nUsage: Untuk Memberi Salam.\
\n`L`\
\nUsage: Untuk Menjawab Salam.\
\n`.tutor`\
\nUsage: Memberitahukan Cara Mendeploy bot tanpa susah menjelaskanny.\
\n`.ig`\
\nUsage: Instagram Owner Dari Bot."
})
