from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID
from database import (
    get_total_students,
    get_results_count,
    get_top_scores
)



async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id


    if user_id != ADMIN_ID:

        await update.message.reply_text(
            "❌ You are not authorized to use this command."
        )

        return



    students = get_total_students()

    attempts = get_results_count()


    text = (
        "👨‍💻 Admin Panel\n\n"
        f"👥 Total Students: {students}\n"
        f"📝 Total Attempts: {attempts}\n\n"

        "Available commands:\n"
        "/stats - View statistics\n"
        "/top - View top scores"
    )


    await update.message.reply_text(
        text
    )





async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:

        return



    students = get_total_students()

    attempts = get_results_count()



    await update.message.reply_text(
        "📊 Statistics\n\n"
        f"👥 Students: {students}\n"
        f"📝 Exam Attempts: {attempts}"
    )





async def top_scores(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:

        return



    results = get_top_scores()



    if not results:

        await update.message.reply_text(
            "No exam results yet."
        )

        return



    text = "🏆 Top Scores\n\n"



    position = 1


    for result in results:

        telegram_id = result[0]

        score = result[1]

        total = result[2]

        percentage = result[3]


        text += (
            f"{position}. "
            f"{score}/{total} "
            f"({percentage}%)\n"
        )


        position += 1



    await update.message.reply_text(
        text
    )