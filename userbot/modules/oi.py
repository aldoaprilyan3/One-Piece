from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.pirates(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hallo Perkenalkan Saya Pirates`")
    sleep(3)
    await typew.edit("`Bisa di panggil aldo`")
    sleep(1)
    await typew.edit("`Dari padang, Salam Kenal :v`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(3)
    await typew.edit("`heheh btw napas manualnya kaka`")
    sleep(2)
    await typew.edit("`Canda Bhaks`")
    sleep(1)
    await typew.edit("`And Jangan Lupa Bersyukur`")
# Create by myself @localheart
