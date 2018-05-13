#-*- coding: utf-8 -*-
#simple example of working with json data.
#This program makee Telegram bot repeat everything you write to him.
import telebot

token = 'Андрію Богдановичу, тут має бути ключ, але я не пишу його, бо всеодно Вам треба мати доступ до бота в телеграмі,' \
        'він я його перероблюю, тому він не матиме такого функціоналу, просто повірте, що він працює'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)



if __name__ == '__main__':
    bot.polling(none_stop=True)

