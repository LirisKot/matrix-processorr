"""
Модуль меню - пример нисходящего проектирования
"""

def main():
    """Главная функция программы"""
    print("Добро пожаловать в меню!")
    show_main_menu()
    choice = get_user_choice()
    process_choice(choice)
    print("До свидания!")

def show_main_menu():
    """Показать главное меню"""
    print("=== ГЛАВНОЕ МЕНЮ ===")
    print("1. Показать все опции")
    print("2. Добавить новую запись")
    print("3. Удалить запись")
    print("4. Поиск")
    print("0. Выход")

def get_user_choice():
    """Получить выбор пользователя"""
    return "образец выбора"

def process_choice(choice):
    """Обработать выбор пользователя"""
    print(f"Обрабатывается выбор: {choice}")

# Заглушки для основных функций
def show_all_options():
    """Показать все опции"""
    pass

def add_new_record():
    """Добавить новую запись"""
    return "образец добавления"

def delete_record():
    """Удалить запись"""
    pass

def search_records():
    """Поиск записей"""
    return "образец поиска"

if __name__ == "__main__":
    main()