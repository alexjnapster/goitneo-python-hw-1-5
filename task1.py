from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.today().date()
    one_week_ahead = today + timedelta(days=7)
    
    # Визначаємо словник для зберігання імен по днях тижня
    birthdays_this_week = defaultdict(list)
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Забезпечуємо, що маємо лише дату без часу
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження уже минув цього року, дивимося на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Визначаємо, чи припадає день народження на наступний тиждень
        if today <= birthday_this_year <= one_week_ahead:
            day_of_week = birthday_this_year.strftime('%A')
            # Якщо день народження припадає на вихідний, відзначаємо в понеділок
            if day_of_week in ['Saturday', 'Sunday']:
                day_of_week = 'Monday'
            birthdays_this_week[day_of_week].append(name)
    
    # Виведення результатів
    for day, names in birthdays_this_week.items():
        print(f"{day}: {', '.join(names)}")

# Приклад використання функції
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},  
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)}  
]

get_birthdays_per_week(users)
