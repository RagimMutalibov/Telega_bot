import telebot

token = "7744323460:AAENR4icfzpSz6t5Qp6In3zCTX3fj4G1a7A"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    if "Рагим" in message.text:
        bot.send_message(message.chat.id, "Ба! Знакомые все лица!")
    elif "Нетология" in message.text:
        bot.send_message(message.chat.id, "Спасибо за прикольный курс!")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True) #Постоянно обращается к серверам