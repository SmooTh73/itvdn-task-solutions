class Employee:
    def __init__(self, name, surname, department, year):
        if type(name) == int or type(surname) == int:
            raise ValueError('''Name or surname can't be integer''')
        if type(year) == str:
            raise ValueError('''Year  can't be string''')
        self.name = name
        self.surname = surname
        self.department = department
        self.year = year
    
    def __str__(self):
        return 'Info: {} {}, {} was hired in {}'.format(self.name, self.surname, self.department, self.year)

first = Employee('Yura', 'Kirchei', 'Cleaner', 2008)
second = Employee('Pavlo', 'Gaman', 'Doctor', 2011)
third = Employee('Ruslan', 'Krishtal', 'C# Developer', 1999)

list_of_employees = [first, second, third]

for employee in list_of_employees:
    if employee.year > 2000:
        print(employee)