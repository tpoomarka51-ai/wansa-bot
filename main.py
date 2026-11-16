import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

JOKES = [
    "مرة واحد محشش دخل الامتحان، كتب اسمو وطلع، قال كفاية انجاز لليوم 😂",
    "قالو ليه ليه بتحب الونسة؟ قال لأنها ببلاش وبتخلي المزاج عال العال 😂",
    "واحد قال لصاحبو: أنا زهجان، قال ليهو: تعال نتوانس، الونسة بتحل كل شي 😂",
]

QUESTIONS = [
    "لو عندك يوم كامل بدون تلفون، حتعمل شنو؟",
    "شنو أكتر حاجة بتخليك تضحك؟",
    "لو سافرت أي حتة في العالم، حتمشي وين؟",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلا بيك في بوت الونسة 🔥\nجرب:\n/نكتة - عشان تضحك\n/سؤال - عشان نتونس")

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(JOKES))

async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(QUESTIONS))

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("نكتة", joke))
    app.add_handler(CommandHandler("سؤال", question))
    print("Bot is running...")
    app.run_polling()
