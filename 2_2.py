HELP = """
help - напечатать справку по программе
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все задачи. """

today = []
tomorrow = []
other = []
run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print("Today:", today)
        print("Tomorrow:", tomorrow) 
        print("Other:", other)
    elif command == "add":
        task = input("Введите название задачи: ")
        date_task = input("Введите дату выполнения задачи: ")
        if date_task == "Сегодня":
            today.append(task)
        elif date_task == "Завтра":
            tomorrow.append(task)
        else:
            other.append(task)
        print("Задача добавлена")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда\nДо свидания!")
        # run = False
        break

