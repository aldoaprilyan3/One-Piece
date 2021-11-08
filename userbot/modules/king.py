""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.marine$")
async def usit(e):
    await e.edit(
        f"**𝘏𝘢𝘭𝘭𝘰 𝘚𝘦𝘯𝘴𝘦𝘪 {DEFAULTUSER} 𝘒𝘢𝘭𝘰 𝘈𝘯𝘥𝘢 𝘛𝘪𝘥𝘢𝘬 𝘛𝘢𝘶 𝘗𝘦𝘳𝘪𝘯𝘵𝘢𝘩 𝘜𝘯𝘵𝘶𝘬 𝘔𝘦𝘮𝘦𝘳𝘪𝘯𝘵𝘢𝘩 𝘒𝘶 𝘒𝘦𝘵𝘪𝘬** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[ᴘɪʀᴀᴛᴇꜱ](t.me/RhitoSakai)"
        "\n[ᴏɴᴇ ᴘɪᴇᴄᴇ](https://github.com/aldoaprilyan3/One-Piece)"
        "\n[ɪɴꜱᴛᴀɢʀᴀᴍ](Instagram.com/aldoaprilyan3)")


@register(outgoing=True, pattern="^.linkdeploy$")
async def var(m):
    await m.edit(
        f"**ᴍᴇɴᴜᴊᴜ ᴋᴇ ʜᴇʀᴏᴋᴜ𒁂**\n"
        "\n[┏━━━━ ☙ 𒆙 ☙ ━━━━┓\n               𝑫𝑬𝑷𝑳𝑶𝒀            \n┗━━━━ ☙ 𒆙 ☙ ━━━━┛](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Faldoaprilyan3%2FOne-Piece&template=https%3A%2F%2Fgithub.com%2Faldoaprilyan3%2FOne-Piece)")


CMD_HELP.update({
    "marine":
    "`.marine`\
\nUsage: Bantuan Untuk One Piece.\
\n`.yonkou`\
\nUsage: Cara Langsung Mendeploy Ke Heroku Tanpa Harus Ke  github."
})
