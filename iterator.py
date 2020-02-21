class MyIterator:
    def __init__(self, user_list):
        self.list = user_list
        self.current_index = len(user_list) - 1
        self.item = None

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_index < 0:
            raise StopIteration
        self.item = self.list[self.current_index]
        self.current_index = self.current_index - 1
        return self.item


mylist =['a', 'b', 'c'] 
iterator = MyIterator(mylist)
for item in iterator:
    print(item)