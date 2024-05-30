import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from random import *
from string import *

from classes import InputException, Document
from helpers import inputTypes, spacer

cred = credentials.Certificate("C:\\Users\\asdasd\\Downloads\\maiapp-aeba5-firebase-adminsdk-czsn6-5140e44663.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def onSeeAllDocs():
    print(f"\n{spacer()}\nВсе документы:\nЗагрузка...\n")
    try:
        docs = db.collection("data").stream()
        for doc in docs:
            print(Document(doc.to_dict()))
        return
    except:
        print('Произошла непредвиденная ошибка.')
        return

def onEditDoc():
    print(spacer())
    id = input('Введите id документа для редактирования\n(exit - выход)\nВвод: ')
    if id == 'exit':
        print('Выход...')
        return
    else:
        try:
            text = input('Введите новый текст для документа: ')
            db.collection('data').document(id).set({
                "id": id,
                "text": text,
            })
            print('Документ отредактирован успешно!\nВы можете просмотреть его новую версию в общем списке.')
            return
        except:
            print('Документ не найден.')
            return

def onDeleteDoc():
    print(spacer())
    id = input('Введите id документа для редактирования\n(exit - выход)\nВвод: ')
    if id == 'exit':
        print('Выход...')
        return
    try:
        db.collection('data').document(id).delete()
        print('Документ удален успешно!')
        return
    except:
        print('Произошла непредвиденная ошибка.\nДокумент не удален.')
        return

def onAddDoc():
    print(spacer())
    text = input('Введите текст для нового документа\n(exit - выход)\nВвод:  ')
    if text == 'exit':
        print('Выход...')
        return
    try:
        id = ''.join(
            choices(
                ascii_uppercase + ascii_lowercase + digits,
                k=20
            )
        )
        db.collection('data').document(id).set(
            {
                "id": id,
                "text":text
            }
        )
        print('Документ успешно добавлен!\nВы можете просмотреть его новую версию в общем списке.')
        return
    except:
        print('Произошла непредвиденная ошибка.')
        return

def main():
    try:
        inp = int(input("Выбор действия:\n(1) Просмотр всех документов\n(2) Редактирвоание документа\n(3) Удаление документа\n(4) Добавление документа\nВведите номер действия: "))
        if inp not in inputTypes:
            raise InputException("Выбран недопустимый номер")

        if inp == inputTypes[0]:
            onSeeAllDocs()
        elif inp == inputTypes[1]:
            onEditDoc()
        elif inp == inputTypes[2]:
            onDeleteDoc()
        else:
            onAddDoc()
    except ValueError:
        print(f'Номером явялется число ({inputTypes[0]}, {inputTypes[1]}, {inputTypes[2]}, {inputTypes[3]})')

main()