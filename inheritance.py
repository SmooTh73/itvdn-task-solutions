class Editor:
    def view_document(self):
        print("You are watching the document")

    def edit_document(self):
        print("You can't edit document in free version")

class ProEditor(Editor):
    def edit_document(self):
        print("You can edit the document")


password = input('Введите пароль: ')
if password == '1234':
    account = ProEditor()
else:
    account = Editor()

account.view_document()
account.edit_document()