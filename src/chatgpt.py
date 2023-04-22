import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

TOKEN = os.getenv("TOKEN")

MODEL_NAME = "gpt-3.5-turbo"

bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)

interview_mode = False

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply(f"Hello! I am chatgpt Telegram bot created by Sagar! \n How may I assist you today?")

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    await message.reply(f"I have cleared the past conversations and context.")

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    help_command = """
    Hi there, I am chatGPT bot created by Sagar! Please follow these commands -
    /start - to start a conversation
    /clear - to clear the previous conversation and context
    /help - to display the help menu
    /interview - to toggle data science interview mode
    I hope this helps
    """
    await message.reply(help_command)

async def ask_question(chat_id):
    global interview_mode

    if not interview_mode:
        return

    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an AI that helps users practice data science interviews by asking them questions."},
            {"role": "user", "content": "Ask me a data science-related question."}
        ]
    )

    question = response['choices'][0]['message']['content']
    await bot.send_message(chat_id=chat_id, text=question)

@dispatcher.message_handler(commands=['interview'])
async def toggle_interview_mode(message: types.Message):
    global interview_mode
    interview_mode = not interview_mode
    if interview_mode:
        await message.reply("Data science interview mode enabled. Let's begin.")
        await ask_question(message.chat.id)
    else:
        await message.reply("Data science interview mode disabled.")

@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    if interview_mode:
        await ask_question(message.chat.id)
    else:
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": message.text}
            ]
        )

        answer = response['choices'][0]['message']['content']
        await bot.send_message(chat_id=message.chat.id, text=answer)

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
