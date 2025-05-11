import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

WELCOME_MESSAGE = (
    "Добро пожаловать в DELETE_ACOUNT_BOT!\n"
    "Просто введите имя пользователя и:\n"
    "- бот запустит огромную волну жалоб\n"
    "- аккаунт будет заблокирован в течение 48 часов\n\n"
    "Если вы хотите продолжить, напишите /продолжить"
)

FOLLOWUP_MESSAGE = "Следуй по этой ссылке: http://account-oblivion-portal.lovable.app/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

async def continue_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FOLLOWUP_MESSAGE)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("продолжить", continue_command))
    app.run_polling()

if __name__ == "__main__":
    main()
