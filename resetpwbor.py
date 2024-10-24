import requests
import pyfiglet

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    k = "<" * 12
    e = ">" * 12
    banner = pyfiglet.figlet_format("D")
    update.message.reply_text(f"{banner}\n𖤍\n   Created by @DizzyMedia join for more Tuto at @GhillieBush\n\n")

def reset(update: Update, context: CallbackContext) -> None:
    try:
        url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"
        headers = {
            "Cookie": "mid=YxfCAQABAAG82m8NRgdsiWEYbhTq; csrftoken=8Ot6Srxbp23reyVuew7mytfMEGFoVrlC",
            "User-Agent": "Instagram 136.0.0.34.124 Android (23/6.0.1; 640dpi; 1440x2392; LGE/lge; RS988; h1; h1; en_US)"
        }
        username = update.message.text.split(' ')[1]
        user_id = requests.get(url="https://i.instagram.com/api/v1/users/web_profile_info/?username=" + username, headers={"x-ig-app-id": "1217981644879628"}).json()["data"]["user"]["id"]
        data = {"user_id": user_id}
        request = requests.post(url=url, headers=headers, data=data).json()["obfuscated_email"]
        update.message.reply_text(f" 💌 Done Reset {request} check your mail")
    except:
        update.message.reply_text("❌ PASS RESET SEND ERROR")

def main() -> None:
    updater = Updater("7564996931:AAHyKbjCJk0_-h44DH6d5KSID2W5Xo_itcY")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("reset", reset))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()