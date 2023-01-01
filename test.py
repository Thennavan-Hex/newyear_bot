import telebot
from datetime import date

token = "5862233012:AAFajuDvO7m6CipkiJPLAS8mXA4biuN0_ss"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome Mr.Thennavan")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """
	/start - Start the bot
	/status - to check the status 
	/goals - to see the goals
	/end - to close the bot""")


d = date.today()
l_date = date(2023, 1, 1)
delta = l_date - d
week = delta // 7
day = str(delta.days)
if week.days >= 4:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
elif week.days >= 8:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
elif week.days >= 12:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
elif week.days >= 16:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
elif week.days >= 20:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
elif week.days >= 24:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
elif week.days >= 28:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
elif week.days >= 32:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
elif week.days >= 36:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
elif week.days >= 40:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
elif week.days >= 44:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
elif week.days >= 48:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
elif week.days >= 52:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")
else:
    @bot.message_handler(commands=['status'])
    def send_welcome(message):
        bot.reply_to(message, "You Have only \'" + day + "\' days left")


@bot.message_handler(commands=['goals'])
def send_welcome(message):
    bot.reply_to(message, """
    1.To Place in the company for part-time 
    2. Visit and try the costly restaurant 
    3. Do github commit for all day...""")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
