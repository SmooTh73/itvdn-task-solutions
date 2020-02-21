import functional 

def menu(user_name):
    while True:
        print('Hello, {}, choose what you want to do'.format(user_name), 
                '1) Note site 2) Delete site 3)Show link or site name 4) Exit ')
        menu_choice = int(input(''))
        if menu_choice == 1:
            note_site()
        elif menu_choice == 2:
            name = input('Write name of site which you want delete ')
            print(functional.delete_link(name))
        elif menu_choice == 3:
            what = input('What you want to see? ')
            if what == 'site':
                link = input('Write link ')
                print(functional.show_name(link))
            elif what == 'link':
                name = input('Write name ')
                print(functional.show_link(name))
            else:
                print('Unknown function')
                menu(user_name)
        elif menu_choice == 4:
            return False
        else:
            print('Unknown comand, try again')
            menu(user_name)

def note_site():
    while True:
        operation = int(input('1)Write new site 2) Close this operation '))
        if operation == 1:
            name = input('Write name of site ')
            link = input('Write link ')
            functional.link_record(name, link)
        elif operation == 2:
            return False
        else:
            print('Incorrect number, try again')
            note_site


if __name__=='__main__':
    while True:
        menu('Bob')