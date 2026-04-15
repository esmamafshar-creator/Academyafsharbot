import os

print("🚀 BOT STARTING...")

TOKEN = os.getenv("TOKEN")

print("TOKEN:", TOKEN)

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 ربات روشنه!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🤖 RUNNING...")

app.run_polling()
