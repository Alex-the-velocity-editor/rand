import telebot
from utils import get_courses, get_tutors, get_tutor_courses
from functools import lru_cache

@lru_cache(maxsize=3)
def get_start_keyboard()-> telebot.types.ReplyKeyboardMarkup:
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = telebot.types.KeyboardButton('Все комманды (включая все ПОДкомманды!)')
    button_2 = telebot.types.KeyboardButton('Поиграть')
    button_3 = telebot.types.KeyboardButton('Решить пример')
    button_4 = telebot.types.KeyboardButton('Вывести картинку')
    keyboard.add(button_4)
    return keyboard



