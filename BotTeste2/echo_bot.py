import telebot
from telebot import types
from random import choice


TOKEN = ''
tb = telebot.TeleBot(TOKEN)
bot = telebot.TeleBot("5415027263:AAGtaqQSPtsCeJAPVYfCwcbDyeJM35tT78k") # You can set parse_mode by default. HTML or MARKDOWN


numbers = [range(1,65) for i in range(1)]
captions = [
"🐱*Blake Belladonna*🐱\n *Raridade:* A \n *Filiação:* Beacon Academy \n *Time:* RWBY \n *Origem:* Menágerie \n *Raça:* Fauno \n *Volume:* 1",
"🐱*Blake Belladonna*🐱\n *Raridade:* S \n *Filiação:* Ozpin \n *Time:* RWBY \n *Origem:* Menágerie \n *Raça:* Fauno \n *Volume:* 4",
"🐱*Blake Belladonna*🐱\n *Raridade:* S+ \n *Filiação:* Team RWBY \n *Time:* RWBY \n *Origem:* Menágerie \n *Raça:* Fauno \n *Volume:* 8",
"🦾*Yang Xiao long*🦾\n *Raridade:* A \n *Filiação:* Beacon Academy \n *Time:* RWBY \n *Origem:* Patch Island \n *Raça:* Humana \n *Volume:* 1",
"🦾*Yang Xiao long*🦾\n *Raridade:* S \n *Filiação:* Ozpin \n *Time:* RWBY \n *Origem:* Patch Island \n *Raça:* Humana \n *Volume:* 4",
"🦾*Yang Xiao long*🦾\n *Raridade:* S+ \n *Filiação:* Team RWBY \n *Time:* RWBY \n *Origem:* Patch Island \n *Raça:* Huamana \n *Volume:* 8",
"🌹*Ruby Rose*🌹\n *Raridade:* A \n *Filiação:* Beacon Academy \n *Time:* RWBY \n *Origem:* Patch Island \n *Raça:* Humana \n *Volume:* 1",
"🌹*Ruby Rose*🌹\n *Raridade:* S \n *Filiação:* Ozpin \n *Time:* RWBY \n *Origem:* Patch Island \n *Raça:* Humana \n *Volume:* 4",
"🌹*Ruby Rose*🌹\n *Raridade:* S+ \n *Filiação:* Team RWBY \n *Time:* RWBY \n *Origem:* Patch Island \n *Raça:* Humana \n *Volume:* 8",
"❄*Weiss Schnee*❄\n *Raridade:* A \n *Filiação:* Beacon Academy \n *Time:* RWBY \n *Origem:* Atlas \n *Raça:* Humana \n *Volume:* 1",
"❄*Weiss Schnee*❄\n *Raridade:* S \n *Filiação:* Ozpin \n *Time:* RWBY \n *Origem:* Atlas \n *Raça:* Humana \n *Volume:* 4",
"❄*Weiss Schnee*❄\n *Raridade:* S+ \n *Filiação:* Team RWBY \n *Time:* RWBY \n *Origem:* Atlas \n *Raça:* Huamana \n *Volume:* 8",
]
photos = []



@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['blake'])
def sendphoto(message):
    bot.send_photo(message.chat.id, 'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/Blake%20V4%20-%20A.png',
                   caption="🐱*Blake Belladonna*🐱\n *Raridade:* A \n *Filiação:* Beacon Academy \n Time: RWBY \n Origem: Menágerie \n Raça: Fauno \n",
                   parse_mode='MarkdownV2')



bot.polling(none_stop=True, timeout=60)

