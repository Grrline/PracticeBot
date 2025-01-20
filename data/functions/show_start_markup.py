import data.markups

def show_start_markup(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome_message(message):
        bot.send_message(message.chat.id,
                         '👋 Привет! 👋\n\n'
                         '🤖 Я - бот-менеджер, которому ты можешь отправить своё 📔резюме📔, посмотреть ответы на ❓часто '
                         'задаваемые вопросы❓ или узнать побольше о нашей 🏢компании🏢!\n\n'
                         
                         '🔴 Выбери одну из кнопок на панели снизу!\n\n'
                         
                         '✏ Информация о вариантах выбора:\n'
                         f'🔵 {data.markups.markup_strings_dictionary['FAQ']} 🔵 - посмотреть ответы на часто задаваемые вопросы\n'
                         f'🟡 {data.markups.markup_strings_dictionary['About']} 🟡 - узнать о нашей компании\n'
                         f'⚪ {data.markups.markup_strings_dictionary['Help']} ⚪ - вызвать это окно (эта кнопка всегда будет с '
                         'вами 😉)',
                         reply_markup=data.markups.start_markup)