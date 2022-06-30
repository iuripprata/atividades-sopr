import telebot


TOKEN = '5415027263:AAGtaqQSPtsCeJAPVYfCwcbDyeJM35tT78k'
tb = telebot.TeleBot(TOKEN)
bot = telebot.TeleBot("5415027263:AAGtaqQSPtsCeJAPVYfCwcbDyeJM35tT78k") # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['bellabunda'])
def sendphoto(message):
    bot.send_photo(message.chat.id, open('Blake V4 - A.png', 'rb'), caption="puta")


bot.polling(none_stop=True, timeout=20)

