import os
from dotenv import load_dotenv
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_USERNAME")
WEBAPP_URL = os.getenv("WEBAPP_URL")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    try:
        member = bot.get_chat_member(CHANNEL, user_id)

        if member.status in ["member", "administrator", "creator"]:
            keyboard = InlineKeyboardMarkup()
            keyboard.add(
                InlineKeyboardButton(
                    "🚀 Open App",
                    web_app=WebAppInfo(WEBAPP_URL)
                )
            )

            bot.send_message(
                message.chat.id,
                "✅ Welcome to Make Your Self Bot",
                reply_markup=keyboard
            )

        else:
            keyboard = InlineKeyboardMarkup()
            keyboard.add(
                InlineKeyboardButton(
                    "📢 Join Channel",
                    url=f"https://t.me/{CHANNEL.replace('@','')}"
                )
            )

            bot.send_message(
                message.chat.id,
                "❌ আগে আমাদের Channel Join করুন।",
                reply_markup=keyboard
            )

    except Exception as e:
        bot.send_message(message.chat.id, str(e))


print("Bot Started...")
bot.infinity_polling()
