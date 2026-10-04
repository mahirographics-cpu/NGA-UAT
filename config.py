import os
from dotenv import load_dotenv


load_dotenv()


# Telegram bot token
TOKEN = os.getenv("BOT_TOKEN")


# Your Telegram channel
CHANNEL = "@nextgrade_academy"


# Your Telegram ID
# Replace this number with your own Telegram user ID
ADMIN_ID = 5069397446



# Exam settings

EXAM_NAME = "UAT Mock Exam"

EXAM_TIME = 2 * 60 * 60   # seconds (2 hours)

EXAM_TIME_TEXT = "2 Hours"



# Practice materials (PDF + online tutorial) registration settings
# Replace these with your real payment details

PAYMENT_ACCOUNT_NAME = "Your Full Name"

PAYMENT_ACCOUNT_NUMBER = "0000000000"

PAYMENT_BANK = "Your Bank Name"

PAYMENT_AMOUNT = "200 Birr"