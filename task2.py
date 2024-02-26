def parse_input(user_input):
    """Розбиває введення користувача на команду та аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """Додає новий контакт до записника."""
    if len(args) != 2:
        return "Невірна кількість аргументів. Використання: add username phone"
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

def change_contact(args, contacts):
    """Змінює номер телефону існуючого контакту."""
    if len(args) != 2:
        return "Невірна кількість аргументів. Використання: change username phone"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Контакт оновлено."
    else:
        return "Контакт не знайдено."

def show_phone(args, contacts):
    """Виводить номер телефону контакту."""
    if len(args) != 1:
        return "Невірна кількість аргументів. Використання: phone username"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Контакт не знайдено."

def show_all(contacts):
    """Виводить всі контакти з номерами телефонів."""
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "Контактів не знайдено."

def main():
    """Основна логіка взаємодії з користувачем."""
    contacts = {}
    print("Ласкаво просимо до бота-помічника!")
    while True:
        user_input = input("Введіть команду: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break
        elif command == "hello":
            print("Як я можу допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()
