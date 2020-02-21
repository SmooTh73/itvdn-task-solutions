class Book:
    def __init__(self, autor, name_of_book, year):
        self.autor = autor 
        self.name_of_book = name_of_book
        self.year = year
        self.info_about_book = '''About book:
Name: {};
Year: {};
Autor: {};'''.format(self.name_of_book, self.year, self.autor)

    def __repr__(self):
        return 'Description {}'.format(self.name_of_book)

    def __str__(self):
        return self.info_about_book
    
    def __eq__(self, other):
        return self.autor == other.autor and self.name_of_book == other.name_of_book

    def __ne__(self, other):
        return self.autor != other.autor or self.name_of_book != other.name_of_book

first = Book('Kafka', 'Reincarnation', '1912')
second = Book('Kafka', 'Reincarnation', '1912')
print(first)
print(repr(first))
print(first != second)