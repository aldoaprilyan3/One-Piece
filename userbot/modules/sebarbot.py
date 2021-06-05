# frm Ultroid
# port by Koala @manusiarakitann
# @xthunderlol
# Alvin Ganteng

from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern="^.sebar (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Sensei Tolong Berikan Saya Sebuah Pesan`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`📢 Sedang Mengirim Pesan Secara Global...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**")

# Shadow
CMD_HELP.update(
    {
        "sebar": "`.sebar <pesan>`\
    \nPenjelasan: Global Broadcast mengirim pesan ke Seluruh Grup yang Sensei Masuki."
    })
