import data.markups


def show_faq(bot):
    @bot.message_handler(func=lambda message: message.text == data.markups.markup_strings_dictionary['FAQ'])
    def send_faq(message):
        bot.reply_to(message,
                     '❓ FAQ ❓\n\n'
                     
                     f'🔴 {data.markups.markup_strings_dictionary['First question']}\n'
                     f'🔵 {data.markups.markup_strings_dictionary['Second question']}\n'
                     f'🟡 {data.markups.markup_strings_dictionary['Third question']}',
                     reply_markup=data.markups.faq_markup)