import json
from datetime import datetime

def sorting():
    print()
    print("1 - Сортировка по умолчанию")
    print("2 - Сортировка по заголовку")
    print("3 - Сортировка по дате")
    print("Для выхода нажмите любую клавишу")
    command = input()
    with open("data.json", "r") as file:
        data = json.load(file)
    match command:
        case "1":
            data = dict(sorted(data.items(), key=lambda item: item[0]))
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=2)
            print("Сортировка прошла успешно")
        case "2":
            data = dict(sorted(data.items(), key=lambda item: item[1][0]))
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=2)
            print("Сортировка прошла успешно")
        case "3":
            data = dict(sorted(data.items(), key=lambda item: item[1][2]))
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=2)
            print("Сортировка прошла успешно")

def addition():
    with open("data.json", "r") as file:
        data = json.load(file)
    print("Введите название заголовка")
    title = input()
    print("Введите заметку")
    body = input()
    time = datetime.now().strftime('%d.%m.%y %H:%M')
    data_length = int(list(data.keys())[-1])
    data[data_length + 1] = [title, body, time]
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 2)
    print("Ваша заметка успешно сохранена")

def reading():
    with open("data.json", "r") as file:
        data = json.load(file)
    print("Заметку под каким номером желаете открыть?")
    for i in data:
        print(i + " - " + data[i][0])
    num = input()
    print()
    if(num in data.keys()):
        print(data[num][1])
        print("Заметка была создана/отредактирована " + data[num][2])
    else:
        print("Такой заметки не существует")
    print()
    print("1 - Редактировать")
    print("2 - Удалить")
    print("Выход - нажмите любую клавишу")
    command = input()
    match command:
        case "1":
            print("Введите новую заметку:")
            body = input()
            time = datetime.now().strftime('%d.%m.%y %H:%M')
            data[num][1] = body
            data[num][2] = time
            print()
            print(data[num][1])
            print("Заметка была создана/отредактирована " + data[num][2])
            print()
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=2)
        case "2":
            data.pop(num)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=2)
            print()
            print("Заметка успешно удалена")
            print()


flag = True
while(flag):
    print("Что хотите сделать?")
    print("1 - Добавить заметку")
    print("2 - Читать заметку")
    print("3 - Сортировка")
    print("Для выхода нажмите любую клавишу")
    command = input()
    match command:
        case "1":
            addition()
        case "2":
            reading()
        case "3":
            sorting()
        case _:
            flag = False


