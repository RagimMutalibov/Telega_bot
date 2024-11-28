import telebot
import random

token = "7744323460:AAENR4icfzpSz6t5Qp6In3zCTX3fj4G1a7A"
bot = telebot.TeleBot(token)

HELP = """
/help - Вывести список доступных команд
/add - добавить задачу в список (формат: /add дата задача @категория)
/show - напечатать все задачи.
/exit - Конец 
/random - добавить случайную задачу на дату Сегодня """
RANDOM_TASKS = [
    ("Записаться на курс в Нетологии", "Обучение"),
    ("Написать Гвидо письмо", "Работа"),
    ("Покормить кошку", "Питомцы"),
    ("Помыть машину", "Транспорт")
]
tasks = {}

def add_todo(date, task, category):
    if len(task) < 3:
        return False
    if date in tasks:
        tasks[date].append((task, category))
    else:
        tasks[date] = []
        tasks[date].append((task, category))
    return True

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=3)
    if len(command) < 4:
        bot.send_message(message.chat.id, "Формат команды: /add дата задача @категория")
        return
    date = command[1].lower()
    task = command[2]
    category = command[3].split('@')[1] if '@' in command[3] else command[3]
    if add_todo(date, task, category):
        text = f"Задача {task} @{category} добавлена на дату {date}"
    else:
        text = "Ошибка: задача должна содержать минимум 3 символа"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message): 
    date = "сегодня"
    task, category = random.choice(RANDOM_TASKS)
    add_todo(date, task, category)
    text = f"Задача {task} @{category} добавлена на дату {date}"
    bot.send_message(message.chat.id, text)  

@bot.message_handler(commands=["show", "print"])
def show(message):  #message.text = /print date1 date2 date3...
    command = message.text.split()
    if len(command) < 2:
        text = "Пожалуйста, укажите хотя бы одну дату"
    else:
        dates = [date.lower() for date in command[1:]]
        text = ""
        for date in dates:
            if date in tasks:
                text += f"\n{date.upper()}\n"
                for task, category in tasks[date]:
                    text += f"[] {task} @{category}\n"
            else:
                text += f"\n{date.upper()}: Задач на эту дату нет\n"
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True) #Постоянно обращается к серверам