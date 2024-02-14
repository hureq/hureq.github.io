import telebot
import  requests
import json
bot = telebot.TeleBot('6821696581:AAFDwJVmdCaGjv2xO20txotr6wDPcQ35MMw')
API = '523ef93145a0b3ef6aa333a4e5fd606f'


@bot.message_handler(commands=['start'])
def start(messeage):
    bot.send_message(messeage.chat.id, f'Привет, рад тебя видеть, {messeage.from_user.first_name} ! Напиши название своего города')
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f'Сейчас {temp} градусов')
        if temp < 0-15.0:
            image = "img.png"
        elif temp > 0-15.0 and temp < 0-5.0:
            image = 'img_1.png'
        elif temp > 0-5.0:
            image = 'img_2.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, 'Такого города нет, перепроверь!')


bot.polling(none_stop=True)