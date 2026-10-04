from exam_data import questions



def create_review_pages(context):

    answers = context.user_data.get(
        "answers",
        {}
    )


    pages = []

    current_page = (
        "📋 Mistake Review\n\n"
    )


    found = False



    for index, question in enumerate(questions):

        user_answer = answers.get(index)



        # unanswered
        if user_answer is None:

            found = True

            current_page += (
                "━━━━━━━━━━━━━━\n"
                f"❌ Question {index + 1}\n\n"
                "Status: Unanswered\n\n"
            )



        # wrong answer
        elif user_answer != question["answer"]:

            found = True

            current_page += (
                "━━━━━━━━━━━━━━\n"
                f"❌ Question {index + 1}\n\n"
                f"{question['question']}\n\n"
                f"Your answer: {user_answer}\n"
                f"Correct answer: {question['answer']}\n\n"
                "📘 Explanation:\n"
                f"{question['explanation']}\n\n"
            )



        # Telegram message length protection
        if len(current_page) > 3500:

            pages.append(
                current_page
            )

            current_page = (
                "📋 Mistake Review (continued)\n\n"
            )



    if not found:

        pages.append(
            "🎉 Perfect Score!\n\n"
            "You answered every question correctly."
        )


    else:

        if current_page.strip():

            pages.append(
                current_page
            )



    return pages