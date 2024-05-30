from helpers import spacer


class InputException(Exception):
    pass


class Document:

    def __init__(self, json):
        self.id = str(json["id"])
        self.text = str(json["text"])

    def __str__(self):
        return f"ID документа: {self.id}\nТекст документа: {self.text}\n{spacer()}"