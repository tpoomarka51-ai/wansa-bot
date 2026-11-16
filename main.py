import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلااااا وغلاااا 😍🔥\nنورت بوت الونسة يا زول!\nاكتب /اوامر عشان تشوف الأوامر")

async def awamer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أوامر بوت الونسة 🤖\n\n/نكتة - يرسل ليك نكتة\n/سؤال - سؤال ونسة\n/لعبة - لعبة خيروك\n/اوامر - تشوف القائمة دي")

async def nokta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = ["مرة واحد راسو مربع، لما نام حلم انو بتدحرج 😂", "واحد غبي مشى الدكان قال ليهو عندك بيبسي؟ قال ليهو ايوة، قال ليهو اديني واحد بارد 😂", "مرة استاذ سأل طالب: شنو عاصمة السودان؟ قال ليهو: الخرطوم 😂"]
    await update.message.reply_text(random.choice(jokes))

async def soal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    qs = ["لو خيروك تسافر أي دولة، بتختار وين وليه؟", "أكتر موقف محرج حصل ليك في المدرسة؟", "لو عندك مليار جنيه، أول حاجة بتعملها شنو؟", "بتفضل الصيف ولا الشتاء؟"]
    await update.message.reply_text("سؤال الونسة 🔥\n\n" + random.choice(qs))

async def leba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("خيروك 🔥\n\nتكون غني وممل ولا فقير ومبسوط؟")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("اوامر", awamer))
    app.add_handler(CommandHandler("نكتة", nokta))
    app.add_handler(CommandHandler("سؤال", soal))
    app.add_handler(CommandHandler("لعبة", leba))
    print("Bot is running...")
    app.run_polling()
