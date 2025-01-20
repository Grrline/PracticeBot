# ФАЙЛ ДЛЯ ОПРЕДЕЛЕНИЯ MARKUP-ов И ИХ ЗНАЧЕНИЙ

from telebot.types import ReplyKeyboardMarkup

markup_strings_dictionary = {
    'FAQ' : 'FAQ',
    'Help' : 'Помощь',
    'Back' : 'Вернуться',
    'Send resume' : 'Отправить резюме',
    'About' : 'О нас',
    'About answer' : 'Наш бот создан для упрощения процессов найма и обучения сотрудников. Мы предоставляем автоматизированные решения, чтобы сэкономить ваше время и помочь сосредоточиться на важных задачах. Используя наш сервис, вы всегда получите доступ к актуальным материалам и быстрые ответы на вопросы!',
    'First question' : 'Как загрузить резюме?',
    'First answer' : 'Отправьте файл с вашим резюме в чат бота. Поддерживаются форматы PDF и DOC. Если файл не загружается, проверьте формат.',
    'Second question' : 'Как я могу больше узнать о компании?',
    'Second answer' : 'Выберите кнопку "Помощь" на нижней панели, а затем нажмите на кнопку "О нас"',
    'Third question' : 'Могу ли я обновить своё резюме после отправки?',
    'Third answer' : 'Да, просто отправьте новый файл, и он заменит предыдущее резюме.'
}

start_markup = ReplyKeyboardMarkup(resize_keyboard=True)
start_markup.add(markup_strings_dictionary['FAQ'],
                  markup_strings_dictionary['About'],
                  markup_strings_dictionary['Help'])

faq_markup = ReplyKeyboardMarkup(resize_keyboard=True)
faq_markup.add(markup_strings_dictionary['First question'],
               markup_strings_dictionary['Second question'],
               markup_strings_dictionary['Third question'],
               markup_strings_dictionary['Back'],
               markup_strings_dictionary['Help']
               )