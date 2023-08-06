import datetime
import json


def loadData():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return[]
    
def saveData(data):
    with open("data.json", "w") as file:
        json.dump(data, file)
    
def showData(data):
    if not data:
        print("Заметок нет")
    else:
        print("Заметки:")
        for note in data:
            print(f"ID: {note['id']}; Заголовок: {note['title']}; Тело заметки: {note['body']}; Дата/время создания: {note['timestamp']}")

def addData(data, title, body):
    new_data = {
        "id": len(data) + 1,
        "title": title,
        "body": body,
        "timestamp": datetime.datetime.now().isoformat()
    }
    data.append(new_data)
    print("Заметка добавлена")

def editData(data, note_id, title, body):
    for note in data:
        if note["id"] == note_id:
            note["title"] = title
            note["body"] = body
            note["timestamp"] = datetime.datetime.now().isoformat()
            print("Заметка успешно отредактирована!")
            return
    print("Заметка с таким ID не найдена.")

def deleteData(data, note_id):
    for note in data:
        if note["id"] == note_id:
            data.remove(note)
            print("Заметка успешно удалена!")
            return
    print("Заметка с таким ID не найдена.")


data = loadData()
while True:
    print("\nВыберите команду:")
    print("1. Просмотреть все заметки")
    print("2. Добавить новую заметку")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choise = input("Введите номер команды: ")
    if choise == "1":
        showData(data)
    elif choise == "2":
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        addData(data, title, body)
    elif choise == "3":
        note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        editData(data,note_id, title, body)
    elif choise == "4":
        note_id = int(input("Введите ID заметки, которую хотите удалить: "))
        deleteData(data, note_id)
    elif choise == "5":
        saveData(data)
        print("Пока")
        break
    else:
        print("Некорректный ввод. Попробуйте еще раз")


