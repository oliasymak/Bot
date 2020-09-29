import telebot
bot = telebot.TeleBot('1128991423:AAHSBnWSw1h5J2m6lOLiuwETy1Xa3U5JMDc')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling (non_stop=True)