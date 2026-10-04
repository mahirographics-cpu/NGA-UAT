from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from exam_data import questions
from results import calculate_results
from timer import start_timer, get_remaining_time
from database import save_student
from config import EXAM_TIME_TEXT



async def start_exam(query, context):

    context.user_data["current"] = 0
    context.user_data["answers"] = {}
    context.user_data["exam_finished"] = False


    # Save student information
    save_student(
        query.from_user
    )


    context.user_data["student_id"] = (
        query.from_user.id
    )


    # Start timer
    context.application.create_task(
        start_timer(
            context,
            query.message.chat.id
        )
    )


    await show_question(
        query,
        context
    )





def create_question_buttons(context):

    buttons = []

    answers = context.user_data.get(
        "answers",
        {}
    )

    current = context.user_data["current"]


    row = []


    for i in range(len(questions)):

        label = f"Q{i + 1}"


        if i == current:

            label = "🔵" + label


        elif i in answers:

            label = "🟢" + label


        else:

            label = "⚪" + label



        row.append(
            InlineKeyboardButton(
                label,
                callback_data=f"question_{i}"
            )
        )


        if len(row) == 5:

            buttons.append(row)

            row = []



    if row:

        buttons.append(row)


    return buttons





async def show_question(query, context):

    current = context.user_data["current"]

    question = questions[current]


    keyboard = []


    selected = context.user_data["answers"].get(
        current
    )


    for option in ["A", "B", "C", "D"]:

        label = option


        if selected == option:

            label = "✅ " + option


        keyboard.append(
            [
                InlineKeyboardButton(
                    label,
                    callback_data=f"answer_{option}"
                )
            ]
        )



    keyboard.extend(
        create_question_buttons(context)
    )



    if current == len(questions) - 1:

        keyboard.append(
            [
                InlineKeyboardButton(
                    "✅ Finish Exam",
                    callback_data="finish"
                )
            ]
        )



    remaining = await get_remaining_time(
        context
    )


    text = (
        f"📚 {question['section']}\n\n"
        f"⏱ Time Left: {remaining}\n\n"
        f"Question {current + 1}/{len(questions)}\n\n"
        f"{question['question']}\n\n"
        f"A. {question['options'][0]}\n"
        f"B. {question['options'][1]}\n"
        f"C. {question['options'][2]}\n"
        f"D. {question['options'][3]}\n\n"
        "🔵 Current  🟢 Answered  ⚪ Unanswered"
    )



    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )





async def answer_question(query, context, answer):

    current = context.user_data["current"]


    context.user_data["answers"][current] = answer


    await show_question(
        query,
        context
    )





async def change_question(query, context, number):

    if number < 0:

        number = 0


    if number >= len(questions):

        number = len(questions) - 1



    context.user_data["current"] = number


    await show_question(
        query,
        context
    )





async def finish_exam(query, context):

    context.user_data["exam_finished"] = True


    result = calculate_results(
        context
    )


    keyboard = [
        [
            InlineKeyboardButton(
                "📖 Review Mistakes",
                callback_data="review"
            )
        ],
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


    text = (
        "🎉 Exam Completed!\n\n"
        "📊 Your Result\n\n"
        f"Score: {result['score']}/{result['total']}\n"
        f"Accuracy: {result['percentage']}%\n\n"
        f"🗣 Verbal: "
        f"{result['verbal_score']}/{result['verbal_total']}\n"
        f"🔢 Quantitative: "
        f"{result['quantitative_score']}/"
        f"{result['quantitative_total']}\n\n"
        "Choose an option:"
    )


    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )