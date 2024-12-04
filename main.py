import telebot
from utils import get_tutor_photo
from keyboards import get_start_keyboard
from exceptions import MarkExistError
# сохраняем токен в переменную в виде строки
TOKEN = '7752972005:AAFSKnAeyi231q5g7BNngZaj8VgfcVk0tmc'
# создаем бота и передаем токен доступа
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start']) # обрабатываем команды, которые есть в списке
def handle_command_start(message):
    bot.send_message(
        message.chat.id, 
        "Привет! Я бот! Я умею кое-что делать! Чтобы мною пользоваться, я добавил кнопки!",
        reply_markup=get_start_keyboard()
    )
@bot.callback_query_handler(func=lambda message: message.text == 'Вывести картинку')
def start_mark_process(message):
    photo_id = "photo_5348059179690092945_y.jpg"
    bot.send_photo(message.chat.id, get_tutor_photo(tutor_id=photo_id))
#я не знаю как выводить фотографию :(
print('Сервер запущен.')
# отправка запросов обновлений
bot.polling(
    non_stop=True, # отправка запросов без остановки один за одним
    interval=1 # интервал между запросами
)