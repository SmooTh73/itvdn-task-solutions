class Rectangle:
    def view(self):
        print('You see ', type(self).__name__)

class Button:
    def click(self):
        print("You can press the ", type(self).__name__)

class RectangleButton(Rectangle, Button):
    pass


rectbut = RectangleButton()
rect = Rectangle()
rect.view()
rectbut.view()
rectbut.click()



