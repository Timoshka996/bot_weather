from email import message
import json
import requests
import telebot
from telebot import types
import random

url = 'https://api.openweathermap.org/data/2.5/weather'
bot = telebot.TeleBot('5124514952:AAG83-urnv2nQ3tEEnjCUpCJuY6o1VGd3do')
api_weather='6393c79d9a5de74eadcf04f7558edd96'
@bot.message_handler(commands=['start'])
def welcom(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton('Рандомное число')
    item1 = types.KeyboardButton('игра')
    item2 = types.KeyboardButton('Прогноз погоды')
    item3 = types.KeyboardButton('Как дела ?')
    markup.add(item, item1, item2)

    bot.send_message(message.chat.id,
        """Добро пожаловать, {0.first_name}!
         Я - <b>{1.first_name}</b>, 
         бот созданный чтобы быть помогать вам.""".format(
         message.from_user, bot.get_me()),
         parse_mode='html', reply_markup=markup)
    #
    # sts = open('static/sticker.webp', 'rb')
    # bot.send_sticker(message.chat.id, sts)
    # sts.close()

@bot.message_handler(commands=["search"])
def welcome(message):
    msg = "Укажите город/страну"
    bot.send_message(message.chat.id, msg)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
        try:  
            if message.text == 'Прогноз погоды':
                params = {'APPID': api_weather,'q': message.text, 'units': 'metric'}
                result = requests.get(url, params=params)
                weather = result.json()
                bot.send_message(message.from_user.id, "\nВаш город: " + str(weather['name']) + "\nТемпература: " + str(weather['main']['temp']) + " C\n"
                + "Максимальная температура: " + str(weather['main']['temp_max']) + " C\n"
                + "Минимальная температура: " + str(weather['main']['temp_min']) + " C\n"
                + "Скорость ветра: " + str(weather['wind']['speed']) + " m/s\n"
                + "Давление: " + str(weather['main']['pressure']) + " Pa\n"
                + "Влажность: " + str(weather['main']['humidity'])+ " %\n"
                + "Погода: " + str(weather['weather'][0]['description']) + "\n")
            elif message.text == "Привет":
                bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
            elif message.text == "/help":
                bot.send_message(message.from_user.id, "Напиши привет")
            elif message.text == "игра":
                bot.send_message(message.from_user.id, "https://vseigru.net/")
            elif message.text == "Рандомное число":
                bot.send_message(message.from_user.id, random.randint(1,100))
            elif message.text == 'Search':
                msg = 'Укажите город/страну: '
                bot.send_message(message.chat.id, msg)
            else:
                try:
                    CITY = message.text
                    URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={api_weather}'
                    response = requests.get(url = URL).json()
                    city_info = {
                        'city': CITY,
                        'temp':response['main']['temp'],
                        'weather':response['weather'][0]['description'],
                        'wind': response['wind']['speed'],
                        'pressure': response['main']['pressure']
                    }
                    msg = f"{CITY.upper()}, \n Weather is {city_info['weather']}\nTemperature: {city_info['temp']} \nWind: {city_info['wind']} \n Pressure: {city_info['pressure']}"
                    bot.send_message(message.chat.id, msg)
                except:
                    msg1 = 'not fount city, Try again'
                    bot.send_message(message.chat.id, msg1)
        except:
            bot.send_message(message.from_user.id, "Введите страну/город: ")    # else:





bot.polling(none_stop=True)

# if message.text == "Привет":
        #     bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        # elif message.text == "/help":
        #     bot.send_message(message.from_user.id, "Напиши привет")
        # elif message.text == "игра":
        #     bot.send_message(message.from_user.id, "https://vseigru.net/")
        # elif message.text == "Рандомное число":
        #     bot.send_message(message.from_user.id, random.randint(1,100))
        # if message.text =='Прогноз погоды':