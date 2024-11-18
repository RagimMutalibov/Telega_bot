import random
HELP = """
help - напечатать справку по программе
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все задачи.
exit - Конец 
random - добавлять случайную задачу на дату Сегодня
"""

RANDOM_TASKS = ["Записаться на курс в Нетологии", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]
tasks = {   
}

run = True

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print("Задача ", task, " добавлена на дату ", date)

def count_letter(tasks, letter):
    count = 0
    letter = letter.lower()
    for word in tasks:
        if letter in word.lower():
            count += 1
    return count

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("Такой даты нет")
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
        letter = input("Введите букву: ")
        count = count_letter(RANDOM_TASKS, letter)
        print(count)
    else:
        print("Неизвестная команда\nДо свидания!")
        break

