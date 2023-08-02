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
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата/время создания: {note['time']}")

def main():
    data = loadData()
    showData(data)

main()
data = loadData()
showData(data)
