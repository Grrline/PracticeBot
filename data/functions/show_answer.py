import os
import data.markups
import sqlite3


def show_answer(bot):
    @bot.message_handler(func=lambda message: message.text == data.markups.markup_strings_dictionary['First question']
                         or message.text == data.markups.markup_strings_dictionary['Second question']
                         or message.text == data.markups.markup_strings_dictionary['Third question'])
    def send_answer(message):
        database = sqlite3.connect("C:/Users/yaros/Private/Practice Project/Project Files/data/database/database.db", check_same_thread=True)
        cursor = database.cursor()
        query = f""" SELECT answer FROM faq WHERE question = "{message.text}" """
        cursor.execute(query)
        result = cursor.fetchone()
        result = result[0].strip()
        bot.reply_to(message, f'❗ Ответ: {result}')
        cursor.close()
        database.close()