import telebot

import re
import os

from BitlyAPI import shorten_urls

API_TOKEN = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = message
    bot.reply_to(msg,  
     f"Hi {msg.chat.first_name}!\n\n"
        "I'm bit.ly link converter bot. Just send me link and get shortened link.\n\n Created By @steallootdeal"
    )


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    msg = message
    msgs = msg.text
    Links = (re.search("(?P<url>https?://[^\s]+)", msgs).group("url"))
    Link = [re.search("(?P<url>https?://[^\s]+)", msgs).group("url")]
    response = shorten_urls(Link)
    output = response[0].short_url
    txt = (msgs.replace(Links, str(output)))
    bot.reply_to(msg, txt, disable_web_page_preview=True)

bot.infinity_polling()