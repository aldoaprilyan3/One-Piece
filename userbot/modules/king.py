""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.marine$")
async def usit(e):
    await e.edit(
        f"**๐๐ข๐ญ๐ญ๐ฐ ๐๐ฆ๐ฏ๐ด๐ฆ๐ช {DEFAULTUSER} ๐๐ข๐ญ๐ฐ ๐๐ฏ๐ฅ๐ข ๐๐ช๐ฅ๐ข๐ฌ ๐๐ข๐ถ ๐๐ฆ๐ณ๐ช๐ฏ๐ต๐ข๐ฉ ๐๐ฏ๐ต๐ถ๐ฌ ๐๐ฆ๐ฎ๐ฆ๐ณ๐ช๐ฏ๐ต๐ข๐ฉ ๐๐ถ ๐๐ฆ๐ต๐ช๐ฌ** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[แดษชสแดแดแด๊ฑ](t.me/RhitoSakai)"
        "\n[แดษดแด แดษชแดแดแด](https://github.com/aldoaprilyan3/One-Piece)"
        "\n[ษชษด๊ฑแดแดษขสแดแด](Instagram.com/aldoaprilyan3)")


@register(outgoing=True, pattern="^.yonkou$")
async def var(m):
    await m.edit(
        f"**๐ป๐๐๐๐๐๐๐ ๐ณ๐๐๐๐๐ข ๐บ๐ ๐ท๐๐๐๐๐ ๐พ๐๐ ๐ฟ๐๐๐๐ ๐๐๐๐๐๐๐**\n"
        "\n[โโโโโ โ ๐ โ โโโโโ\n               ๐ซ๐ฌ๐ท๐ณ๐ถ๐            \nโโโโโ โ ๐ โ โโโโโ](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2Faldoaprilyan3%2FOne-Piece%2Ftree%2FLord-Userbot)")


CMD_HELP.update({
    ".marine":
    "`.marine`\
\nUsage: Bantuan Untuk One Piece.\
\n`.yonkou`\
\nUsage: Cara Langsung Mendeploy Ke Heroku Tanpa Harus Ke  github."
})
