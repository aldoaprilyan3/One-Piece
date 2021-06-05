#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677 and SpEcHiDe
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Silakan buka my.telegram.org
Masuk menggunakan akun Telegram Anda
Klik Alat Pengembangan API
Buat aplikasi baru, dengan memasukkan detail yang diperlukan
Periksa bagian pesan tersimpan Telegram Anda ke STRING_SESSION""")
API_KEY = int(input("Letakan API_KEY disini: "))
API_HASH = input("Letakan API_HASH disini: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print("Check Telegram Save Message Mu Untuk Copy STRING_SESSION ")
    session_string = client.session.save()
    saved_messages_template = """ Support @xthunderlol
<code>STRING_SESSION</code>: <code>{}</code>
⚠️ <i>Please be careful before passing this value to third parties</i>""".format(session_string)
    client.send_message("me", saved_messages_template, parse_mode="html")
