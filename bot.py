
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✈️ Bienvenue sur AvionJet Bot !\n\n"
        "Commandes disponibles :\n"
        "/results - Résultats\n"
        "/stats - Statistiques\n"
        "/history - Historique\n"
        "/help - Aide\n\n"
        "Attention : aucune donnée en temps réel n'est encore connectée."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

async def results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Les résultats en temps réel ne sont pas encore connectés."
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Les statistiques seront disponibles quand une source de résultats sera connectée."
    )

async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🗂️ L'historique des résultats n'est pas encore disponible."
    )

app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("results", results))
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CommandHandler("history", history))

app.run_polling()
  
