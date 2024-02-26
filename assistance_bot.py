from collections import defaultdict
from datetime import datetime, timedelta

def parse_input(user_input):
    """Розбиває введення користувача на команду та аргументи."""
    return user_input.strip().lower().split(" ", 2)

def add_contact(args, contacts):
    """Додає новий контакт до записника з датою народження."""
    if len(args) != 3:
        return "Невірна кількість аргументів. Використання: add username phone YYYY-MM-DD"
    name, phone, birthday = args
    contacts[name] = {"phone": phone, "birthday": birthday}
    return "Контакт додано."

def get_birthdays_per_week(contacts):
    """Виводить контакти, які мають день народження на наступний тиждень."""
    today = datetime.today().date()
    one_week_ahead = today + timedelta(days=7)
    birthdays_this_week = defaultdict(list)

    for name, info in contacts.items():
        birthday_str = info.get("birthday", "")
        if birthday_str:
            birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()
            birthday_this_year = birthday.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            if today <= birthday_this_year <= one_week_ahead:
                day_of_week = birthday_this_year.strftime('%A')
                if day_of_week in ['Saturday', 'Sunday']:
                    day_of_week = 'Monday'
                birthdays_this_week[day_of_week].append(name)

    return "\n".join([f"{day}: {', '.join(names)}" for day, names in birthdays_this_week.items()]) if birthdays_this_week else "Немає днів народження на наступний тиждень."

def main():
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
            response = add_contact(args, contacts)
            print(response)
        elif command == "birthdays":
            response = get_birthdays_per_week(contacts)
            print(response)
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()
