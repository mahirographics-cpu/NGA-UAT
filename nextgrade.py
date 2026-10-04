from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Call this right before your Telegram bot starts its polling loop
keep_alive()

from dotenv import load_dotenv
import os

from exam import (
    start_exam,
    answer_question,
    change_question,
    finish_exam
)

from review import create_review_pages
from exam_data import questions

from database import create_tables

from config import EXAM_TIME_TEXT

from admin import (
    admin,
    stats,
    top_scores
)

from registration import (
    registration_conv_handler,
    admin_decision_handler
)


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL = "@nextgrade_academy"


# Create database tables
create_tables()





async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id


    try:

        member = await context.bot.get_chat_member(
            CHANNEL,
            user_id
        )

        joined = member.status not in [
            "left",
            "kicked"
        ]

    except:

        joined = False



    if joined:

        keyboard = [
            [
                InlineKeyboardButton(
                    "📝 UAT Mock Exam",
                    callback_data="uat"
                )
            ],
            [
                InlineKeyboardButton(
                    "📚 More Practice Questions",
                    callback_data="practice"
                )
            ]
        ]

    else:

        keyboard = [
            [
                InlineKeyboardButton(
                    "📢 Join Channel",
                    url="https://t.me/nextgrade_academy"
                )
            ],
            [
                InlineKeyboardButton(
                    "✅ I Joined",
                    callback_data="check"
                )
            ]
        ]



    await update.message.reply_text(
        "🎓 Welcome to Next Grade Academy\n\n"
        "Your UAT preparation platform.\n\n"
        "Commands:\n"
        "/help - Help\n"
        "/contact - Contact support",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )






async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "📖 Next Grade Academy Help\n\n"
        "• Use /start to open the main menu.\n"
        "• Join our Telegram channel if required.\n"
        "• Select UAT Mock Exam.\n"
        "• Answer questions and submit your exam.\n"
        "• Review mistakes after finishing.\n\n"
        "Need assistance? Use /contact."
    )






async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "📞 Next Grade Academy Support\n\n"
        "Telegram Support:\n"
        "@nextgrade_academysupport"
    )







async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()



    if query.data == "check":

        member = await context.bot.get_chat_member(
            CHANNEL,
            query.from_user.id
        )


        if member.status not in [
            "left",
            "kicked"
        ]:

            await query.edit_message_text(
                "✅ Access granted!\n\n"
                "Welcome to Next Grade Academy 🎓",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "📝 UAT Mock Exam",
                                callback_data="uat"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "📚 More Practice Questions",
                                callback_data="practice"
                            )
                        ]
                    ]
                )
            )


        else:

            await query.answer(
                "Please join the channel first.",
                show_alert=True
            )






    elif query.data == "uat":

        await query.edit_message_text(
            "📝 UAT Mock Exam\n\n"
            f"📌 Total Questions: {len(questions)}\n"
            f"⏱ Time Limit: {EXAM_TIME_TEXT}\n\n"
            "Sections:\n"
            "🗣 Verbal Reasoning\n"
            "🔢 Quantitative Reasoning\n\n"
            "Instructions:\n"
            "• Select one answer\n"
            "• Change answers anytime\n"
            "• Use question navigation\n\n"
            "Good luck 🍀",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "▶ Start Exam",
                            callback_data="start"
                        )
                    ]
                ]
            )
        )






    elif query.data in [
        "start",
        "start_exam"
    ]:

        await start_exam(
            query,
            context
        )






    elif query.data.startswith("answer_"):

        answer = query.data.split("_")[1]


        await answer_question(
            query,
            context,
            answer
        )






    elif query.data.startswith("question_"):

        number = int(
            query.data.split("_")[1]
        )


        await change_question(
            query,
            context,
            number
        )






    elif query.data == "finish":

        await finish_exam(
            query,
            context
        )






    elif query.data == "review":

        pages = create_review_pages(
            context
        )


        for page in pages:

            await query.message.reply_text(
                page
            )


        await query.message.reply_text(
            "What would you like to do next?",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "📚 Want More Practice",
                            callback_data="practice"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "🔄 Retake Exam",
                            callback_data="retake"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "🏠 Main Menu",
                            callback_data="main_menu"
                        )
                    ]
                ]
            )
        )






    elif query.data == "retake":

        context.user_data["current"] = 0

        context.user_data["answers"] = {}


        await start_exam(
            query,
            context
        )






    elif query.data == "main_menu":

        await query.edit_message_text(
            "🎓 Next Grade Academy\n\n"
            "Choose an option:",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "📝 UAT Mock Exam",
                            callback_data="uat"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "📚 More Practice Questions",
                            callback_data="practice"
                        )
                    ]
                ]
            )
        )







app = Application.builder().token(TOKEN).build()



app.add_handler(
    CommandHandler(
        "start",
        start
    )
)


app.add_handler(
    CommandHandler(
        "help",
        help_command
    )
)


app.add_handler(
    CommandHandler(
        "contact",
        contact
    )
)


app.add_handler(
    CommandHandler(
        "admin",
        admin
    )
)


app.add_handler(
    CommandHandler(
        "stats",
        stats
    )
)


app.add_handler(
    CommandHandler(
        "top",
        top_scores
    )
)



app.add_handler(
    registration_conv_handler
)


app.add_handler(
    admin_decision_handler
)


app.add_handler(
    CallbackQueryHandler(
        button_handler
    )
)



print("Bot is running...")


app.run_polling()