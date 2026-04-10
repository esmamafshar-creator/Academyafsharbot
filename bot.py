from telegram import Update, ChatPermissions
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "BURAYA_TOKEN"

users = {}
REQUIRED_INVITES = 5

async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        users[user.id] = 0
        
        await context.bot.restrict_chat_member(
            chat_id=update.effective_chat.id,
            user_id=user.id,
            permissions=ChatPermissions(can_send_messages=False)
        )
        
        await update.message.reply_text(
            f"{user.first_name}, mesaj yazmak için 5 kişi davet etmelisin 🚀"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))

app.run_polling()
