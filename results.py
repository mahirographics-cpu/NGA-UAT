from exam_data import questions
from database import save_result
from config import EXAM_NAME



def calculate_results(context):

    answers = context.user_data.get(
        "answers",
        {}
    )


    score = 0

    verbal_score = 0

    quantitative_score = 0


    verbal_total = 0

    quantitative_total = 0



    for index, question in enumerate(questions):


        section = question.get(
            "section",
            ""
        )


        if section == "Verbal":

            verbal_total += 1


        elif section == "Quantitative":

            quantitative_total += 1




        user_answer = answers.get(index)



        if user_answer == question["answer"]:

            score += 1


            if section == "Verbal":

                verbal_score += 1


            elif section == "Quantitative":

                quantitative_score += 1




    total = len(questions)



    percentage = round(
        (score / total) * 100
    ) if total > 0 else 0



    # Save student's attempt

    if context.user_data.get(
        "student_id"
    ):

        save_result(
            context.user_data["student_id"],
            EXAM_NAME,
            score,
            total,
            percentage
        )



    return {

        "score": score,

        "total": total,

        "percentage": percentage,


        "verbal_score": verbal_score,

        "verbal_total": verbal_total,


        "quantitative_score": quantitative_score,

        "quantitative_total": quantitative_total

    }