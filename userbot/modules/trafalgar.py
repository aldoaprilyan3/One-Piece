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
    await typew.edit("[ɪɴꜱᴛᴀɢʀᴀᴍ](instagram.com/bxbsakai3)")


@register(outgoing=True, pattern='^.ian(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("[INSTAGRAM](instagram.com/ianjing_)")


@register(outgoing=True, pattern='^.tutor(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("[TUTORIAL](https://t.me/tutorbotx)")


@register(outgoing=True, pattern="^.potek$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")
        await e.edit("❤️")
        await e.edit("💔")


@register(outgoing=True, pattern="^.bro$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("**EHEHEH GUA TAU LO BOT**")
        await e.edit("**TAPI PLISS LAH**")
        await e.edit("**JANGAN NORAK AMAT**")
        await e.edit("**EKEKEKEEK**")
        await e.edit("**CANDA BABI🙏**")


@register(outgoing=True, pattern="^.a$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("**Hehehe**")
        await e.edit("**Engga Dulu 😁🙏 **")


@register(outgoing=True, pattern="^.alay$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("**ALAY LO NGENTOT MAININ USERBOT MULU KESANNYA TU KE NORAKK BEGOO**")


@register(outgoing=True, pattern="^.hai$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("**Hai Salken**")
        await e.edit("**Saya ʙʀᴀᴅʟᴇʏ ☠️ **")
        await e.edit("**Saya Adalah Owner One Piece**")
        await e.edit("**Bisa Dibilang saya adalah manusia tampan 😎**")
        await e.edit("**Oke Sekian Mksh🙇🏿‍♂🙇🏿‍♂**")


@register(outgoing=True, pattern="^.pp$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("**YEU NGENTOT AVA GADA MAKE AKUN FAKE PAKE PP DULU YA TOLOL BIAR BISA LIAT GUA SEBERAPA HINANYA MUKA LU BODOH**")


@register(outgoing=True, pattern='^.axel(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("[INSTAGRAM](instagram.com/axqrptan)")


@register(outgoing=True, pattern="^.o$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("**LAH NGATUR KONTOL SUKA SUKA GUA DONG EMANG LO SIAPA ANJING NGATUR² GUA.**")



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
