from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    CallbackQueryHandler,
    MessageHandler,
    CommandHandler,
    filters
)

from config import (
    ADMIN_ID,
    PAYMENT_ACCOUNT_NAME,
    PAYMENT_ACCOUNT_NUMBER,
    PAYMENT_BANK,
    PAYMENT_AMOUNT
)

from database import (
    save_registration,
    get_registration,
    update_registration_status
)


# Conversation states
ASK_NAME, ASK_PHONE, ASK_PROOF, CONFIRM_PAYMENT = range(4)




async def start_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    await query.message.reply_text(
        "📚 UAT Full Practice Package\n\n"
        "Here's what's included:\n\n"
        "📄 A large bank of extra PDF practice questions, covering "
        "Verbal Reasoning, Logical Reasoning, Vocabulary, Analogy, "
        "and Quantitative Reasoning — well beyond this mock exam.\n\n"
        "📝 A PDF study note covering the key concepts, formulas, "
        "and strategies you need to prepare for the UAT.\n\n"
        "This is a one-time package you keep and study at your own pace "
        "(not a live class or tutorial).\n\n"
        "Let's get you registered. What is your full name?"
    )


    return ASK_NAME




async def receive_name(update: Update, context: ContextTypes.DEFAULT_TYPE):

    full_name = update.message.text.strip()

    context.user_data["registration_name"] = full_name


    await update.message.reply_text(
        "📱 What is your phone number?\n\n"
        "We'll use this to contact you and send you the materials "
        "once your payment is confirmed."
    )


    return ASK_PHONE




async def receive_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):

    phone_number = update.message.text.strip()

    context.user_data["registration_phone"] = phone_number


    await update.message.reply_text(
        "💳 Payment Details\n\n"
        f"Account Name: {PAYMENT_ACCOUNT_NAME}\n"
        f"Bank: {PAYMENT_BANK}\n"
        f"Account Number: {PAYMENT_ACCOUNT_NUMBER}\n"
        f"Amount: {PAYMENT_AMOUNT}\n\n"
        "Once you've sent the payment, please upload a screenshot "
        "or photo of your payment proof here.\n\n"
        "Send /cancel to stop registration."
    )


    return ASK_PROOF




async def receive_proof(update: Update, context: ContextTypes.DEFAULT_TYPE):

    photo_file_id = update.message.photo[-1].file_id

    context.user_data["registration_photo"] = photo_file_id


    keyboard = [
        [
            InlineKeyboardButton(
                "✅ Confirm My Payment",
                callback_data="confirm_payment"
            )
        ]
    ]


    await update.message.reply_text(
        "Got your payment proof. Please confirm to submit your "
        "registration for review.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


    return CONFIRM_PAYMENT




async def receive_proof_wrong_type(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Please upload your payment proof as a photo/screenshot, "
        "or send /cancel to stop registration."
    )


    return ASK_PROOF




async def confirm_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    user = update.effective_user

    full_name = context.user_data.get(
        "registration_name",
        user.full_name
    )

    phone_number = context.user_data.get(
        "registration_phone",
        ""
    )

    photo_file_id = context.user_data.get(
        "registration_photo"
    )


    if not photo_file_id:

        await query.message.reply_text(
            "Something went wrong — I don't have your payment proof. "
            "Please upload the photo again."
        )

        return ASK_PROOF


    registration_id = save_registration(
        user.id,
        full_name,
        phone_number,
        user.username,
        photo_file_id
    )


    await query.edit_message_text(
        "✅ Registration submitted!\n\n"
        "Your payment is under review. "
        "We will send you an approval message here once it's confirmed."
    )


    # Notify admin with the proof photo and an approve/reject choice
    keyboard = [
        [
            InlineKeyboardButton(
                "✅ Approve",
                callback_data=f"reg_approve_{registration_id}"
            ),
            InlineKeyboardButton(
                "❌ Reject",
                callback_data=f"reg_reject_{registration_id}"
            )
        ]
    ]


    caption = (
        "🆕 New Practice Materials Registration\n\n"
        f"Name: {full_name}\n"
        f"Phone: {phone_number}\n"
        f"Username: @{user.username if user.username else 'N/A'}\n"
        f"Telegram ID: {user.id}\n"
        f"Registration ID: {registration_id}"
    )


    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo_file_id,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


    context.user_data.pop("registration_name", None)

    context.user_data.pop("registration_phone", None)

    context.user_data.pop("registration_photo", None)


    return ConversationHandler.END




async def cancel_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data.pop("registration_name", None)

    context.user_data.pop("registration_phone", None)

    context.user_data.pop("registration_photo", None)


    await update.message.reply_text(
        "Registration cancelled. You can start again anytime with "
        "the \"Want More Practice\" button."
    )


    return ConversationHandler.END




async def handle_admin_decision(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    if query.from_user.id != ADMIN_ID:

        await query.answer(
            "Not authorized.",
            show_alert=True
        )

        return


    # query.data looks like "reg_approve_5" or "reg_reject_12"
    _, action, registration_id = query.data.split("_", 2)


    registration = get_registration(
        int(registration_id)
    )


    if not registration:

        await query.edit_message_caption(
            caption=(query.message.caption or "") + "\n\n⚠️ Registration not found."
        )

        return


    telegram_id = registration[1]

    full_name = registration[2]


    if action == "approve":

        update_registration_status(
            int(registration_id),
            "approved"
        )


        await context.bot.send_message(
            chat_id=telegram_id,
            text=(
                "🎉 Your registration has been approved!\n\n"
                "Welcome to the UAT Full Practice Package. "
                "We'll be in touch shortly with your PDF practice "
                "questions and PDF study note."
            )
        )


        await query.edit_message_caption(
            caption=(query.message.caption or "") + f"\n\n✅ Approved ({full_name})"
        )


    elif action == "reject":

        update_registration_status(
            int(registration_id),
            "rejected"
        )


        await context.bot.send_message(
            chat_id=telegram_id,
            text=(
                "❌ We couldn't verify your payment proof.\n\n"
                "Please contact support via /contact, or try registering "
                "again with a clearer payment screenshot."
            )
        )


        await query.edit_message_caption(
            caption=(query.message.caption or "") + f"\n\n❌ Rejected ({full_name})"
        )




registration_conv_handler = ConversationHandler(
    entry_points=[
        CallbackQueryHandler(
            start_registration,
            pattern="^practice$"
        )
    ],

    states={
        ASK_NAME: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                receive_name
            )
        ],

        ASK_PHONE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                receive_phone
            )
        ],

        ASK_PROOF: [
            MessageHandler(
                filters.PHOTO,
                receive_proof
            ),
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                receive_proof_wrong_type
            )
        ],

        CONFIRM_PAYMENT: [
            CallbackQueryHandler(
                confirm_payment,
                pattern="^confirm_payment$"
            )
        ]
    },

    fallbacks=[
        CommandHandler(
            "cancel",
            cancel_registration
        )
    ]
)




admin_decision_handler = CallbackQueryHandler(
    handle_admin_decision,
    pattern="^reg_(approve|reject)_\\d+$"
)
