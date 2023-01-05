import openai
import asyncio
from telebot.async_telebot import AsyncTeleBot

openai.api_key = "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"
bot = AsyncTeleBot('5662750659:AAH9NniXsGLeiv1SOExi8iHI2_DIsqJnB9w')


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Halo my name is Anastasia. Let's talk?\
""")

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    response = openai.Completion.create(model="text-davinci-003", prompt=message.text, temperature=0, max_tokens=1000)
    await bot.reply_to(message, response['choices'][0]['text'])


asyncio.run(bot.polling())
