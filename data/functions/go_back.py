import data.markups
from data.functions.show_start_markup import show_start_markup


def go_back(bot):
    @bot.message_handler(func=lambda message: message.text == data.markups.markup_strings_dictionary['Back'])
    def back(message):
        bot.send_message(message.chat.id,
                         'Возвращаем вас...',
                         reply_markup=data.markups.start_markup)