import data.markups


def show_about(bot):
    @bot.message_handler(func=lambda message: message.text == data.markups.markup_strings_dictionary['About'])
    def send_about(message):
        bot.send_message(message.chat.id, f'{data.markups.markup_strings_dictionary['About answer']}')