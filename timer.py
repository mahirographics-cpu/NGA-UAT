import asyncio
import time

from config import EXAM_TIME



async def start_timer(context, chat_id):

    context.user_data["timer_start"] = time.time()

    context.user_data["time_finished"] = False


    await asyncio.sleep(EXAM_TIME)



    # If student already submitted, stop timer
    if context.user_data.get("exam_finished"):

        return



    context.user_data["exam_finished"] = True



    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "⏰ Time is over!\n\n"
            "Your exam has been automatically submitted."
        )
    )



async def get_remaining_time(context):

    if "timer_start" not in context.user_data:

        return EXAM_TIME



    elapsed = (
        time.time()
        -
        context.user_data["timer_start"]
    )


    remaining = EXAM_TIME - int(elapsed)



    if remaining < 0:

        remaining = 0



    minutes = remaining // 60

    seconds = remaining % 60



    return f"{minutes:02d}:{seconds:02d}"